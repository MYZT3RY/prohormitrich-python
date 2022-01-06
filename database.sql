-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               8.0.19 - MySQL Community Server - GPL
-- Операционная система:         Win64
-- HeidiSQL Версия:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Дамп структуры базы данных prohormitrich
CREATE DATABASE IF NOT EXISTS `prohormitrich` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `prohormitrich`;

-- Дамп структуры для таблица prohormitrich.chats
CREATE TABLE IF NOT EXISTS `chats` (
  `id` varchar(64) NOT NULL DEFAULT '',
  `messages` int NOT NULL DEFAULT '0',
  `dateofregister` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `voices` int NOT NULL DEFAULT '0',
  `videos` int NOT NULL DEFAULT '0',
  `audios` int NOT NULL DEFAULT '0',
  `photos` int NOT NULL DEFAULT '0',
  `documents` int NOT NULL DEFAULT '0',
  `stickers` int NOT NULL DEFAULT '0',
  `videovoices` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.

-- Дамп структуры для таблица prohormitrich.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(64) NOT NULL,
  `username` varchar(24) NOT NULL,
  `chatid` varchar(64) NOT NULL,
  `messages` int NOT NULL DEFAULT '0',
  `dateofregister` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `voices` int NOT NULL DEFAULT '0',
  `videos` int NOT NULL DEFAULT '0',
  `audios` int NOT NULL DEFAULT '0',
  `photos` int NOT NULL DEFAULT '0',
  `documents` int NOT NULL DEFAULT '0',
  `stickers` int NOT NULL DEFAULT '0',
  `videovoices` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  KEY `FK_users_chats` (`chatid`),
  CONSTRAINT `FK_users_chats` FOREIGN KEY (`chatid`) REFERENCES `chats` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Экспортируемые данные не выделены.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
