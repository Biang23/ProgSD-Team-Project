# -*- coding: utf-8 -*-
"""
2022-10-10
@author: Yiyang Bo
"""
import time
import datetime
import numpy as np

# Return the time now
def get_time():

    time = datetime.datetime.now()
    print(type(time))
    return time


"""
Input: start: start time -> datetime.datetime; end: end time -> datetime.datetime
Output: res: time past -> np.array
"""
def calculate_time(start, end):

    start_list = np.array([start.year,start.month,start.day,start.hour,start.minute,start.second])
    end_list = np.array([end.year,end.month,end.day,end.hour,end.minute,end.second])
    
    return end_list-start_list

