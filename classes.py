# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:38:41 2022

@author: 豪帅, Yiyang Bo
"""

import time
from time_op import *
import numpy as np
import matplotlib.pyplot as plt


from pymysql import Connection


#创建对象，构造方法
conn=Connection (
    host='localhost',   #主机名
    port=3306,          #端口
    user='root',        #账户
    password='',        #密码
    autocommit=True     #自动确认机制
    )

print(conn.get_server_info())#打印数据库软件信息


cursor=conn.cursor() #获得游标对象
#选择数据库
conn.select_db("rent")


class Customer():
    def __init__(self, id, rent_id, name, gender, age, rent, money, start, end, latitude, longtitude) -> None:
        self.id = id
        self.rent_id = rent_id  # the vehicle id of which customer rent
        self.name = name
        self.gender = gender
        self.age = age
        self.rent = rent        # boolean. represent whether the customer has rent a vehicle
        self.money = money
        self.start = start      # datetime.datetime
        self.end = end          # datetime.datetime
        self.latitude = latitude
        self.longtitude = longtitude
        
        sql=f"""insert into customer(id,rent_id,name,gender,age,rent,money) values ("%s","%s","%s","%s","%s","%s","%s")"""%(self.id,self.rent_id,self.name,self.gender,self.age,self.rent,self.money)
        cursor.execute(sql)
        
    def rent_vehicle(self, vehicle):
        if self.rent:   #当rent=1的时候
            message = "Sorry. You can only rent ONE vehicle at same time! "
            return message, None
        if vehicle.status != "Available":
            message = "Sorry. The vehicle is {}".format(vehicle.status)
            return message, None
        
        self.rent = True  #当rent=0的时候，把rent的值改变
        """
            self.rent -> DB
        """
        sql=f"""update customer set rent={self.rent} where id={self.id}"""
        cursor.execute(sql)
        
        
        
        
        self.rent_id = vehicle.id
        """
            self.rent_id -> DB
        """
        sql=f"""update customer set rent_id={self.rent_id} where id={self.id}"""
        cursor.execute(sql)
        
        
        self.start = get_time()
        sql=f"""update customer set start={self.start} where id={self.id}"""
        cursor.execute(sql)
        
        message = "Success. Enjoy your journey! Time: {}.".format(self.start)
        return message, self.start

    def return_vehicle(self, vehicle): #换车
        if not self.rent:  #若rent=0
            message = "Sorry. You can only return a vehicle when you have rent one."
            return message, None
        
        self.end = get_time()
        sql=f"update customer set end={self.end} where id={self.id}"
        cursor.execute(sql)
        
        paid_status = False
        while not paid_status:
            paid_status, = self.pay(self.start, self.end)

        self.rent = False  # set rent status to False
        sql=f"update customer set rent={self.rent} where id={self.id}"
        cursor.execute(sql)

        self.rent_id = None
        sql=f"update customer set rent_id={None} where id={self.id}"
        cursor.execute(sql)

        message = "Your rent ends.Time: {}. ".format(self.end)
        return message
    
    def report_vehicle(self, vehicle):
        report_id = input("Please input the vehicle's ID: ")
        return report_id

    def pay(self, vehicle_type, vehicle_spot):  
        paid = False
        
        
        time_list = calculate_time(self.start,self.end)
        total_minute = time_list[0]*525948.766+time_list[1]*43,200+time_list[2]*1440+\
                        time_list[3]*60+time_list[4]+round(time_list[5]/60)
        

        # Several vehicle types
        if vehicle_type == "bicycle":
            amount = total_minute * 10
        elif vehicle_type == "electricycle":
            amount = total_minute * 20
        else:
            amount = total_minute * 30
        
        penalty, penalty_message = self.penalty(self, vehicle_spot) # penalty_message -> list
        if penalty:
            amount += 100
        
        time.sleep(5)
        self.money -= amount
        
        #将数据库的monry值改变并存到数据库里面
        sql=f"update customer set money={self.money} where id={self.id}"
        cursor.execute(sql)
        
        
        while self.money < 0:
            self.charge()
        paid = True
        message = "Thank you. Have a good day! "
        return paid, message, penalty_message
    
    # save money to account
    def charge(self):
        amount = input("Please enter the AMOUNT you wanna charge: ")  
        if amount.isnumeric:
            self.money += float(amount)
            
        sql=f"update customer set money={self.money} where id={self.id}"
        cursor.execute(sql)
        
        message = "Success!"
        return message
    
    def penalty(self, vehicle_spot):
        be_penalty = False
        spot_index = [0]
        dis = np.inf
        loc = np.array([self.latitude, self.longtitude])
        for i in range(len(vehicle_spot)):
            cur_dis = np.linalg.norm(vehicle_spot[i]-loc, 2, axis=0)
            if cur_dis < dis:
                dis = cur_dis
                spot_index.clear()
                spot_index.append(i)
            elif cur_dis == dis:
                spot_index.append(i)
            else:
                continue
        message_box = []
        if dis >= 100.0:
            be_penalty = True
            for j in range(len(spot_index)):
                index = spot_index[j]
                message = "You are far from parking spot. The nearest spot is spot{} at latitude: {}, longtitude: {}".format(index, vehicle_spot[index, 0], vehicle_spot[index, 1])
                message_box.append(message)
        return be_penalty, message_box

class Operator():
    def __init__(self, id, name, gender, age) -> None:
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age

    def track_vehicle(self, locations):
        """
        Connect to the database and export all vehicles' locations
        """
        return locations

    def charge_vehicle(self, vehicle_type):
        if vehicle_type == "electricycle" or vehicle_type == "motorcycle":
            return True
        return False
    
    def repair_vehicle(self, vehicle_status):
        if vehicle_status == "defective":
            return True
        return False

    def move_vehicle(self, old_latitude, old_longtitude, latitude, longtitude):
        if old_latitude != latitude and old_longtitude != longtitude:
            new_latitude = latitude
            new_longtitue = longtitude
            time = (new_latitude+new_longtitue-old_latitude-old_longtitude) * 100
            return True, latitude, longtitude, time
        else:
            return False, old_latitude, old_longtitude, 0


class Manager():
    def __init__(self, id, name, gender, age) -> None:
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age

    def generate_reports(vehicle_data):
        
        time_stamp = vehicle_data[:, 0]
        vehicle_type = vehicle_data[:, 1]

        bicycle_t, electricycle_t, motorcycle_t = [], [], []
        bicycle_n, electricycle_n, motorcycle_n = [], [], []

        for i in len(vehicle_type):

            cur_type = vehicle_type[i]
            cur_time = time_stamp[i]

            if cur_type == 0:
                if cur_time not in bicycle_t:
                    bicycle_t.append(time_stamp[i])
                    bicycle_n.append(int(1))
                else:
                    bicycle_n[-1] += 1
            elif cur_type == 1:
                if cur_time not in electricycle_t:
                    electricycle_t.append(time_stamp[i])
                    electricycle_n.append(int(1))
                else:
                    electricycle_n[-1] += 1
            else:
                if cur_time not in motorcycle_t:
                    motorcycle_t.append(time_stamp[i])
                    motorcycle_n.append(int(1))
                else:
                    motorcycle_n[-1] += 1

        plt.title("Vehicle Report")
        plt.plot(bicycle_t, bicycle_n, color='r')
        plt.plot(electricycle_t, electricycle_n, color='g')
        plt.plot(motorcycle_t, motorcycle_n, color='y')
        plt.legend(['Bicycle', 'Electricycle', 'Motorcycle'], loc=0)
        plt.show()


class vehicle():
    def __init__(self, id, latitude, longtitude, status, type) -> None:
        self.id = id
        self.latitude = latitude
        self.longtitude = longtitude
        self.status = status # Occupied, Available, Charging, Moving, Defective
        self.type = type # bicycle, electricycle, motorcycle
        
        sql=f"""insert into vehicle(id,latitude,longtitude,status,type) values ("%s","%s","%s","%s","%s")"""%(self.id,self.latitude,self.longtitude,self.status,self.type)
        cursor.execute(sql)
        
        
    def be_rent(self, customer):
        self.status = "Occupied"
        return self.status
    
    def be_returned(self, customer):
        self.latitude = customer.latitude
        self.longtitude = customer.longtitude
        """
        self.latitude -> DB
        self.longtitude -> DB
        """
        sql=f"update vehicle set latitude={self.latitude} where id={self.id}"
        cursor.execute(sql)
        sql=f"update vehicle set longtitude={self.longtitude} where id={self.id}"
        cursor.execute(sql)
        
        
        self.status = "Available"
        """
        self.status -> DB
        """
        sql=f"update vehicle set status='{self.status}' where id={self.id}"
        cursor.execute(sql)
        
        return self.status, self.latitude, self.longtitude
        
    def be_reported(self, ID):

        self.status = "Defective"
        """
        self.status -> DB
        """
        sql=f"update vehicle set status='{self.status}' where id={self.id}"
        cursor.execute(sql)
        
        return self.status

    def be_charged(self, need_charge):
        if need_charge:

            self.status = "Charging"
            """
            self.status -> DB
            """
            sql=f"update vehicle set status='{self.status}' where id={self.id}"
            cursor.execute(sql)
            
            time.sleep(5000)

            self.status = "Available"
            """
            self.status -> DB
            """
            sql=f"update vehicle set status='{self.status}' where id={self.id}"
            cursor.execute(sql)

    def be_repaired(self, need_repair):
        if need_repair:

            self.status = "Charging"
            """
            self.status -> DB
            """
            sql=f"update vehicle set status='{self.status}' where id={self.id}"
            cursor.execute(sql)
            
            time.sleep(5000)

            self.status = "Available"
            """
            self.status -> DB
            """
            sql=f"update vehicle set status='{self.status}' where id={self.id}"
            cursor.execute(sql)

    def be_moved(self, need_move, latitude, longtitude):
        if need_move:
            self.latitude = latitude
            self.longtitude = longtitude
            """
            self.latitude -> DB
            self.longtitude -> DB
            """
            sql=f"update vehicle set latitude={self.latitude} where id={self.id}"
            cursor.execute(sql)
            sql=f"update vehicle set longtitude={self.longtitude} where id={self.id}"
            cursor.execute(sql)
            
            self.status = "Moving"
            """
            self.status -> DB
            """
            sql=f"update vehicle set status='{self.status}' where id={self.id}"
            cursor.execute(sql)
            
            time.sleep(time)

            self.status = "Available"
            """
            self.status -> DB
            """
            sql=f"update vehicle set status='{self.status}' where id={self.id}"
            cursor.execute(sql)


# class electric(vehicle):
#     def __init__(self, id, latitude, longtitude, status, electricity) -> None:
#         super(electric, self).__init__(id, latitude, longtitude, status)
#         self.electricity = electricity

# class motor(vehicle):
#     def __init__(self, id, latitude, longtitude, status, oil_quantity) -> None:
#         super(motor, self).__init__(id, latitude, longtitude, status)
#         self.oil_quantity = oil_quantity



# v6=vehicle(6,3.5,4.5,"Available","normal")
# a5=Customer(6,0,"f",1,13,0,5000,"'n'",'213','1010','1235')
# a5.rent_vehicle(v6)


##关闭连接
conn.close()