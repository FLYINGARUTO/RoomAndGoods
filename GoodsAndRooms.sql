/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80402
 Source Host           : localhost:3306
 Source Schema         : GoodsAndRooms

 Target Server Type    : MySQL
 Target Server Version : 80402
 File Encoding         : 65001

 Date: 24/02/2025 23:11:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_id` int DEFAULT NULL COMMENT '发起评论的用户的id',
  `post_id` int NOT NULL COMMENT '被评论的帖子的id',
  `to_id` int NOT NULL COMMENT '被评论的用户的id',
  `comment` varchar(255) NOT NULL,
  `read` int NOT NULL DEFAULT '0' COMMENT '0 未读 1 已读',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `from_user` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comment-post` (`post_id`),
  CONSTRAINT `comment-post` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of comment
-- ----------------------------
BEGIN;
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`, `from_user`) VALUES (20, NULL, 30, 1, '保养过几次', 0, '2025-02-24 22:56:39', 'Sean');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`, `from_user`) VALUES (21, NULL, 32, 1, '还在吗 想短租', 0, '2025-02-24 22:57:35', 'Sean');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`, `from_user`) VALUES (22, NULL, 1, 1, '还在吗', 0, '2025-02-24 22:58:08', 'Sean');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`, `from_user`) VALUES (23, NULL, 42, 1, '我想去', 0, '2025-02-24 22:59:51', 'Rachel');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`, `from_user`) VALUES (24, NULL, 21, 1, '还在吗请问', 0, '2025-02-24 23:00:05', 'Rachel');
INSERT INTO `comment` (`id`, `from_id`, `post_id`, `to_id`, `comment`, `read`, `create_time`, `from_user`) VALUES (25, NULL, 43, 1, '我这里有3b2b的次卧出租', 0, '2025-02-24 23:00:44', 'Rachel');
COMMIT;

-- ----------------------------
-- Table structure for like
-- ----------------------------
DROP TABLE IF EXISTS `like`;
CREATE TABLE `like` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from_user` varchar(255) NOT NULL COMMENT '点赞的用户',
  `to_id` int NOT NULL COMMENT '被点赞的用户',
  `post_id` int NOT NULL COMMENT '被点赞的帖子',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `only like once` (`from_user`,`post_id`),
  KEY `link to post` (`post_id`),
  CONSTRAINT `link to post` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of like
-- ----------------------------
BEGIN;
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (17, 'Sean', 1, 3, '2025-02-24 22:20:40');
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (19, 'Sean', 1, 42, '2025-02-24 22:25:41');
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (22, 'Sean', 1, 30, '2025-02-24 22:39:12');
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (23, 'Sean', 1, 1, '2025-02-24 22:58:06');
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (24, 'Rachel', 1, 21, '2025-02-24 23:00:08');
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (25, 'Rachel', 1, 43, '2025-02-24 23:00:48');
INSERT INTO `like` (`id`, `from_user`, `to_id`, `post_id`, `created_time`) VALUES (26, 'Sean', 1, 21, '2025-02-24 23:01:16');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of message
-- ----------------------------
BEGIN;
INSERT INTO `message` (`id`, `from_id`, `to_id`, `text`, `read`, `created_time`) VALUES (1, 2, 3, 'sadjba', 0, '2025-02-19 23:17:52');
INSERT INTO `message` (`id`, `from_id`, `to_id`, `text`, `read`, `created_time`) VALUES (2, 1, 3, '123', 0, '2025-02-19 23:25:11');
INSERT INTO `message` (`id`, `from_id`, `to_id`, `text`, `read`, `created_time`) VALUES (3, 1, 1, 'dd', 0, '2025-02-20 00:33:55');
INSERT INTO `message` (`id`, `from_id`, `to_id`, `text`, `read`, `created_time`) VALUES (4, 1, 1, 'hello', 0, '2025-02-23 16:13:31');
INSERT INTO `message` (`id`, `from_id`, `to_id`, `text`, `read`, `created_time`) VALUES (5, 1, 2, 'asddsa', 0, '2025-02-23 18:55:53');
COMMIT;

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `publisher_id` int DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `details` varchar(255) NOT NULL,
  `views` int unsigned DEFAULT '0',
  `likes` int unsigned DEFAULT '0' COMMENT '点赞量',
  `category` varchar(255) NOT NULL DEFAULT 'other',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `delete_time` timestamp NULL DEFAULT NULL,
  `stars` int DEFAULT '0' COMMENT '收藏',
  `comments` int DEFAULT '0' COMMENT '评论数',
  `publisher` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of post
-- ----------------------------
BEGIN;
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (1, 1, '出二手投影仪', '100镑不刀', 169, 1, 'Used', '2025-02-12 17:18:53', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (3, 1, '出西景studio', '格拉斯哥West View（西景）公寓Gold studio出短租，因为本人圣诞要回国，该公寓位于格拉斯哥大学附近，楼下就有Lidl和morrison，还有partick火车站和地铁站，交通非常方便，该studio26.2平很大的studio，位于1楼，相当于国内的2楼，电器调味品锅碗瓢盆一切可以免费用，空气炸锅，炖汤的砂锅都有，免费用，租金原价350pw，打包一个月只要700\n', 69, 1, 'Other', '2025-02-12 17:34:43', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (6, 1, '出刚开封老抽', '1镑自取', 237, 0, 'Used', '2025-02-14 13:37:18', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (16, 1, '出95新iPhone 15', '600胖，格拉市中心和学校附近可送货', 3, 0, 'Used', '2025-02-18 00:57:22', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (17, 1, '便宜出switch', '两年前英国购入，使用频率不高，140镑出，送塞尔达', 6, 0, 'Used', '2025-02-18 01:02:34', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (21, 1, '出佳能ccd', 'IXUS 55', 24, 2, 'Used', '2025-02-18 12:15:15', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (22, 1, '出北面登山包', '50镑自提', 4, 0, 'Used', '2025-02-18 12:54:21', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (26, 1, '出jbl音响', '50镑 G4自提', 4, 0, 'Used', '2025-02-18 15:43:07', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (27, 1, '出山寨劳力士', 'learning hub面交', 4, 0, 'Used', '2025-02-19 14:12:15', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (28, 1, '周六求跑腿', '有偿', 3, 0, 'Other', '2025-02-19 14:21:14', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (29, 1, '出荷花', '60rmb一包', 21, 0, 'Used', '2025-02-23 13:21:45', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (30, 1, '出14年mini cooper', '可试车', 5, 1, 'Used', '2025-02-23 13:25:55', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (31, 1, '出市中心社会公寓', '主卧 700p一个月', 0, 0, 'Sublet', '2025-02-23 13:29:08', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (32, 1, '出西村studio', '官方合同', 2, 0, 'Sublet', '2025-02-23 14:29:04', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (35, 1, '周末找伦敦搭子', '3-5天', 0, 0, 'Other', '2025-02-23 14:36:56', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (42, 1, 'who wants to travel to Edinburgh', 'tomorrow', 81, 1, 'Other', '2025-02-23 15:29:14', NULL, 0, 0, 'Sean');
INSERT INTO `post` (`id`, `publisher_id`, `title`, `details`, `views`, `likes`, `category`, `create_time`, `delete_time`, `stars`, `comments`, `publisher`) VALUES (43, 1, '求市中心社会公寓房源', '600per month以内可以接受', 3, 1, 'Sublet', '2025-02-23 20:38:00', NULL, 0, 0, 'Sean');
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3;

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
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (25, 27, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 12.13.06.png', NULL, '2025-02-19 14:12:18');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (26, 27, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-18 12.13.19.png', NULL, '2025-02-19 14:12:20');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (27, 28, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-16 03.27.40.png', NULL, '2025-02-19 14:21:15');
INSERT INTO `post_pic` (`id`, `post_id`, `photo_url`, `order`, `created_time`) VALUES (28, 43, 'https://my-it-bucket-glasgow.s3.eu-north-1.amazonaws.com/uploads/截屏2025-02-23 20.37.44.png', NULL, '2025-02-23 20:38:03');
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
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
