-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para imagenes
CREATE DATABASE IF NOT EXISTS `imagenes` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `imagenes`;

-- Volcando estructura para tabla imagenes.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(50) DEFAULT NULL,
  `apellido_usuario` varchar(255) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `validate` varchar(5) DEFAULT NULL,
  `tokenPass` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imagenes.usuarios: ~15 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT IGNORE INTO `usuarios` (`id_usuario`, `nombre_usuario`, `apellido_usuario`, `user`, `password`, `validate`, `tokenPass`) VALUES
	(5, 'YILBER ', 'GUEVARA', 'yilber-88@hotmail.com', 'dbae2dd6daf2b924ac945f2220847e64c2673d89d751d8ae2b4735999539b51026aebf39cea53d47432fa656c696332e0a9f6e762f9f6f2506335230e309ca60', 'true', NULL),
	(6, 'YILBER ', 'GUEVARA', 'sauteuppegowu-1555@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(7, 'YILBER ', 'GUEVARA', 'gugogrulaprau-6603@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'Tp0BO', NULL),
	(8, 'YILBER ', 'GUEVARA', 'nebabippene-5501@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', NULL),
	(9, 'YILBER ', 'GUEVARA', 'vavejatroipru-9309@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(10, 'YILBER ', 'GUEVARA', 'niprofauppade-6763@yopmail.com', 'fcd08d9670c54ace9046ce494ed0f94d065bb80ddf549e72de2747cdb9a3d80d6724fcfa587749b3a185f02a18ab62f731f7c91566d67c824d2c7e4408e5343b', 'true', NULL),
	(11, 'YILBER ', 'GUEVARA', 'beussoddullamu-4521@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(12, 'YILBER ', 'GUEVARA', 'xugulettoijeu-6816@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(13, 'YILBER ', 'GUEVARA', 'fromelleifrauzei-8829@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(14, 'YILBER ', 'GUEVARA', 'xommepreupeufro-3245@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(15, 'YILBER ', 'GUEVARA', 'queiddonanissu-8994@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(16, 'YILBER ', 'GUEVARA', 'bazarabreuddei-1504@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(17, 'YILBER ', 'GUEVARA', 'juttetticoippa-9410@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'true', NULL),
	(18, 'YILBER ', 'GUEVARA', 'freimeiwoxinnei-3676@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', NULL),
	(19, 'YILBER ', 'GUEVARA', 'grotausseheico-2663@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
