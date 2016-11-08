CREATE DATABASE  IF NOT EXISTS `info_tracker` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `info_tracker`;
-- MySQL dump 10.13  Distrib 5.6.13, for osx10.6 (i386)
--
-- Host: 127.0.0.1    Database: info_tracker
-- ------------------------------------------------------
-- Server version	5.6.20

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
-- Table structure for table `headline`
--

DROP TABLE IF EXISTS `headline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `headline` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(256) NOT NULL,
  `post_date` date DEFAULT NULL,
  `digest` varchar(256) DEFAULT NULL,
  `title` varchar(128) CHARACTER SET utf8mb4 NOT NULL,
  `score` int(11) NOT NULL,
  `website_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `headline_bb08ac1c` (`website_id`),
  CONSTRAINT `headline_website_id_7b74878c5f2b2d96_fk_website_id` FOREIGN KEY (`website_id`) REFERENCES `website` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `headline`
--

LOCK TABLES `headline` WRITE;
/*!40000 ALTER TABLE `headline` DISABLE KEYS */;
INSERT INTO `headline` VALUES (1,'https://news.ycombinator.com/item?id=12417290',NULL,NULL,'An account of a serious medical emergency on a transoceanic flig789',789,1),(2,'https://news.ycombinator.com/item?id=12421687',NULL,NULL,'How to Tell a Mother Her Child Is Dead',574,1),(3,'https://news.ycombinator.com/item?id=12420763',NULL,NULL,'500 Byte Images: The Haiku Vector Icon Format',232,1),(4,'https://news.ycombinator.com/item?id=12422891',NULL,NULL,'FLAC Support in Firefox 51',216,1),(5,'https://news.ycombinator.com/item?id=12420147',NULL,NULL,'People in Los Angeles Are Getting Rid Of Their Cars',209,1),(6,'https://news.ycombinator.com/item?id=12423331',NULL,NULL,'Skypeopensource2 – Skype client based on reversing Skype 5.5',191,1),(7,'https://news.ycombinator.com/item?id=12422124',NULL,NULL,'“We have been experiencing a catastrophic DDoS attack”',171,1),(8,'https://news.ycombinator.com/item?id=12422378',NULL,NULL,'A Fighter Pilot’s Guide to Surviving on the Roads (2012) [pdf]',167,1),(9,'https://news.ycombinator.com/item?id=12423371',NULL,NULL,'Richard Stallman: Online Publishers Should Let Readers Pay Anony161',161,1),(10,'https://news.ycombinator.com/item?id=12420811',NULL,NULL,'The neurology of self-awareness',159,1),(11,'https://www.reddit.com/r/programming/comments/5134ur/fresh_ide_v230_has_been_released/',NULL,NULL,'Fresh IDE v2.3.0 has been released.',99,8),(12,'https://www.reddit.com/r/programming/comments/510lti/i_made_a_network_graph_of_programming_languages/',NULL,NULL,'I made a network graph of programming languages and compilers',104,8),(13,'https://www.reddit.com/r/programming/comments/50zpin/so_you_want_to_be_a_functional_programmer_part_1/',NULL,NULL,'So You Want to be a Functional Programmer (Part 1)',98,8),(15,'https://www.reddit.com/r/programming/comments/510jgh/results_of_the_2016_nim_community_survey/',NULL,NULL,'Results of the 2016 Nim Community Survey',90,8),(16,'https://www.reddit.com/r/programming/comments/511i0j/pep_530_asynchronous_comprehensions/',NULL,NULL,'PEP 530 -- Asynchronous Comprehensions',87,8),(17,'https://www.reddit.com/r/programming/comments/513l8b/gambas_390_is_out_gambas_is_a_free_development/',NULL,NULL,'Gambas 3.9.0 is out! Gambas is a free development environment an49',49,8),(18,'https://www.reddit.com/r/programming/comments/50zh0c/spirv_compression/',NULL,NULL,'SPIR-V Compression',36,8),(19,'https://www.reddit.com/r/programming/comments/51049h/this_website_is_basically_amp_html/',NULL,NULL,'This Website is Basically AMP HTML',38,8),(20,'https://www.reddit.com/r/programming/comments/5127hj/apicombo_api_testing_and_monitoring_in_the/',NULL,NULL,'APICombo - API Testing and Monitoring in the easiest way',8,8),(21,'https://medium.com/p/i-got-scammed-by-a-silicon-valley-startup-574ced8acdff',NULL,NULL,'I Got Scammed By A Silicon Valley Startup',5439,5),(22,'https://medium.com/p/a-verdade-sobre-bel-pesce-82c706e16b4a',NULL,NULL,'A verdade sobre Bel Pesce',584,5),(23,'https://medium.com/p/cognitive-bias-cheat-sheet-55a472476b18',NULL,NULL,'Cognitive bias cheat sheet',1139,5),(24,'https://medium.com/p/why-i-am-giving-up-teaching-bc3ec2071c80',NULL,NULL,'Why I Am Giving Up Teaching',354,5),(25,'https://medium.com/p/how-not-to-bomb-your-offer-negotiation-c46bb9bc7dea',NULL,NULL,'How not to bomb your offer negotiation',358,5),(26,'https://medium.com/p/8-ways-billionaires-and-elite-athletes-perform-at-the-highest-level-cd7f97082f5e',NULL,NULL,'8 Ways Billionaires and Elite Athletes Perform at the Highest Le524',524,5),(27,'https://medium.com/p/how-i-used-abused-my-tesla-what-a-tesla-looks-like-after-100-000-miles-a-48-state-road-trip-6b6ae66b3c10',NULL,NULL,'How I Used & Abused My Tesla — What a Tesla looks like after 102938',2938,5),(28,'https://medium.com/p/7-productivity-apps-that-shave-10-hours-off-your-work-week-634604304763',NULL,NULL,'7 Productivity Apps That Shave 10 Hours Off Your Work Week',553,5),(29,'https://medium.com/p/0-to-640m-non-obvious-lessons-learned-at-brightroll-b6b3eb4086ac',NULL,NULL,'0 to $640M: Non-obvious Lessons Learned at BrightRoll',500,5),(30,'https://medium.com/p/how-to-read-to-learn-and-exercise-your-brain-df8310785239',NULL,NULL,'How to read to learn and exercise your brain',561,5),(31,'https://www.producthunt.com/tech/letsventure-2',NULL,NULL,'LetsVenture: Discover &amp; invest in startups',119,2),(32,'https://www.producthunt.com/tech/stocky',NULL,NULL,'Stocky: Free photo, video, graphics &amp; music for commercial u70',70,2),(33,'https://www.producthunt.com/tech/jayc-audio',NULL,NULL,'JAYC.audio: Youtube converter, simple, fast &amp; ad-free',44,2),(34,'https://www.producthunt.com/tech/burfi-2-0',NULL,NULL,'Burfi 2.0: A simplest way to take notes without leaving your bro35',35,2),(35,'https://www.producthunt.com/tech/people-ai',NULL,NULL,'people.ai: Know what your sales team is up to',37,2),(36,'https://www.producthunt.com/podcasts/hello-tech-pros-interview-players-for-your-d-d-campaign',NULL,NULL,'Hello Tech Pros: Interview Players For Your D&amp;D Campaign: By3',3,2),(37,'https://www.producthunt.com/tech/hotkey',NULL,NULL,'Hotkey: Simple yet powerful lists with a keyboard only interface23',23,2),(38,'https://www.producthunt.com/tech/get-moving',NULL,NULL,'Get Moving: The app that motivates you to sit less and stand mor20',20,2),(39,'https://www.producthunt.com/tech/racefully',NULL,NULL,'Racefully: Run with friends wherever they are!',23,2),(40,'https://www.producthunt.com/tech/timezoner',NULL,NULL,'Timezoner: Time zone calculator bot for Slack',2,2),(41,'https://github.com/ElemeFE/element',NULL,NULL,'ElemeFE/element: Desktop UI elements for Vue.js 2.0',201,4),(42,'https://github.com/tmrts/go-patterns',NULL,NULL,'tmrts/go-patterns: A curated list of Go patterns and idioms',200,4),(43,'https://github.com/facebook/zstd',NULL,NULL,'facebook/zstd: Zstandard - Fast real-time compression algorithm',168,4),(44,'https://github.com/xcatliu/mobi.css',NULL,NULL,'xcatliu/mobi.css: A lightweight, flexible css framework that foc152',152,4),(45,'https://github.com/david-gpu/srez',NULL,NULL,'david-gpu/srez: Image super-resolution through deep learning',138,4),(46,'https://github.com/heynickc/awesome-ddd',NULL,NULL,'heynickc/awesome-ddd: A curated list of Domain-Driven Design (DD138',138,4),(47,'https://github.com/gridcontrol/gridcontrol',NULL,NULL,'gridcontrol/gridcontrol: Networked Process Manager to execute fu131',131,4),(48,'https://github.com/waud/waud',NULL,NULL,'waud/waud: Web Audio Library',122,4),(49,'https://github.com/brillout/awesome-react-components',NULL,NULL,'brillout/awesome-react-components: Catalog of React components /116',116,4),(50,'https://github.com/VctrySam/whatsapp',NULL,NULL,'VctrySam/whatsapp: WhatsApp in React Native',113,4);
/*!40000 ALTER TABLE `headline` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-07 17:58:41
