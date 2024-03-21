-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: dimasapp
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exercises`
--

DROP TABLE IF EXISTS `exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercises` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `approach` int NOT NULL,
  `time` int NOT NULL,
  `repetition` int NOT NULL,
  `totalTime` int NOT NULL,
  `videoLink` varchar(255) NOT NULL,
  `workoutId` int DEFAULT NULL,
  `level` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `workoutId` (`workoutId`),
  CONSTRAINT `exercises_ibfk_1` FOREIGN KEY (`workoutId`) REFERENCES `workouts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises`
--

LOCK TABLES `exercises` WRITE;
/*!40000 ALTER TABLE `exercises` DISABLE KEYS */;
INSERT INTO `exercises` VALUES ('00783073-3e72-411e-a7f5-fccb50f72ad8','Wall Training for Passing and Receiving',3,25,5,125,'videos/570d3d9c-a04c-4105-80f4-988bcedf3f12.mp4',37,3),('05290d97-3efd-46e9-9a44-983dced30d8d','Complete Soccer Drills',3,20,20,400,'videos/704f4da0-92e2-4667-b71e-f91ba02598bb.mp4',43,3),('0fa7c3d5-cb4e-4767-8c7a-997f13396d24','Figure 8 Drill',3,10,15,75,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',38,3),('0ffbb049-5798-42af-9bfc-d23f30859b38','Ball Mastery in Small Spaces',1,15,8,120,'videos/570d3d9c-a04c-4105-80f4-988bcedf3f12.mp4',37,2),('1d3c6449-dc70-49b8-bcd2-c6f7f3336c32','Basic Passing and Receiving',1,10,10,100,'videos/704f4da0-92e2-4667-b71e-f91ba02598bb.mp4',43,1),('26ce2c2c-89ae-4c91-968c-774b74a1f4f8','Shooting Practice',2,15,10,150,'videos/93400e40-f731-4ec0-aa3f-06ab4f8a5237.mp4',34,2),('30b8c93c-5db5-4a4a-98d6-e454665d3434','Advanced Ball Handling Skills',3,20,6,120,'videos/947a1942-416d-429c-a0c0-4c8d78f8dd08.mp4',41,3),('3112d4c5-f108-4117-8969-0c7272a1a7e9','Dribbling Drills',1,15,15,225,'videos/963bde02-f6bc-462c-9016-58173a3256b6.mp4',42,2),('34bfd5f9-8d05-46e5-8b20-12b8afd98e9a','Basic Dribbling Fundamentals',1,10,10,100,'videos/963bde02-f6bc-462c-9016-58173a3256b6.mp4',42,1),('37ce864e-c23d-450b-bdf6-d39f1f302a3b','10 Minute Ball Mastery',1,10,10,100,'videos/947a1942-416d-429c-a0c0-4c8d78f8dd08.mp4',41,1),('39c06c27-b471-497a-a18b-7d2085797d31','Two Touch Passing',1,10,10,80,'videos/15abd4b0-7928-48c3-8463-12178c7bd1e3.mp4',44,2),('3aeca424-91d0-49ef-8608-c016a1704d3c','1v1 to Goal',1,10,15,120,'videos/15abd4b0-7928-48c3-8463-12178c7bd1e3.mp4',44,3),('489bc555-1fab-46e5-8d54-3d3653d31521','Precision Figure 8 Drill',2,15,30,70,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',39,3),('525770b9-1b1f-4d77-a809-9e638b8b4bc9','Intermediate Ball Control',2,15,12,180,'videos/704f4da0-92e2-4667-b71e-f91ba02598bb.mp4',43,2),('6084f423-c5ad-46a6-8083-3606fa93857b','Advanced Agility Drills',3,12,12,144,'videos/78934220-b663-4bf8-a95f-09007d0c016e.mp4',45,3),('611f1405-f3fd-4501-90da-08d0165a487e','Soccer Footwork Drills',1,10,10,100,'videos/4231166b-e211-4e66-9ca7-78e9a79b2572.mp4',47,2),('643c32d4-7e20-4212-a410-b6ada4ada971','Intensive Ball Mastery',2,15,20,50,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',39,2),('64afb8a3-98de-4975-bbaf-f0763d24be00','Elite Ball Mastery',1,20,30,35,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',40,2),('76b0ca3c-3a6c-4d70-986b-f1c74952c594','Soccer Footwork Drills',1,10,10,100,'videos/4231166b-e211-4e66-9ca7-78e9a79b2572.mp4',47,1),('8b80d84f-3ed0-4512-9b61-a97855d4f831','Close Control Dribbling Session',3,20,30,480,'videos/1db3d676-fb59-43bd-91f6-01cbc8415d60.mp4',46,3),('90de7829-da9b-4cd7-a1f1-d7a0bf37c4be','Fast Feet Drills',2,10,10,100,'videos/78934220-b663-4bf8-a95f-09007d0c016e.mp4',45,2),('95bb0611-f3ca-4313-b05b-b9b568335ffa','Soccer Footwork Drills',1,10,10,100,'videos/4231166b-e211-4e66-9ca7-78e9a79b2572.mp4',47,3),('99bcb011-84ca-4ccc-acb7-814faa1f258e','Trapezoid Passing Pattern',1,10,5,50,'videos/15abd4b0-7928-48c3-8463-12178c7bd1e3.mp4',44,1),('9b8ca93d-00ba-4e90-82bc-23e49ab15753','Ball Mastery Basics',3,10,10,50,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',38,2),('9fb89b5c-5307-473e-9cdd-1172d25672d1','Solo Touch Improvement',1,15,5,75,'videos/7bb35891-c612-493b-8c23-dae5e9372df6.mp4',36,1),('a5276633-2719-46d7-bfca-8d01207ca5fb','Advanced Dribbling',3,10,15,150,'videos/93400e40-f731-4ec0-aa3f-06ab4f8a5237.mp4',34,3),('a6067ea4-4a7c-4583-b372-d2e6e3bf6e16','Solo Dribbling Drills',2,20,4,80,'videos/7bb35891-c612-493b-8c23-dae5e9372df6.mp4',36,2),('a8a1529c-fbb1-4ea0-ab53-2abc0f8646a6','Juggling for Touch Improvement',1,10,10,100,'videos/570d3d9c-a04c-4105-80f4-988bcedf3f12.mp4',37,1),('a8b47f29-a157-4d0d-b2ed-2d550b253cbc','Touch Training Solo',1,25,5,125,'videos/3a9ae104-dbe9-43b1-968b-776b86f287b9.mp4',35,1),('aeca1829-bc77-44ad-b5d6-d957f5eb6b75','Pro Wall Training for Precision',1,20,15,20,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',40,3),('b619497a-b56d-485d-99f2-8b705a37d688','Juggling Fundamentals',3,10,5,30,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',38,1),('c6b1ee97-ee84-48fc-8aea-29ab5f48dd8f','Intermediate Ball Control Drills',2,15,8,120,'videos/947a1942-416d-429c-a0c0-4c8d78f8dd08.mp4',41,2),('c9434834-80f7-4d79-a0aa-3f83369fa0fd','Advanced Dribbling Techniques',3,20,10,200,'videos/963bde02-f6bc-462c-9016-58173a3256b6.mp4',42,3),('d2bf9174-bbe7-4ffc-a9b8-d73acddbb3dd','Essential Dribbling Drills',3,15,15,225,'videos/1ee9a017-e3a8-4590-b21c-8b3fed4488e3.mp4',46,1),('d841ed0c-ed57-44fd-ba2d-68f692b0ff61','Advanced Juggling Techniques',2,15,10,30,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',39,1),('d8cf3362-830b-44f1-be77-fbc9233629cd','Close Control Dribbling Session',3,20,20,400,'videos/1db3d676-fb59-43bd-91f6-01cbc8415d60.mp4',46,2),('d93dafc5-d1ef-43a2-b0de-88eb25418df0','Passing Drills Solo',2,20,10,200,'videos/3a9ae104-dbe9-43b1-968b-776b86f287b9.mp4',35,2),('e1ef3144-fd8b-4284-8a00-3b2b3050be34','Solo Shooting Techniques',3,15,15,225,'videos/3a9ae104-dbe9-43b1-968b-776b86f287b9.mp4',35,3),('e7d4040d-99dc-4ada-8536-b5439213f207','Passing and Shooting Alone',3,25,3,75,'videos/7bb35891-c612-493b-8c23-dae5e9372df6.mp4',36,3),('ea393c5c-c6dd-4e55-8903-7591e99288f2','Expert Figure 8 Drill',1,20,45,55,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',40,3),('f425421b-cae0-4e8f-af05-9d6139d9763e','Beginner Footwork Drills',1,10,8,80,'videos/78934220-b663-4bf8-a95f-09007d0c016e.mp4',45,1),('fc19499f-ac1a-4b0d-8e41-acdae9108c2e','Essential Football Drills',1,20,5,100,'videos/93400e40-f731-4ec0-aa3f-06ab4f8a5237.mp4',34,1),('fc67d6f0-17a1-49a1-ae6d-c7626e4ebd6d','Professional Juggling Mastery',1,20,15,20,'videos/732eb07a-9778-4f6f-8b39-1bce0f5428be.mp4',40,1);
/*!40000 ALTER TABLE `exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `level` int NOT NULL,
  `goal` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2ad1bbcc-2d77-47c2-8018-0b9a4df87c1e','',2,NULL),('58f7fe6a-a4ba-44f8-9d75-0144fe47b5db','',2,NULL),('be646499-e934-4489-a361-364e89d5ea6a','test token',0,NULL),('c380180002faa4b5b8aa99a6542893dba.0.srxvy.iAx0CfG777k07xgfbAushg','cE6nEmfSuEFMtw7i-n0_gg:APA91bHskscCHgNNrMqeN_EmaQK2Sji1LZKPEyI7d1ObSAXAzwAp6_GkfXyxVqQX7sO8Hrkd8nHLJAUyjND5a_rCj-0eKsyL0IrVZPOISOuM-5bK5AjU6neeDurySqkpWBSC9NzC-m8t',0,1),('c5ec5e470116c48a8b5fdcdd4be30e15b.0.srszt.EjWxcUMZ_VkrMmBU9Y_rmw','',2,NULL),('c9ef6cdc7d02e45c0847fce982ef7f88c.0.srszt.Uegv8J3KCjqMN19Dl-8K8A','token 88',0,NULL),('ca2e6d055d30c4f01b341a4b709765df0.0.srszt.SN8s6es3L-yAsTCVn0Q3RA','',2,NULL),('ccc46199474f84624bc83cab0dcd24bdf.0.srszt.HLn2AsPV9H9OgFN-0Vl3BA','cfXqxqTq4EGfj66oVNLhYu:APA91bFH-TSfL2umOgBEQmpb4wlGy8zn0tMC5P-eO_Gv3jZdOkzIBgrzpgfpezB3es6-c8YS066pmlEQgKDe97N_HNVify0FKp6eKxTJdl_zvDcSFMEmmjeKUhBr6LOElFWXEjWeEkf-',2,NULL),('cf076df9244ef43ac8b0c4be07ab44566.0.rruzw.NE99tXOfSPuOpLcwWQ_E-g','',0,NULL),('codeStrin2g','c6_6IKTAB0D-gwxmbzgM7e:APA91bHbMBvkzU1f2TZqA65kpTgvEO7xc2SAWfniwfPr_lmftOa8hIPR_hadb2vpkKtcfzzJOKixYC875lwx1RXQijCvGSMxQH4cu0wkYnpUuwx4pS59TIRkPiDIjjVN23TgWTz0px_u',1,NULL),('codeString','c6_6IKTAB0D-gwxmbzgM7e:APA91bHbMBvkzU1f2TZqA65kpTgvEO7xc2SAWfniwfPr_lmftOa8hIPR_hadb2vpkKtcfzzJOKixYC875lwx1RXQijCvGSMxQH4cu0wkYnpUuwx4pS59TIRkPiDIjjVN23TgWTz0px_u',2,NULL),('dfsf444','dgJ_bRJ5G0tHtJAso4_dal:APA91bFO8G0FQVOTxgADL1jJDanJWwZRi9zetdjQiR4jYL4pRhO8i8AcdqWtIMTP7tCZCYSlD1NUrpgfvjp34xVjYjQZcBQV3xdAYALq9LTGTsg30JqJ7F4NAshaUZtUIoqRpGLVzKWn',1,1),('e68316d0-8df8-46bc-82e9-99a85e19f0d9','string',0,NULL),('ee7a9531-b893-462b-8122-03f364549d20','',2,NULL),('string','string',0,NULL),('string1231212321331231231233','string',0,10),('string1231231231231233','string',0,NULL),('test111','token 88',0,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workout_history`
--

DROP TABLE IF EXISTS `workout_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workout_history` (
  `history_id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `completion_date` datetime NOT NULL,
  `workout_details` text NOT NULL,
  `workout_id` int NOT NULL,
  PRIMARY KEY (`history_id`),
  KEY `user_id` (`user_id`),
  KEY `workout_id` (`workout_id`),
  CONSTRAINT `workout_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `workout_history_ibfk_2` FOREIGN KEY (`workout_id`) REFERENCES `workouts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workout_history`
--

LOCK TABLES `workout_history` WRITE;
/*!40000 ALTER TABLE `workout_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `workout_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workouts`
--

DROP TABLE IF EXISTS `workouts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workouts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `level` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workouts`
--

LOCK TABLES `workouts` WRITE;
/*!40000 ALTER TABLE `workouts` DISABLE KEYS */;
INSERT INTO `workouts` VALUES (34,'2024-03-22 09:00:00','Football Skills Training',1),(35,'2024-03-22 10:00:00','Solo Training Session',1),(36,'2024-03-22 11:00:00','Solo Football Skills Training',1),(37,'2024-03-22 14:00:00','Indoor Soccer Skills Training',1),(38,'2024-03-22 15:00:00','Indoor Soccer Skills',1),(39,'2024-03-22 16:00:00','Indoor Soccer Skills',2),(40,'2024-03-22 17:00:00','Indoor Soccer Skills',3),(41,'2024-03-23 08:00:00','Ball Mastery Training',1),(42,'2024-03-23 09:00:00','Dribbling Improvement',2),(43,'2024-03-23 12:00:00','Comprehensive Soccer Skills',3),(44,'2024-03-23 13:00:00','Professional Football Training',1),(45,'2024-03-23 18:00:00','Footwork Improvement',2),(46,'2024-03-23 19:00:00','Dribbling Mastery',3),(47,'2024-03-23 20:00:00','Soccer Footwork Routine',1);
/*!40000 ALTER TABLE `workouts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-21 11:09:26
