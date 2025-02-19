/*
 Navicat Premium Data Transfer

 Source Server         : IT-PROJECT
 Source Server Type    : MySQL
 Source Server Version : 80040
 Source Host           : database-1.c3iemm2ycfl8.us-east-1.rds.amazonaws.com:3306
 Source Schema         : the_platform

 Target Server Type    : MySQL
 Target Server Version : 80040
 File Encoding         : 65001

 Date: 19/02/2025 13:04:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for banner
-- ----------------------------
DROP TABLE IF EXISTS `banner`;
CREATE TABLE `banner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `picture_url` varchar(255) NOT NULL COMMENT '广告图片的url',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted` int NOT NULL DEFAULT '0' COMMENT '0 未删除 （展示1 已删除（不展示',
  `admin_id` int NOT NULL COMMENT '发布这条广告的管理员id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of banner
-- ----------------------------
BEGIN;
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (3, 'www.baidu.com', '2025-02-12 17:14:10', 0, 23);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (4, '/static/pic/1.png', '2025-02-12 17:52:05', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (5, '/static/pic/1.png', '2025-02-12 19:07:05', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (6, '/static/pic/1.png', '2025-02-12 19:08:17', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (7, '/static/pic/1.png', '2025-02-12 19:10:02', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (8, '/static/pic/1.png', '2025-02-12 19:10:27', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (9, '/static/pic/1.png', '2025-02-12 19:10:34', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (10, '/static/pic/1.png', '2025-02-12 19:10:56', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (11, '/static/pic/1.png', '2025-02-12 19:10:56', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (12, '/static/pic/1.png', '2025-02-12 19:10:57', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (13, '/static/pic/1.png', '2025-02-12 19:13:43', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (14, '/static/pic/1.png', '2025-02-12 22:35:37', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (15, '/static/pic/1.png', '2025-02-12 22:54:57', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (16, '/static/pic/1.png', '2025-02-12 23:21:50', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (17, '/static/pic/1.png', '2025-02-14 00:32:47', 0, 10);
INSERT INTO `banner` (`id`, `picture_url`, `created_time`, `deleted`, `admin_id`) VALUES (18, '/static/pic/1.png', '2025-02-14 02:01:14', 0, 10);
COMMIT;

-- ----------------------------
-- Table structure for collect
-- ----------------------------
DROP TABLE IF EXISTS `collect`;
CREATE TABLE `collect` (
  `id` int NOT NULL,
  `from_id` int NOT NULL COMMENT '收藏的用户',
  `to_id` int NOT NULL COMMENT '被收藏的用户',
  `post_id` int NOT NULL COMMENT '被收藏的帖子',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of collect
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_id` int NOT NULL COMMENT '发起评论的用户的id',
  `post_id` int NOT NULL COMMENT '被评论的帖子的id',
  `to_id` int NOT NULL COMMENT '被评论的用户的id',
  `comment` varchar(255) NOT NULL,
  `read` int NOT NULL DEFAULT '0' COMMENT '0 未读 1 已读',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of comment
-- ----------------------------
BEGIN;
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`) VALUES (1, 1, 3, 2, 'dd', 0, '2025-02-17 15:40:25');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`) VALUES (2, 3, 3, 2, '可以小刀吗', 0, '2025-02-17 15:40:36');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`) VALUES (3, 1, 6, 3, 'dd', 0, '2025-02-17 16:19:11');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`) VALUES (4, 0, 6, 0, '私聊', 0, '2025-02-17 16:19:20');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`) VALUES (5, 0, 1, 0, '可以少点吗', 0, '2025-02-17 16:19:32');
COMMIT;

-- ----------------------------
-- Table structure for like
-- ----------------------------
DROP TABLE IF EXISTS `like`;
CREATE TABLE `like` (
  `id` int NOT NULL,
  `from_id` int NOT NULL COMMENT '点赞的用户',
  `to_id` int NOT NULL COMMENT '被点赞的用户',
  `post_id` int NOT NULL COMMENT '被点赞的帖子',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of like
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_id` int NOT NULL COMMENT '留言用户id',
  `to_id` int NOT NULL COMMENT '被留言用户id',
  `text` varchar(255) DEFAULT NULL COMMENT '留言内容',
  `read` int NOT NULL DEFAULT '0' COMMENT '0/1 未读/已读',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of message
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `publisher_id` int NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `details` varchar(255) NOT NULL,
  `views` int unsigned DEFAULT '0',
  `likes` int unsigned DEFAULT '0' COMMENT '点赞量',
  `category` varchar(255) NOT NULL DEFAULT 'other',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `delete_time` timestamp NULL DEFAULT NULL,
  `stars` int DEFAULT '0' COMMENT '收藏',
  `comments` int DEFAULT '0' COMMENT '评论数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of post
-- ----------------------------
BEGIN;
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (1, 2, '出二手投影仪', '100镑不刀', 107, 0, 'sublet', '2025-02-12 17:18:53', NULL, 0, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (3, 3, '出西景studio', '格拉斯哥West View（西景）公寓Gold studio出短租，因为本人圣诞要回国，该公寓位于格拉斯哥大学附近，楼下就有Lidl和morrison，还有partick火车站和地铁站，交通非常方便，该studio26.2平很大的studio，位于1楼，相当于国内的2楼，电器调味品锅碗瓢盆一切可以免费用，空气炸锅，炖汤的砂锅都有，免费用，租金原价350pw，打包一个月只要700\n', 62, 0, 'other', '2025-02-12 17:34:43', NULL, 0, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (6, 3, '出刚开封老抽', '1镑自取', 103, 13, 'sublet', '2025-02-14 13:37:18', NULL, 20, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (16, 1, '出95新iPhone 15', '600胖，格拉市中心和学校附近可送货', 1, 0, 'used', '2025-02-18 00:57:22', NULL, 0, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (17, 1, '便宜出switch', '两年前英国购入，使用频率不高，140镑出，送塞尔达', 5, 0, 'used', '2025-02-18 01:02:34', NULL, 0, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (21, 1, '出佳能ccd', 'IXUS 55', 11, 0, 'Used', '2025-02-18 12:15:15', NULL, 0, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (22, 1, '出北面登山包', '50镑自提', 2, 0, 'Used', '2025-02-18 12:54:21', NULL, 0, 0);
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`) VALUES (26, 1, '出jbl音响', '50镑 G4自提', 2, 0, 'Used', '2025-02-18 15:43:07', NULL, 0, 0);
COMMIT;

-- ----------------------------
-- Table structure for post_pic
-- ----------------------------
DROP TABLE IF EXISTS `post_pic`;
CREATE TABLE `post_pic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `post_id` int NOT NULL COMMENT '帖子的id',
  `photo_url` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '照片的id',
  `order` int DEFAULT NULL COMMENT '帖子里的第几张照片',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `pics-post` (`post_id`),
  CONSTRAINT `pics-post` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of post_pic
-- ----------------------------
BEGIN;
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (3, 6, 'https://img1.wushang.com/pn/wsec-img1/2023/8/30/e01001b5-37ae-44f5-b9c2-957ef253acd7.jpg?x-oss-process=image/resize,w_800,h_800', 1, '2025-02-14 13:37:18');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (4, 6, 'https://th.bing.com/th/id/OIP._t1viDQ5CiZhU4RNEvNLiQHaHa?rs=1&pid=ImgDetMain', 2, '2025-02-14 13:37:18');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (7, 3, 'https://th.bing.com/th/id/R.7614d9e40b232f41aeceef5a095fa5d0?rik=uqVr%2bPNJFSMRPA&pid=ImgRaw&r=0', 1, '2025-02-16 04:47:08');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (9, 3, 'https://www.hallbookers.co.uk/cache/upload/properties/1122/Silver_Studio_West_View-1000x666.jpg', 2, '2025-02-17 16:12:03');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (12, 16, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/apple-iphone-15-pro-7.avif', NULL, '2025-02-18 00:57:23');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (13, 17, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/OIP.jpeg', NULL, '2025-02-18 01:02:35');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (14, 17, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/OIP (1).jpeg', NULL, '2025-02-18 01:02:36');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (19, 21, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 12.14.06.png', NULL, '2025-02-18 12:15:18');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (20, 21, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 12.14.14.png', NULL, '2025-02-18 12:15:20');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (21, 22, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 12.53.28.png', NULL, '2025-02-18 12:54:22');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (22, 22, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 12.53.41.png', NULL, '2025-02-18 12:54:25');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (23, 26, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 15.39.47.png', NULL, '2025-02-18 15:43:09');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (24, 26, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 15.39.39.png', NULL, '2025-02-18 15:43:11');
COMMIT;

-- ----------------------------
-- Table structure for uploaded_file
-- ----------------------------
DROP TABLE IF EXISTS `uploaded_file`;
CREATE TABLE `uploaded_file` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uploaded_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `file` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of uploaded_file
-- ----------------------------
BEGIN;
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (1, '2025-02-17 00:58:22', 'uploads/截屏2025-01-25_00_crj3ycn.58.47.png');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (2, '2025-02-17 01:01:02', 'uploads/1.py');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (3, '2025-02-17 01:05:12', 'uploads/1_Hifhs6J.py');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (4, '2025-02-17 01:08:27', 'uploads/1_5CjN0JA.py');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (5, '2025-02-17 01:12:07', 'uploads/1_ylNlU82.py');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (6, '2025-02-17 01:13:58', 'uploads/1_mSa5HgE.py');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (7, '2025-02-17 01:19:37', 'uploads/1_rjJn0lA.py');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (8, '2025-02-17 01:27:27', 'uploads/P1113919.JPG');
INSERT INTO `uploaded_file` (`id`, `uploaded_at`, `file`) VALUES (9, '2025-02-17 01:28:36', 'uploads/P1113919_ARu8H38.JPG');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT 'user' COMMENT '角色',
  `register_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `level` int DEFAULT '0' COMMENT '等级',
  `avatar` varchar(255) DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` (`id`, `username`, `password`, `role`, `register_time`, `level`, `avatar`) VALUES (1, 'Sean', '123456', 'user', '0000-00-00 00:00:00', 0, NULL);
INSERT INTO `user` (`id`, `username`, `password`, `role`, `register_time`, `level`, `avatar`) VALUES (2, 'Amy', '123456', 'user', '2025-02-12 17:33:39', 0, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
