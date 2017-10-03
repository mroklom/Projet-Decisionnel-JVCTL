CREATE DATABASE  IF NOT EXISTS `jvctl-dataset-1` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `jvctl-dataset-1`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: jvctl-dataset-1
-- ------------------------------------------------------
-- Server version	5.7.15-log

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
-- Table structure for table `trees`
--

DROP TABLE IF EXISTS `trees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trees` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `addr_sect` int(10) unsigned NOT NULL COMMENT 'Sector identifier.',
  `seeding_year` int(10) unsigned NOT NULL,
  `diagnosis_year` int(10) unsigned NOT NULL COMMENT 'Year when the tree was diagnosed.',
  `next_diagnosis_year` int(10) unsigned DEFAULT NULL COMMENT 'Preconised year for the next diagnosis.',
  `code` varchar(45) NOT NULL COMMENT 'Tree identifier.',
  `parent_code` varchar(45) NOT NULL COMMENT 'Station identifier.',
  `parent_code_desc` varchar(255) NOT NULL COMMENT 'Location of the station.',
  `stump_diameter` varchar(45) NOT NULL,
  `species` varchar(255) NOT NULL COMMENT 'Tree species.',
  `busyness` varchar(255) NOT NULL COMMENT 'Passage near the tree.',
  `botanical_type` varchar(45) NOT NULL COMMENT 'Botanical type of the tree.',
  `plu_id` int(11) DEFAULT NULL COMMENT 'Local town plan identifier.',
  `plu_category_label` varchar(45) DEFAULT NULL COMMENT 'Local town plan category label.',
  `diagnosis_note` varchar(255) DEFAULT NULL COMMENT 'Result of the diagnosis.',
  `renewal_priority` varchar(45) DEFAULT NULL COMMENT 'Renewal priority for the tree.',
  `seeding_purpose` varchar(45) DEFAULT NULL COMMENT 'Why this tree was planted.',
  `remarks` varchar(255) DEFAULT NULL COMMENT 'Remarks about the tree.',
  `subcategory_code` varchar(45) DEFAULT NULL COMMENT 'Code of the subcategory.',
  `subcategory_desc` varchar(255) DEFAULT NULL COMMENT 'Description of the subcategory',
  `development_status` varchar(45) DEFAULT NULL COMMENT 'Current status of the tree''s development.',
  `development_status_when_diagnosed` varchar(45) DEFAULT NULL COMMENT 'Developement status of the tree when it was diagnosed. A tree is young until it''s 10 years old.',
  `caterpillar_treatment` varchar(45) DEFAULT NULL COMMENT 'How this tree was treated for caterpillars.',
  `recommanded_action_diagnosis` varchar(45) DEFAULT NULL COMMENT 'The recommanded action for the tree after the diagnosis.',
  `sidewalk_proximity` tinyint(1) DEFAULT NULL COMMENT 'Defines whether the tree is near a sidewalk.',
  `seeding_type` varchar(45) DEFAULT NULL COMMENT 'How the tree was planted.',
  `variety` varchar(45) DEFAULT NULL COMMENT 'The variety of the tree.',
  `vigor` varchar(45) DEFAULT NULL COMMENT 'The vigor of the tree.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_UNIQUE` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trees`
--

LOCK TABLES `trees` WRITE;
/*!40000 ALTER TABLE `trees` DISABLE KEYS */;
/*!40000 ALTER TABLE `trees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-22 11:41:24
