/*
 Navicat Premium Data Transfer

 Source Server         : rent
 Source Server Type    : MySQL
 Source Server Version : 50022
 Source Host           : localhost:3306
 Source Schema         : rent

 Target Server Type    : MySQL
 Target Server Version : 50022
 File Encoding         : 65001

 Date: 31/10/2022 14:25:32
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for customer-vehicle
-- ----------------------------
DROP TABLE IF EXISTS `customer-vehicle`;
CREATE TABLE `customer-vehicle`  (
  `id` int(255) NULL DEFAULT NULL,
  `cus_id` int(255) NULL DEFAULT NULL,
  `veh_id` int(255) NULL DEFAULT NULL,
  `start` float NULL DEFAULT NULL,
  `end` float NULL DEFAULT NULL,
  `old_latitude` float NULL DEFAULT NULL,
  `old_longtitude` float NULL DEFAULT NULL,
  `new_latitude` float NULL DEFAULT NULL,
  `new_longtitude` float NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of customer-vehicle
-- ----------------------------

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT,
  `rent_id` bigint(255) NULL DEFAULT NULL,
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `gender` tinyint(255) NULL DEFAULT NULL,
  `age` bigint(255) NULL DEFAULT NULL,
  `rent` tinyint(255) NULL DEFAULT NULL,
  `money` float NULL DEFAULT NULL,
  `start` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `end` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `latitude` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `longtitude` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES (1, 0, 'a', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (2, 0, 'b', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (3, 0, 'c', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (4, 0, 'd', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (5, 0, 'e', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (6, 0, 'f', 1, 13, 1, 5000, '1665849519.9200468', NULL, NULL, NULL);
INSERT INTO `customer` VALUES (7, 7, 'f', 1, 13, 1, 5000, '1665849637.1523564', NULL, NULL, NULL);
INSERT INTO `customer` VALUES (8, 0, 'f', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (9, 0, 'f', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);
INSERT INTO `customer` VALUES (10, 0, 'f', 1, 13, 0, 5000, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for manager
-- ----------------------------
DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager`  (
  `id` int(255) NOT NULL DEFAULT '',
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `gender` tinyint(255) NULL DEFAULT NULL,
  `age` int(255) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of manager
-- ----------------------------

-- ----------------------------
-- Table structure for operator-vehicle
-- ----------------------------
DROP TABLE IF EXISTS `operator-vehicle`;
CREATE TABLE `operator-vehicle`  (
  `id` int(11) NULL DEFAULT NULL,
  `ope_id` int(255) NULL DEFAULT NULL,
  `veh_id` int(255) NULL DEFAULT NULL,
  `operation_type` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `old_latitude` float NULL DEFAULT NULL,
  `old_longtitude` float NULL DEFAULT NULL,
  `new_latitude` float NULL DEFAULT NULL,
  `new_longtitude` float NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of operator-vehicle
-- ----------------------------

-- ----------------------------
-- Table structure for operator
-- ----------------------------
DROP TABLE IF EXISTS `operator`;
CREATE TABLE `operator`  (
  `id` int(255) NOT NULL DEFAULT '',
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `gender` tinyint(4) NULL DEFAULT NULL,
  `age` int(255) NULL DEFAULT NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of operator
-- ----------------------------
INSERT INTO `operator` VALUES (1, 'a', 1, 23);

-- ----------------------------
-- Table structure for parking_spots
-- ----------------------------
DROP TABLE IF EXISTS `parking_spots`;
CREATE TABLE `parking_spots`  (
  `id` int(11) NOT NULL DEFAULT '',
  `latitude` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `longtitude` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of parking_spots
-- ----------------------------
INSERT INTO `parking_spots` VALUES (1, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (2, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (3, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (4, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (5, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (6, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (7, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (8, '4.5', '55.5');
INSERT INTO `parking_spots` VALUES (10, '4.5', '55.5');

-- ----------------------------
-- Table structure for vehicle
-- ----------------------------
DROP TABLE IF EXISTS `vehicle`;
CREATE TABLE `vehicle`  (
  `id` int(255) NOT NULL DEFAULT '',
  `latitude` float NULL DEFAULT NULL,
  `longtitude` float NULL DEFAULT NULL,
  `status` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `type` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY USING BTREE (`id`)
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of vehicle
-- ----------------------------
INSERT INTO `vehicle` VALUES (1, 3.5, 4.5, 'Available', 'normal');
INSERT INTO `vehicle` VALUES (2, 3.5, 4.5, 'Available', 'normal');
INSERT INTO `vehicle` VALUES (3, 3.5, 4.5, 'Available', 'electric');
INSERT INTO `vehicle` VALUES (4, 3.5, 4.5, 'Available', 'electric');
INSERT INTO `vehicle` VALUES (5, 3.5, 4.5, 'Available', 'normal');
INSERT INTO `vehicle` VALUES (7, 3.8, 4.5, 'Available', 'normal');
INSERT INTO `vehicle` VALUES (10, 3.8, 4.5, 'Available', 'normal');

SET FOREIGN_KEY_CHECKS = 1;
