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

-- Дамп структуры для таблица prohormitrich.updates
CREATE TABLE IF NOT EXISTS `updates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Дамп данных таблицы prohormitrich.updates: ~4 rows (приблизительно)
/*!40000 ALTER TABLE `updates` DISABLE KEYS */;
INSERT INTO `updates` (`id`, `text`) VALUES
	(1, '<b>Обновление 0.1</b>\r\n\r\n- Добавлена команда просмотра команд - <i>/help</i>.\r\n- Добавлена команда просмотра личной статистики - <i>/mystats</i>.\r\n- Добавлена команда просмотра статистики чата - <i>/stats</i>.\r\n- Добавлен счётчик сообщений, голосовых сообщений, видео, аудио, фото, документов, стикеров и видео сообщений.\r\n- Добавлено подключение к базе данных.\r\n- Добавлено подключение к боту.'),
	(2, '<b>Обновление 0.1.1</b>\r\n\r\n- Исправлена ошибка при выводе статистики с нулевым днём регистрации чата/участника.'),
	(3, '<b>Обновление 0.2</b>\r\n\r\n- Добавлена команда с просмотром рейтинга 10 пользователей по количеству сообщений - <i>/top</i>.\r\n- Добавлена команда с просмотром последних 5-ти обновлений бота - <i>/updates</i>.'),
	(4, '<b>Обновление 0.3</b>\r\n\r\n- Добавлена поддержка разметки текста.\r\n- Добавлена загрузка текста для команды <i>/help</i> из базы данных.'),
  (5, '<b>Обновление 0.3.1</b>\r\n\r\n- Исправлено корректное отображение среднего количества сообщений.');
/*!40000 ALTER TABLE `updates` ENABLE KEYS */;

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

-- Дамп структуры для таблица prohormitrich.help
CREATE TABLE IF NOT EXISTS `help` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Дамп данных таблицы prohormitrich.help: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `help` DISABLE KEYS */;
INSERT INTO `help` (`id`, `text`) VALUES
	(1, '<i>/stats</i> - просмотр статистики чата.'),
	(2, '<i>/mystats</i> - просмотр личной статистики в чате.'),
	(3, '<i>/updates</i> - просмотр последних обновлений бота.'),
	(4, '<i>/top</i> - рейтинг участников чата.');
/*!40000 ALTER TABLE `help` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;