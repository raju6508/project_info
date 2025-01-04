-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: my_database
-- ------------------------------------------------------
-- Server version	8.0.31

--
-- Table structure for table `project_info`
--

DROP TABLE IF EXISTS `project_info`;

CREATE TABLE `project_info` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Project_Title` varchar(255) NOT NULL,
  `PartNumbers` varchar(255) DEFAULT NULL,
  `Proj_Status` varchar(255) DEFAULT NULL,
  `Action` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

