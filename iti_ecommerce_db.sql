-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: iti_ecommerce_db
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add profile',7,'add_profile'),(26,'Can change profile',7,'change_profile'),(27,'Can delete profile',7,'delete_profile'),(28,'Can view profile',7,'view_profile'),(29,'Can add wishlist',8,'add_wishlist'),(30,'Can change wishlist',8,'change_wishlist'),(31,'Can delete wishlist',8,'delete_wishlist'),(32,'Can view wishlist',8,'view_wishlist'),(33,'Can add wishlist_ item',9,'add_wishlist_item'),(34,'Can change wishlist_ item',9,'change_wishlist_item'),(35,'Can delete wishlist_ item',9,'delete_wishlist_item'),(36,'Can view wishlist_ item',9,'view_wishlist_item'),(37,'Can add category',10,'add_category'),(38,'Can change category',10,'change_category'),(39,'Can delete category',10,'delete_category'),(40,'Can view category',10,'view_category'),(41,'Can add cart',11,'add_cart'),(42,'Can change cart',11,'change_cart'),(43,'Can delete cart',11,'delete_cart'),(44,'Can view cart',11,'view_cart'),(45,'Can add cart item',12,'add_cartitem'),(46,'Can change cart item',12,'change_cartitem'),(47,'Can delete cart item',12,'delete_cartitem'),(48,'Can view cart item',12,'view_cartitem'),(49,'Can add product',13,'add_product'),(50,'Can change product',13,'change_product'),(51,'Can delete product',13,'delete_product'),(52,'Can view product',13,'view_product'),(53,'Can add category',14,'add_category'),(54,'Can change category',14,'change_category'),(55,'Can delete category',14,'delete_category'),(56,'Can view category',14,'view_category'),(57,'Can add product',15,'add_product'),(58,'Can change product',15,'change_product'),(59,'Can delete product',15,'delete_product'),(60,'Can view product',15,'view_product'),(61,'Can add order',16,'add_order'),(62,'Can change order',16,'change_order'),(63,'Can delete order',16,'delete_order'),(64,'Can view order',16,'view_order'),(65,'Can add order item',17,'add_orderitem'),(66,'Can change order item',17,'change_orderitem'),(67,'Can delete order item',17,'delete_orderitem'),(68,'Can view order item',17,'view_orderitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_category`
--

DROP TABLE IF EXISTS `category_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_category`
--

LOCK TABLES `category_category` WRITE;
/*!40000 ALTER TABLE `category_category` DISABLE KEYS */;
INSERT INTO `category_category` VALUES (1,'Fashion','Fashion related products'),(2,'Electronics','Electronics related products'),(3,'Books','Books of various genres and topics'),(5,'Home Appliances','This category includes various home appliances'),(6,'Sports Equipment','This category includes sports-related items and equipment');
/*!40000 ALTER TABLE `category_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(10,'category','category'),(4,'contenttypes','contenttype'),(16,'order','order'),(17,'order','orderitem'),(13,'product','product'),(14,'productByCat','category'),(15,'productByCat','product'),(5,'sessions','session'),(11,'shopping_cart','cart'),(12,'shopping_cart','cartitem'),(7,'user','profile'),(6,'user','user'),(8,'wishlist','wishlist'),(9,'wishlist','wishlist_item');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-08 06:46:53.928897'),(2,'contenttypes','0002_remove_content_type_name','2024-04-08 06:46:54.009848'),(3,'auth','0001_initial','2024-04-08 06:46:54.331989'),(4,'auth','0002_alter_permission_name_max_length','2024-04-08 06:46:54.402799'),(5,'auth','0003_alter_user_email_max_length','2024-04-08 06:46:54.408810'),(6,'auth','0004_alter_user_username_opts','2024-04-08 06:46:54.414768'),(7,'auth','0005_alter_user_last_login_null','2024-04-08 06:46:54.422748'),(8,'auth','0006_require_contenttypes_0002','2024-04-08 06:46:54.425738'),(9,'auth','0007_alter_validators_add_error_messages','2024-04-08 06:46:54.433720'),(10,'auth','0008_alter_user_username_max_length','2024-04-08 06:46:54.439733'),(11,'auth','0009_alter_user_last_name_max_length','2024-04-08 06:46:54.445718'),(12,'auth','0010_alter_group_name_max_length','2024-04-08 06:46:54.461681'),(13,'auth','0011_update_proxy_permissions','2024-04-08 06:46:54.469622'),(14,'auth','0012_alter_user_first_name_max_length','2024-04-08 06:46:54.476602'),(15,'user','0001_initial','2024-04-08 06:46:54.901997'),(16,'admin','0001_initial','2024-04-08 06:46:55.057626'),(17,'admin','0002_logentry_remove_auto_add','2024-04-08 06:46:55.065604'),(18,'admin','0003_logentry_add_action_flag_choices','2024-04-08 06:46:55.077574'),(19,'category','0001_initial','2024-04-08 06:46:55.097520'),(20,'product','0001_initial','2024-04-08 06:46:55.121455'),(21,'product','0002_product_category','2024-04-08 06:48:12.534309'),(22,'sessions','0001_initial','2024-04-08 06:48:12.573206'),(23,'shopping_cart','0001_initial','2024-04-08 06:48:12.780717'),(24,'user','0002_remove_profile_type','2024-04-08 06:48:12.806847'),(25,'user','0003_alter_profile_image','2024-04-08 06:48:12.817686'),(26,'user','0004_profile_email_profile_phone_alter_profile_full_name','2024-04-08 06:48:13.109905'),(27,'wishlist','0001_initial','2024-04-08 06:48:13.195682'),(28,'wishlist','0002_wishlist_item_wishlist_products','2024-04-08 06:48:13.334121'),(29,'productByCat','0001_initial','2024-04-08 09:53:37.205037'),(30,'order','0001_initial','2024-04-09 04:55:47.517277'),(31,'order','0002_orderitem','2024-04-09 04:55:47.681874'),(32,'order','0003_order_created_at_order_shipping_address_order_status_and_more','2024-04-09 04:55:48.166692'),(33,'order','0004_alter_order_user','2024-04-09 04:55:48.179688'),(34,'order','0005_alter_order_user_alter_orderitem_product','2024-04-09 04:55:48.416027'),(35,'order','0006_alter_orderitem_product','2024-04-09 04:55:48.685305');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order`
--

DROP TABLE IF EXISTS `order_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) DEFAULT NULL,
  `shipping_address_id` bigint DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_order_shipping_address_id_57e64931_fk_user_profile_id` (`shipping_address_id`),
  KEY `order_order_user_id_7cf9bc2b_fk_user_user_id` (`user_id`),
  CONSTRAINT `order_order_shipping_address_id_57e64931_fk_user_profile_id` FOREIGN KEY (`shipping_address_id`) REFERENCES `user_profile` (`id`),
  CONSTRAINT `order_order_user_id_7cf9bc2b_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order`
--

LOCK TABLES `order_order` WRITE;
/*!40000 ALTER TABLE `order_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_orderitem`
--

DROP TABLE IF EXISTS `order_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `price` decimal(10,2) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_orderitem_order_id_aba34f44_fk_order_order_id` (`order_id`),
  KEY `order_orderitem_product_id_c5c6b07a_fk_product_product_id` (`product_id`),
  CONSTRAINT `order_orderitem_order_id_aba34f44_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`),
  CONSTRAINT `order_orderitem_product_id_c5c6b07a_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product_product` (`id`),
  CONSTRAINT `order_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_orderitem`
--

LOCK TABLES `order_orderitem` WRITE;
/*!40000 ALTER TABLE `order_orderitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_product`
--

DROP TABLE IF EXISTS `product_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `rating` double NOT NULL,
  `quantity` int NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_product_category_id_0c725779_fk_category_category_id` (`category_id`),
  CONSTRAINT `product_product_category_id_0c725779_fk_category_category_id` FOREIGN KEY (`category_id`) REFERENCES `category_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_product`
--

LOCK TABLES `product_product` WRITE;
/*!40000 ALTER TABLE `product_product` DISABLE KEYS */;
INSERT INTO `product_product` VALUES (1,'T-Shirt','A stylish t-shirt','product_images/Tshirt.jpg',19.99,4.5,50,1),(2,'Smartphone','A high-performance smartphone','product_images/smartphone.jpg',399.99,4.7,100,2),(3,'Laptop','A powerful laptop for productivity','product_images/laptop.jpg',999.99,4.6,50,2),(4,'Headphones','High-quality headphones for immersive audio experience','product_images/headphones.jpg',79.99,4.3,100,2),(5,'Mystery Novel','An intriguing mystery novel','product_images/mystery_novel_image.jpg',19.99,2.5,9,3),(6,'Science Fiction Book','An imaginative science fiction book','product_images/science_fiction_image.jpg',24.99,3,12,3),(7,'Jeans','Classic denim jeans for everyday wear','product_images/jeans.jpeg',39.99,4,35,1),(9,'Hoodie','A warm and cozy hoodie for chilly days','product_images/hoodie_image.jpg',49.99,4.3,20,1),(10,'Dress Shirt','A stylish dress shirt for formal occasions','product_images/dress_shirt_image.jpg',59.99,4.5,30,1),(11,'Sneakers','Comfortable and trendy sneakers for everyday wear','product_images/sneakers_image.jpg',79.99,4.2,40,1),(12,'Skirt','A fashionable skirt for casual or formal wear','product_images/skirt_image.jpg',39.99,4,25,1),(13,'Jacket','A stylish jacket for layering in colder weather','product_images/jacket_image.jpg',89.99,4.7,15,1),(14,'Coffee Maker','A programmable coffee maker for brewing your favorite beverages','product_images/coffee_maker_image.jpg',79.99,4.4,25,5),(15,'Toaster Oven','A versatile toaster oven for toasting, baking, and broiling','product_images/toaster_oven_image.jpg',99.99,4.2,20,5),(16,'Robot Vacuum Cleaner','An intelligent robot vacuum cleaner for automated cleaning','product_images/robot_vacuum_image.jpg',199.99,4.6,15,5),(17,'Air Fryer','A compact air fryer for healthier frying with less oil','product_images/air_fryer_image.jpg',129.99,4.3,20,5),(18,'Blender','A powerful blender for making smoothies, soups, and sauces','product_images/blender_image.jpg',69.99,4.5,30,5),(19,'Yoga Mat','A high-quality yoga mat for practicing yoga and other floor exercises','product_images/yoga_mat_image.jpg',29.99,4.7,50,6),(20,'Dumbbell Set','A set of adjustable dumbbells for strength training at home','product_images/dumbbell_set_image.jpg',99.99,4.6,30,6),(21,'Tennis Racket','A professional-grade tennis racket for players of all levels','product_images/tennis_racket_image.jpg',89.99,4.5,20,6),(22,'Basketball','A durable basketball for outdoor and indoor play','product_images/basketball_image.jpg',24.99,4.4,40,6),(23,'Running Shoes','High-performance running shoes for jogging and long-distance running','product_images/running_shoes_image.jpg',79.99,4.8,25,6);
/*!40000 ALTER TABLE `product_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productbycat_category`
--

DROP TABLE IF EXISTS `productbycat_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productbycat_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productbycat_category`
--

LOCK TABLES `productbycat_category` WRITE;
/*!40000 ALTER TABLE `productbycat_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `productbycat_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productbycat_product`
--

DROP TABLE IF EXISTS `productbycat_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productbycat_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `productByCat_product_category_id_a7d5267e_fk_productBy` (`category_id`),
  CONSTRAINT `productByCat_product_category_id_a7d5267e_fk_productBy` FOREIGN KEY (`category_id`) REFERENCES `productbycat_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productbycat_product`
--

LOCK TABLES `productbycat_product` WRITE;
/*!40000 ALTER TABLE `productbycat_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `productbycat_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_cart_cart`
--

DROP TABLE IF EXISTS `shopping_cart_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_cart_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `shopping_cart_cart_user_id_2bf33d14_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_cart_cart`
--

LOCK TABLES `shopping_cart_cart` WRITE;
/*!40000 ALTER TABLE `shopping_cart_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `shopping_cart_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_cart_cartitem`
--

DROP TABLE IF EXISTS `shopping_cart_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_cart_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `cart_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shopping_cart_cartitem_cart_id_adaf8330_fk_shopping_cart_cart_id` (`cart_id`),
  KEY `shopping_cart_cartitem_product_id_327be483_fk_product_product_id` (`product_id`),
  CONSTRAINT `shopping_cart_cartitem_cart_id_adaf8330_fk_shopping_cart_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `shopping_cart_cart` (`id`),
  CONSTRAINT `shopping_cart_cartitem_product_id_327be483_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_cart_cartitem`
--

LOCK TABLES `shopping_cart_cartitem` WRITE;
/*!40000 ALTER TABLE `shopping_cart_cartitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `shopping_cart_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `full_name` varchar(500) DEFAULT NULL,
  `about` longtext,
  `gender` varchar(500) DEFAULT NULL,
  `country` varchar(1000) DEFAULT NULL,
  `city` varchar(500) DEFAULT NULL,
  `state` varchar(500) DEFAULT NULL,
  `address` varchar(1000) DEFAULT NULL,
  `date` datetime(6) DEFAULT NULL,
  `pid` varchar(20) NOT NULL,
  `user_id` bigint NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pid` (`pid`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `user_profile_user_id_8fdce8e2_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--

LOCK TABLES `user_profile` WRITE;
/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user`
--

DROP TABLE IF EXISTS `user_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `full_name` varchar(500) DEFAULT NULL,
  `phone` varchar(500) NOT NULL,
  `otp` varchar(1000) DEFAULT NULL,
  `reset_token` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_groups`
--

DROP TABLE IF EXISTS `user_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_groups_user_id_group_id_bb60391f_uniq` (`user_id`,`group_id`),
  KEY `user_user_groups_group_id_c57f13c0_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_user_groups_group_id_c57f13c0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_user_groups_user_id_13f9a20d_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_groups`
--

LOCK TABLES `user_user_groups` WRITE;
/*!40000 ALTER TABLE `user_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_user_permissions`
--

DROP TABLE IF EXISTS `user_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq` (`user_id`,`permission_id`),
  KEY `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_user_user_permissions_user_id_31782f58_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_user_permissions`
--

LOCK TABLES `user_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlist_wishlist`
--

DROP TABLE IF EXISTS `wishlist_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist_wishlist` (
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `wishlist_wishlist_user_id_13f28b16_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist_wishlist`
--

LOCK TABLES `wishlist_wishlist` WRITE;
/*!40000 ALTER TABLE `wishlist_wishlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `wishlist_wishlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlist_wishlist_item`
--

DROP TABLE IF EXISTS `wishlist_wishlist_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist_wishlist_item` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` bigint NOT NULL,
  `wish_list_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wishlist_wishlist_item_product_id_cc6dd3c5_fk_product_product_id` (`product_id`),
  KEY `wishlist_wishlist_it_wish_list_id_91958c81_fk_wishlist_` (`wish_list_id`),
  CONSTRAINT `wishlist_wishlist_it_wish_list_id_91958c81_fk_wishlist_` FOREIGN KEY (`wish_list_id`) REFERENCES `wishlist_wishlist` (`user_id`),
  CONSTRAINT `wishlist_wishlist_item_product_id_cc6dd3c5_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist_wishlist_item`
--

LOCK TABLES `wishlist_wishlist_item` WRITE;
/*!40000 ALTER TABLE `wishlist_wishlist_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `wishlist_wishlist_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-13 21:20:20
