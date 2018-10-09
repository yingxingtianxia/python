-- MySQL dump 10.13  Distrib 5.6.11, for Linux (x86_64)
--
-- Host: localhost    Database: ecom
-- ------------------------------------------------------
-- Server version	5.6.11-log

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `id` int(11) unsigned NOT NULL COMMENT '订单号',
  `id_user` varchar(50) NOT NULL DEFAULT '' COMMENT '买家用户编号',
  `totalpay` double NOT NULL COMMENT '订单总额',
  `dtime` varchar(50) NOT NULL DEFAULT '' COMMENT '订单产生的时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='购买订单表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (5,'1',132.61,'2016-08-05 23:07:18'),(6,'1',68.63,'2016-08-05 23:07:47');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_item`
--

DROP TABLE IF EXISTS `bill_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill_item` (
  `id_bill` int(11) unsigned NOT NULL COMMENT '订单号',
  `id_product` varchar(50) NOT NULL DEFAULT '' COMMENT '商品编号',
  `pcount` int(11) NOT NULL COMMENT '购买数量',
  `price` int(11) NOT NULL COMMENT '单价'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单清单表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_item`
--

LOCK TABLES `bill_item` WRITE;
/*!40000 ALTER TABLE `bill_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `bill_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) unsigned NOT NULL COMMENT '商品编号',
  `cname` varchar(50) NOT NULL DEFAULT '' COMMENT '商品名称',
  `cdes` varchar(200) NOT NULL DEFAULT '' COMMENT '商品描述',
  `cpic` varchar(50) NOT NULL DEFAULT '' COMMENT '图片',
  `cprice` varchar(10) NOT NULL DEFAULT '' COMMENT '价格',
  `pcount` int(11) NOT NULL COMMENT '库存数量',
  `dtime` varchar(50) NOT NULL DEFAULT '' COMMENT '上架时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商品表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'坚果干果炒货零食','零食，样样美味，酌饮一口，齿颊留香!中外品牌\"惠\"聚，任您精挑细选!天猫超市，实惠到家，体验健康生活!','a00001.jpg','31.99',10,''),(2,'统一100 老坛酸菜牛肉面','又辣又酸，快捷方便，出差旅游是必备食品。带给你现代快节奏的效率。','a00015.jpg','14.88',50,''),(3,'百草味-炭烧腰果','大颗粒腰果 颗粒饱满 香脆美味','a00018.jpg','45.88',100,''),(4,'艾do家纺 纯棉四件套','全棉四件套纯棉春夏被套床单4件套1.8m床2.0双人件套简约床上用品 ','a00011.jpg','688.00',70,''),(5,'蓝月亮洗手液','蓝月亮机洗至尊，开启机洗泵时代！一次一泵，计量精准；小体积，大能量。','a00004.jpg','23.99',180,''),(6,'威露士洗衣除菌消毒液','专业品牌，有机健康，享品质生活!天猫超市，品牌直营，品质护航，一站购齐!上天猫，就够了!','a00012.jpg','37.88',90,''),(7,'Herbs/禾博士 维生素C咀嚼片','品牌聚惠，品质保障，畅享健康生活!部分地区更享当日达!天猫超市-100%正品!部分城市更享当日达，当日买，当日用，省钱省心! ','a00005.jpg','23.99',200,''),(8,'2016夏季牛皮女童凉鞋','真皮 女童鞋-汪涵代言「蜜芽」精选进口童鞋，舒适透气，时尚耐磨，妈妈疯抢，1折起，国际品牌入驻，强强联手!','a00021.jpg','65.00',20,'');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL COMMENT '用户编号',
  `clogin` varchar(50) NOT NULL DEFAULT '' COMMENT '用户登录名',
  `cpwd` varchar(200) NOT NULL DEFAULT '' COMMENT '用户登录密码，md5',
  `dtime` varchar(50) NOT NULL DEFAULT '' COMMENT '用户注册时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'tom','123','3'),(2,'alice','23','2'),(3,'John','123','');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-06 15:54:29
