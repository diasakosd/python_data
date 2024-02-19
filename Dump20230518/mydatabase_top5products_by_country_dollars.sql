-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `top5products_by_country_dollars`
--

DROP TABLE IF EXISTS `top5products_by_country_dollars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `top5products_by_country_dollars` (
  `Product` varchar(255) NOT NULL,
  `Value` bigint DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `top5products_by_country_dollars`
--

LOCK TABLES `top5products_by_country_dollars` WRITE;
/*!40000 ALTER TABLE `top5products_by_country_dollars` DISABLE KEYS */;
INSERT INTO `top5products_by_country_dollars` VALUES ('All-countries',NULL,1),('All-1',1603472000000,2),('Non-food manufactured goods',403154000000,3),('Milk powder, butter, and cheese-1',98757000000,4),('Mechanical machinery and equip',57567000000,5),('Meat and edible offal-1',51206000000,6),('Australia',NULL,7),('All-2',107686000000,8),('China',NULL,9),('All-3',182406000000,10),('Milk powder, butter, and cheese-2',31216000000,11),('Logs, wood, and wood articles',17993000000,12),('Electrical machinery and equip',16478000000,13),('Meat and edible offal-2',15463000000,14),('East Asia (excluding China)',NULL,15),('All-4',89245000000,16),('Milk powder, butter, and cheese-3',27311000000,17),('European Union (27)',NULL,18),('All-5',26644000000,19),('Japan',NULL,20),('All-6',23155000000,21),('Total (excluding China)',NULL,22),('All-7',291991000000,23),('United Kingdom',NULL,24),('All-8',21591000000,25),('United States',NULL,26),('All-9',40477000000,27),('Meat and edible offal-3',11843000000,28);
/*!40000 ALTER TABLE `top5products_by_country_dollars` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-18 13:50:12
