-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: prohormitrich
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
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
  `nicknameid` int DEFAULT NULL,
  `nicknamevisible` int NOT NULL DEFAULT '1',
  `edited_messages` int NOT NULL DEFAULT '0',
  `vodka_drinked` float NOT NULL DEFAULT '0',
  `vodka_timeout` bigint NOT NULL DEFAULT '0',
  `food_eated` bigint NOT NULL DEFAULT '0',
  `food_timeout` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  KEY `FK_users_chats` (`chatid`),
  KEY `nicknameid` (`nicknameid`),
  CONSTRAINT `FK_users_chats` FOREIGN KEY (`chatid`) REFERENCES `chats` (`id`) ON DELETE CASCADE,
  CONSTRAINT `FK_users_nicknames` FOREIGN KEY (`nicknameid`) REFERENCES `nicknames` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3 COMMENT='Таблица с информацией о пользователях';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `food_list`
--

DROP TABLE IF EXISTS `food_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `food` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `min_food_value` int NOT NULL,
  `max_food_value` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Таблица с едой';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_list`
--

LOCK TABLES `food_list` WRITE;
/*!40000 ALTER TABLE `food_list` DISABLE KEYS */;
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(1, '🍎', 5, 15);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(2, '🧄', -80, -20);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(3, '🧅', -80, -20);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(4, '🍋', 1, 10);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(5, '🍌', 5, 15);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(6, '🍉', 5, 20);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(7, '🍅', 5, 15);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(8, '🍆', 5, 20);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(9, '🍔', 10, 25);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(10, '🍕', 5, 20);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(11, '🥙', 20, 70);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(12, '🍡', 5, 15);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(13, '🍪', 10, 25);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(14, '🍭', 10, 25);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(15, '🍛', 20, 70);
INSERT INTO prohormitrich.food_list (id, food, min_food_value, max_food_value) VALUES(16, '🍜', 20, 70);
/*!40000 ALTER TABLE `food_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `help`
--

DROP TABLE IF EXISTS `help`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `help` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COMMENT='Таблица с тектом помощи';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `help`
--

LOCK TABLES `help` WRITE;
/*!40000 ALTER TABLE `help` DISABLE KEYS */;
INSERT INTO `help` VALUES (1,'<i>/stats</i> - просмотр статистики чата.'),(2,'<i>/mystats</i> - просмотр личной статистики в чате.'),(3,'<i>/updates</i> - просмотр последних обновлений бота.'),(4,'<i>/top</i> - рейтинг участников чата.'),(5,'<i>/nick</i> - управление внутренним никнеймом в чате.'),(6,'<i>/all</i> - упоминание всех участников чата.'),(7,'<i>/anek</i> - случайный анекдот.'),(8,'<i>/settings</i> - настройки чата.'),(9,'<i>/vodka</i> - выпить водки.'),(10,'<i>/eat</i> - пополнить сытость.');
/*!40000 ALTER TABLE `help` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nicknames`
--

DROP TABLE IF EXISTS `nicknames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nicknames` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=471 DEFAULT CHARSET=utf8mb3 COMMENT='Таблица с никнеймами';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nicknames`
--

LOCK TABLES `nicknames` WRITE;
/*!40000 ALTER TABLE `nicknames` DISABLE KEYS */;
INSERT INTO `nicknames` VALUES (294,'\" Чо-по кличке волОс \"'),(114,'\"Убиваю принцесс, спасаю драконов\"'),(1,'$KYpidar'),(59,'( .) ( .)'),(110,'**IIIpyc[bI] HA rOLOBe**'),(7,'*О*Д*У*В*А*Н*Ч*И*К*'),(167,'.оО Мышка-стрептизёрша Оо.'),(87,'/7eXaPb TBOEu MAMKu'),(214,'0CEMEH1TEJIb 6a6yJIek ?'),(307,'0ssTraSI Ko4erbI}|{kA'),(461,'100gramoВИЧ'),(437,'100pudoff'),(67,'175см55кг19лет (она)'),(184,'3JIbIe ТеFteLi'),(416,'6a6ka Иa {Х}odylЯx'),(469,'9 6erу TAkou a BoJIocbI Ha3ad'),(317,'90-60-90 (он)'),(157,'90x60x90'),(243,'<Заяц, Боевой, Ушастый>'),(15,'<ИСЧАДИЕ РАЯ> или <ИСЧАДИЕ АДА>'),(155,'?Кошак'),(78,'Apple_Ѽ_Xrym'),(382,'BECe^JIbIu^ KOHb'),(274,'BepHuTe CaMoKaT ?'),(177,'BoЗbMy B РoT 3a 6yTEP6poT'),(324,'CaHuTaP Tya/eToB'),(297,'CbIpOCTb_oT_HoCkA'),(16,'cheLentano'),(318,'DeaD_MaKcNm'),(444,'Dj хлопушка'),(53,'Do hyia delov analnbI’ zud'),(279,'Dobriy Govnodaw'),(293,'donkyHOT'),(10,'EasyHUIsy'),(205,'EcJLu CEKCA B }|{u3Hu HET, CgEJLau CAM Ce6E MuHeT ?'),(378,'Global Silver Elit™'),(240,'GoJIoVa DoMa 谷'),(137,'Head$hoTuku 0T AwoTuka'),(134,'HeHacto9wuu’ Mapkeloff'),(211,'hotelkin'),(341,'Hugo_borz'),(97,'I am Batmen'),(143,'in100gramm'),(212,'Kiss Ме в|слепую'),(118,'KurWa*'),(91,'Kuшe4нo-Пoлoвoй Tpaкт'),(335,'Loading… ██████████████] 99%'),(408,'LoL'),(102,'Lol_for_all'),(11,'lopata'),(121,'MC.Додик'),(323,'MePTBbIu_CJIoHuK'),(94,'molodoy_i_pianbIi'),(322,'Mo}{natbIe SI’LLa'),(122,'Mr.Epic'),(90,'MYDAK'),(64,'MyZHik B JIo$iNAX'),(120,'OLOLO-OLOLO-Ya-BoditeLb-NLO'),(109,'oTMorozsko'),(426,'p*zda tebe'),(100,'Passu za Adminky'),(464,'Ra$PizDAY'),(316,'reach beach'),(290,'SAHARWHORES'),(425,'sexy 6aTaH'),(388,'SkuZoppO'),(343,'Sosok-Admina'),(397,'spinogryz'),(68,'SvYt@yA_]{aRtOsHkA'),(185,'S| ybil эtor0 4yВаkа'),(5,'TaeKwonDo'),(73,'TAMBOVS WOLF'),(48,'Tampax Inside – обладателем является лицо мужского пола)'),(440,'TaPo4oK'),(436,'terroristka и fsbshnica'),(40,'Tor4oK'),(265,'TPAXMECTEP'),(236,'TvoSI Mamka'),(140,'Xa-Xa-Crazy-Xa-Xa'),(443,'Y0ur_Bunny_Wr0te (твой зайчик написал)'),(80,'Ya y mamki Dyra4oK ?'),(125,'Ya_B0G_A_Tb)_Lo}{'),(376,'Youdontknowwhoiam'),(223,'Your perdAk is under AttAck'),(163,'ZadNizza'),(325,'[!_m0kal v b0kal_!]'),(364,'[X]odok 3anuB0M'),(178,'[Х]o4y B kJIaH Ho 9 E6JIaH'),(195,']Mr.Сексуальность['),(190,'^_^::п0каж1 CиCечкi::^_^'),(160,'_А жИзНь ЧуМаАа_'),(24,'_от_А(да)_до_(ра)Я_'),(37,'{X}o4y kak PR0™ moGy kak DNO'),(346,'|Pi_Pi|'),(124,'|’|uCe4Ka'),(158,'}{a|{eR_MaZaFa|{eR'),(269,'}{олодный Πонос'),(210,'}|{o/7a_4eIIIeTc9'),(452,'ΠΘΔΖΣΜΚΛ'),(179,'А вот и ЙА'),(315,'Абу хазми буль-буль Пятар'),(200,'Агрессивное дно'),(139,'Али Ибн Абдул Обстул Задом Бей'),(431,'Алло ето АТС'),(394,'Ангел-предохранитель'),(30,'Атцкий киви'),(34,'афлЁный кирпич'),(446,'БАБА С ВОЗУ'),(225,'БаБа_В_КеДАхХх'),(332,'БАБАЙКА'),(231,'бауди на ауди'),(285,'без трусиков'),(311,'белка-хотелка'),(82,'Белый нигер'),(261,'БеШаНаЯ НоГа'),(194,'Блoха в Сарафане'),(389,'Блоха в скафандре'),(266,'Блоха в униформе'),(154,'БОМЖ'),(273,'Бомж с рублёвки или Рублёвский Бомж'),(89,'Бронетемкин Поносецъ'),(206,'Бублик'),(271,'Бугагашенька'),(355,'Бухое печенюшко'),(309,'в клеточку'),(342,'ВААЩЕ ЧУМАВОЙ ДИНАЗАВР'),(22,'Ведро с глазами'),(337,'ведь_были_крылья'),(296,'Вежливый снайпер'),(164,'ВеЛиКиЙ КуКуРуЗкО'),(270,'веснушка'),(329,'Вечный ньюб!'),(312,'визуальный обман'),(219,'виртуальная сопля'),(161,'Влад доил жирафа'),(220,'Водаврот'),(58,'волк_в_овечей_шкуре'),(339,'волчья пися'),(88,'волшебная клизма'),(305,'Волшебные репетузы'),(251,'Вонючий Суслик переросток'),(181,'ВОРУЮ_МАМОК'),(60,'ВОРЮГА-АНАНЮГА'),(49,'врач-похметолог'),(369,'ВЫЛЫСЫПЫДЫСТ'),(54,'Вылысыпыдыстка'),(116,'Высоковольтный Майонез'),(228,'Г0рячий_туалетный_ЕршNк'),(283,'Гамадрила'),(308,'Гербалайф'),(175,'Гибрид оленя с человелом'),(180,'Глиста в скафандре'),(267,'гнойная палочка'),(287,'Гомик в Деревне'),(66,'Гордый птичка'),(357,'Гравицапа'),(238,'Грегуар на трахуаре'),(462,'Группа Крови'),(254,'Грустный такой Лосяра'),(441,'грязь из под ногтей'),(418,'Гусь Великий Воин'),(216,'Дачный душ Зеленовка'),(204,'Девственная извращенка'),(330,'Девственник всея Руси'),(26,'ДеВУшКи-ЦвЕтИтЕ,МУжЧиНы-НЕРаСпУСКаЙТеСь'),(239,'Девчонка без тормозов'),(348,'девчонка в наушниках'),(46,'девый пальчик'),(221,'Дед-отмороз'),(327,'Дед_Пыхто'),(123,'Дедуськина бабуська'),(289,'Дедушка-Западло'),(126,'ДЕРЕВОЛАЗ'),(253,'Дермонтиновый убийца'),(166,'Джафар с Востока'),(85,'Дибил - Пет докеби'),(353,'Димка вырви глаз'),(286,'добрый жук'),(127,'Доктор Зло - Аколит'),(451,'Домгагающаяся пандА'),(52,'Доместос_супер_грязь'),(9,'дося'),(360,'Дурочка-с-переулочка'),(379,'Дырка в голове'),(259,'Дюжина_ножей_в_спину_революции'),(229,'Дядя из министерства добрых дел'),(392,'енот импотЕнт'),(241,'Жжженя'),(262,'Жизнепоглатитель'),(457,'Жуткость Тормозная'),(442,'загорелая роза'),(103,'зачем_мне_ник'),(412,'Заяц Боевой Ушастый'),(41,'ЗелеБоба'),(14,'Злая тарелка'),(413,'зло_в_воплощении_ангела'),(153,'злобный бурбулятор'),(284,'Злой Гусь'),(27,'Злой димедрол'),(381,'Злой зелёный таракан'),(465,'Злыдень с карданом'),(282,'ЗОМби_КРОШИТ_П@Ц@нов'),(390,'Идеальная Оптимистка'),(435,'Интернет Бродилкин'),(65,'Интим не предлагать'),(217,'интимный прыщик'),(252,'Йа КреведКО'),(361,'Йожик_без_кое-чего'),(226,'Какаши Жмуруками'),(338,'Какуля'),(55,'Канализационный Крыс'),(277,'Капитан Джек Поскорей'),(45,'Карманный Блоходав'),(404,'касатик-М-16'),(407,'Кина не будет'),(399,'Клавиатура Мониторовна'),(61,'Клон из пробирки №13'),(183,'КОВАРНОЕ ЛАМО'),(207,'Ковбой Хагис'),(99,'колючая карамелька'),(193,'Конопляных Дел Мастер'),(258,'королЕва задрот'),(424,'кот дьявола'),(383,'Кот шашлык'),(63,'КоТэ С NoЖом'),(414,'Кошерный Доктор'),(202,'Кошка в вязаной шапке'),(450,'Кпсс-сс'),(62,'Краснопьяточный грядкоторчатель'),(385,'Краснопяточный грядкоторчатель'),(366,'Кривые Руки'),(56,'крик урагана'),(304,'Кровавое Утро'),(18,'Круглый в карты проигрался'),(292,'Крытый медным тазом'),(187,'кукла дождя'),(4,'Кура-с ИнтелеКтоМ'),(144,'кураГАЛЯ'),(320,'Куропеко'),(222,'Кусочек сыра с паштетом**'),(306,'ЛblсоКоHb'),(248,'Лекарь-Костоправ'),(468,'ЛеНиН ЖиВ'),(8,'Летучий Олень'),(384,'лишённая души'),(415,'Лохматая Волчица'),(168,'лучший из худших'),(141,'Лысый аптекарь'),(453,'ЛЮБАпытнаЯ.'),(395,'Любовница Смерти'),(93,'Любовница_Смерти'),(268,'Ляськи_Масяськи'),(303,'МаДаМ [Бруньки]'),(447,'Макрофлекс – убийца сикелей'),(298,'МАЛЬЧИК_И_ДЕВОЧКА.БУДЕШЬ_3им?'),(31,'МАЛЬЧИК_НА_САНКАХ'),(406,'марионетка листопада'),(186,'Марс атакует'),(280,'Матраскин'),(13,'Мертвая дельфинка'),(256,'Мертвый Котенок'),(445,'Минздрав'),(191,'МиСс НеПрИяТнОсТь'),(242,'Многокашиел'),(345,'Мозги в носке'),(230,'Монитор Клавиатурович'),(146,'морозоустойчивая дама'),(106,'Московская Колхозница'),(35,'Мстящий за Зайца'),(173,'Мы Взрывали Апельсин'),(349,'Мыха-наруха'),(336,'Накуренный Волшебник'),(301,'Не плюй против ветра-можешь промахнуться!!'),(234,'Не убивай лошадь'),(174,'Не_ежык_но_в_тумане'),(57,'НЕ_ТАБАК!'),(117,'Невеста ветра'),(142,'Неиграю в УО'),(132,'некропедозоофил'),(95,'Неопознанный Летающий Мужик'),(29,'Неуравновешанный хомяк убийца'),(129,'Ни разу не критовик!'),(430,'Нифиги ни фея - мой ник))'),(375,'НОСИЛЬНИК МАМОНТОВ'),(367,'НОЧНОЙ_ПОРТНОЙ'),(380,'Ночью под мостом и с топором'),(101,'Нудистка'),(32,'нухотьэтотникблянезанят'),(351,'Оближи_меня'),(347,'Обожённый_лунным_светоМ'),(84,'Окуеть дайте две'),(300,'омлетка+)'),(340,'ОпА$нЫй_ВоЗрА$т'),(172,'ОпАSнЫй ВоЗрАSт'),(401,'Оператор отбойного молотка'),(264,'Опухший заяц'),(334,'Осторожно Танк'),(368,'отдамся за 5 рублей'),(373,'ОчЕнЬ ЧуЖоЙ'),(288,'ОченьПриятно-Царь'),(276,'Очкастый мачо'),(165,'Пyk@N_в_огNe'),(115,'Па3итИФф'),(295,'Паганый_нини'),(148,'папа антилопы'),(19,'ПАСТУХ_МЕРТВЕЦОВ'),(69,'Паук_Шнюк'),(263,'Пендальф - Виз'),(410,'Пенкуздуй'),(86,'Перловая каша супер мутант'),(224,'Пернатый Перфоратор'),(272,'Персонаж заблокирован!'),(201,'Печень Сталина'),(39,'Пих Пах Убит Нах'),(371,'Пихал Михалыч'),(23,'ПлАсТеЛиН ОвЕц'),(354,'Пластун'),(170,'Пленник SexShop-а!'),(278,'Плюхай Яйцедубович'),(70,'Под испанским нЁбом'),(456,'Подметало'),(257,'Подружка безопасности'),(356,'Полнолуние'),(21,'Полулысое недоразумение'),(393,'Помыла Андерсон'),(470,'Последнее слово чебурашки'),(112,'Посмотри Направо'),(313,'Потолковый Лампонюх'),(359,'появилась из облака'),(133,'Приведение в кроссовках'),(159,'Призрак Ваньки Хоя'),(105,'принцесса дури'),(420,'ПРОЗРАЧНАЯ_РУБАШКА(ОНА)'),(6,'просто глюк'),(145,'простой парень с Рублёвки...'),(449,'протри монитор'),(113,'ПуЛи_От_ДеДуЛи'),(150,'пурген'),(130,'ПУТИН'),(427,'Пьяная Мартышка'),(463,'Пьяный дровосек'),(417,'Пять_недель_на_воздушном_шаре'),(423,'РАй тик'),(198,'Ромашка_Бегемотовна'),(387,'Рыбка с запошком'),(409,'рыло_кирпичем'),(344,'рыцарь круглова стала'),(197,'СoC ok'),(467,'САМ ТАКОЙ'),(209,'сам_себе_дед'),(314,'САМ_ТАКОЙ'),(44,'СвингДавалочка'),(377,'Свинья Пеппа'),(249,'сволочь в перчатках'),(391,'Святой Блинчик'),(135,'сексуальная козявка'),(362,'Сильвестр в столовой'),(321,'Сиреневый_Турбовыбулькиватель'),(147,'СкОлЬзКаЯ МоЧаЛкА'),(244,'Скупщик ресниц'),(17,'СЛЕГКА ОБДОЛБАНАЯ'),(363,'Следующая остановка – сердце.'),(189,'смерть админа'),(188,'смерть с косой'),(38,'СМЕТАНКА_ДЛЯ_КОТОВ'),(411,'снегурка_в_чулках'),(107,'Сочная ставка'),(213,'Сплюнахнетрогать'),(149,'СрульНафсех'),(386,'Сталин Арчер'),(374,'Сталин_каскадёр - =))'),(83,'Старики кактусы смерти'),(460,'Старый_панда'),(28,'Стёпикмен`'),(77,'Стон водопада'),(281,'страусятина'),(2,'Страшный симпатюга'),(232,'Страшный симпатяга'),(111,'стремнаЯ'),(439,'стремная гусеница'),(372,'стрЁмный физрук'),(12,'сумасшедший автобус'),(429,'супер-пупер падла'),(138,'Схватка 2 якодзун'),(196,'Сытый тролль'),(365,'тараканище_без_зубастое'),(398,'Тараканка'),(79,'Тарелочка Борщя'),(454,'Твоu’ МоX'),(405,'телаЧьи нежноСти'),(119,'Темный повелитель чебураторов'),(247,'То яма то канава - Монк'),(422,'Товарищ в гражданском'),(310,'Толпа узкоглазых Якудза'),(151,'Торговец плотью'),(458,'Тр@вокYр'),(352,'ТРАВА_НЕ_НАРКОТИК'),(36,'Трепанатор из Одессы'),(291,'Тролль из уборной'),(350,'Турбовозбудитель'),(459,'ТуФлЁй_По_ЯйЦаМ'),(182,'Тухлый Чучо'),(176,'Тэ'),(448,'ТэдЯ'),(428,'Тюленьвсяжопавракушках'),(192,'тяжелое пёрышко'),(434,'Убийца матрёшек'),(203,'Убийца пьяных бабочек'),(402,'УБИЦА ЛЮБИМЕЦ ЖЕНЬЩИН'),(233,'уборщик подвижного состава'),(218,'УбЬю ТаПкОм'),(227,'угон девушек за 60 секунд'),(98,'Унитазная элементаль'),(50,'урок с паяльником'),(215,'усы-лапы-хвост'),(169,'Утка_в_тапках'),(131,'Утро псового лая'),(72,'Фиолетовый Пук'),(432,'Фипилявая какаФка'),(358,'Фрекен Бог'),(433,'Фрося_Бурлакова'),(128,'ФСБ_постучись'),(245,'Фыбыдыжьдыжьбыдыжь'),(108,'ХАЛЯВА НА БАЗЕ'),(396,'хвост_мышки_майкрософт'),(403,'Хип-Хоп в Твоём Доме'),(104,'Хомяк с пастой бленд а мед'),(419,'Хотящий'),(331,'хранитель червя'),(199,'Хранительница чешки'),(246,'хрен в каске2'),(421,'Хренабубка'),(333,'Хрум-Хрумыч'),(42,'Хьуна ма хаза аватор карина...'),(171,'ЦойЖив'),(74,'Ч. У. М. А.'),(136,'ЧинГачГук Обвислое Перо'),(20,'Чихуахуёнышь – сын Чи-хуа-хуа'),(438,'Чудесный Хобот'),(299,'Чухонский культиватор'),(43,'Чучело-Мяучело'),(455,'Чьи трусы?'),(51,'шаловливая пиранья'),(235,'Шаман-наркоман'),(208,'шанс_года'),(81,'ШаУрМа МяУкАеТ'),(400,'Шиза -не приходит одна'),(47,'Шишколобый_Гнидодав'),(152,'Шо_тЫ_ВИЛУПIЛОСЬ??!'),(466,'Ща воткну этот меч в твой глаз'),(156,'ьькосмический калощьь'),(260,'Это Был Не Нескафе'),(25,'эхо унитазного бачка'),(370,'Юрец всем в торец'),(75,'Я вернулась из блока'),(326,'Я вернулся из блока'),(162,'Я королева,а вы простите кто?'),(237,'Я не ПРодАЮсь,Я саМа поКупАю'),(71,'я со снаиперкой'),(319,'я_не_трус_но_я_боюсь'),(3,'Яичница с беконом'),(92,'Янот_ЧеРеЗ*Я*'),(328,'Яростный кулак Джека'),(255,'Ятидренный Хряп'),(33,'Яубьютогоктосломалмойпробел'),(250,'٩(×̯×)۶ InoPLANetSInin ٩(×̯×)۶'),(76,'† КОЛХОЗНИК †'),(96,'€to ne to o 4em tbI podymal ㋛'),(302,'☞0tsosi ne trЯsi'),(275,'☠_ПИСЕВТbIКАТЕJI`_☠');
/*!40000 ALTER TABLE `nicknames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_settings`
--

DROP TABLE IF EXISTS `chat_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat_settings` (
  `chatid` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `show_anek_bg` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`chatid`),
  KEY `chat_settings_chatid_IDX` (`chatid`) USING BTREE,
  CONSTRAINT `chat_settings_FK` FOREIGN KEY (`chatid`) REFERENCES `chats` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='Таблица с внутренними настройками чатов';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `chats`
--

DROP TABLE IF EXISTS `chats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chats` (
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
  `edited_messages` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='Таблица с информацией о чатах';
/*!40101 SET character_set_client = @saved_cs_client */;

/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `chats_create` AFTER INSERT ON `chats` FOR EACH ROW begin 
	insert into 
		chat_settings
	set
		chat_settings.chatid = new.id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `updates`
--

DROP TABLE IF EXISTS `updates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `updates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(1024) NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3 COMMENT='Таблица с текстом обновлений';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `updates`
--

LOCK TABLES `updates` WRITE;
/*!40000 ALTER TABLE `updates` DISABLE KEYS */;
INSERT INTO `updates` VALUES (1,'<b>Обновление 0.1</b>\r\n\r\n- Добавлена команда просмотра команд - <i>/help</i>.\r\n- Добавлена команда просмотра личной статистики - <i>/mystats</i>.\r\n- Добавлена команда просмотра статистики чата - <i>/stats</i>.\r\n- Добавлен счётчик сообщений, голосовых сообщений, видео, аудио, фото, документов, стикеров и видео сообщений.\r\n- Добавлено подключение к базе данных.\r\n- Добавлено подключение к боту.','2022-01-05 21:00:00'),(2,'<b>Обновление 0.1.1</b>\r\n\r\n- Исправлена ошибка при выводе статистики с нулевым днём регистрации чата/участника.','2022-01-05 21:00:00'),(3,'<b>Обновление 0.2</b>\r\n\r\n- Добавлена команда с просмотром рейтинга 10 пользователей по количеству сообщений - <i>/top</i>.\r\n- Добавлена команда с просмотром последних 5-ти обновлений бота - <i>/updates</i>.','2022-01-06 21:00:00'),(4,'<b>Обновление 0.3</b>\r\n\r\n- Добавлена поддержка разметки текста.\r\n- Добавлена загрузка текста для команды <i>/help</i> из базы данных.','2022-01-06 21:00:00'),(5,'<b>Обновление 0.3.1</b>\r\n\r\n- Исправлено корректное отображение среднего количества сообщений.','2022-01-06 21:00:00'),(6,'<b>Обновление 0.3.2</b>\r\n\r\n- Бот отправляет бесшумные сообщения, не вызывая звук при упоминании участников чата.','2022-01-07 21:00:00'),(7,'<b>Обновление 0.4</b>\r\n\r\n- Добавлена команда для управления внутренним никнеймом в чате - <i>/nick</i>.\r\n- Добавлена команда для упоминания всех участников чата - <i>/all</i>','2022-01-31 21:00:00'),(8,'<b>Обновление 0.4.1</b>\r\n\r\n- Исправлено некорректное упоминание участников чата.','2022-01-31 21:00:00'),(9,'<b>Обновление 0.5</b>\r\n\r\n- Добавлена команда для вывода случайного анекдота - <i>/anek</i>.\r\n- Рефакторинг SQL запросов.','2022-08-29 21:00:00'),(10,'<b>Обновление 0.6</b>\r\n\r\n- Добавлена обработка и счётчик редактируемых сообщений.\r\n- Добавлена команда для управления внутренними настройками чата - <i>/settings</i>.\r\n- Добавлено управление отображением картинки в анекдотах (<i>/settings anekbg</i>).\r\n- Добавлено отображение даты обновления в команде <i>/updates</i>.\r\n- Исправлено неправильное отображение имён в команде <i>/all</i>.\r\n- Рефакторинг SQL запросов.','2023-02-09 10:44:56'),(11,'<b>Обновление 0.6.1</b>\r\n\r\n- Исправлена кодировка при использовании команды <i>/anek</i>.','2023-02-10 12:37:34'),(12,'<b>Обновление 0.6.2</b>\r\n\r\n- Исправлена команда <i>/all</i>.','2023-02-16 16:09:18'),(13,'<b>Обновление 0.7</b>\r\n\r\n- Добавлена команда <i>/vodka</i>\r\n- Добавлена команда <i>/eat</i>\r\n- Команда <i>/top</i> разделена на категории.\r\n- Добавлен топ по количеству выпитой водки (<i>/top_vodka</i>).\r\n- Добавлен топ по количеству сытости (<i>/top_eda</i>).','2023-02-23 23:08:02');
/*!40000 ALTER TABLE `updates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-24  2:24:24
