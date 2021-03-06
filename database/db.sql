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

-- Volcando estructura para tabla imagenes.archivos
CREATE TABLE IF NOT EXISTS `archivos` (
  `id_producto` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_usuario` bigint(20) DEFAULT NULL,
  `nombre_archivo` varchar(255) DEFAULT NULL,
  `ruta_archivo` varchar(255) DEFAULT NULL,
  `tipo_archivo` varchar(255) DEFAULT NULL,
  `peso_archivo` varchar(255) DEFAULT NULL,
  `acceso_archivo` varchar(255) DEFAULT NULL,
  `ruta_imagen_archivo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imagenes.archivos: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `archivos` DISABLE KEYS */;
INSERT IGNORE INTO `archivos` (`id_producto`, `id_usuario`, `nombre_archivo`, `ruta_archivo`, `tipo_archivo`, `peso_archivo`, `acceso_archivo`, `ruta_imagen_archivo`) VALUES
	(9, 18, 'Programa', '2022-04-20_16_37_3_774452.html', 'html', '748.0 bytes', 'SI', './static/images/tipo_archivos/file_html.png'),
	(11, 18, 'imagen', '2022-04-20_16_42_55_140435.png', 'png', '896.0 KB', 'SI', './static/images/2022-04-20_16_42_55_140435.png'),
	(12, 19, 'Articulos', '2022-04-26_14_18_47_977413.pdf', 'pdf', '2.7 MB', 'SI', './static/tipo_archivos/file_pdf.png'),
	(13, 18, 'Llave', '2022-05-09_19_29_58_615071.png', 'png', '12.2 KB', 'SI', './static/images/2022-05-09_19_29_58_615071.png'),
	(14, 20, 'Salsa', '2022-05-12_14_55_54_603965.jpg', 'jpg', '123.6 KB', 'SI', './static/images/2022-05-12_14_55_54_603965.jpg');
/*!40000 ALTER TABLE `archivos` ENABLE KEYS */;

-- Volcando estructura para tabla imagenes.urls
CREATE TABLE IF NOT EXISTS `urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `nueva` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imagenes.urls: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `urls` DISABLE KEYS */;
INSERT IGNORE INTO `urls` (`id`, `url`, `nueva`) VALUES
	(1, 'https://virtual.itp.edu.co/', 'qa9T'),
	(2, 'https://virtual.itp.edu.co/', 'j2Yr'),
	(3, 'https://virtual.itp.edu.co/', '3GtB'),
	(4, 'https://virtual.itp.edu.co/', 'bwES'),
	(5, 'file:///D:/DOCUMENTOS%20USUARIO/Documents/RED_PARCIAL_SOLUCIONES_TELECOMUNICACIONES%20(1).svg', '7gCv'),
	(6, 'https://sigedin.itp.edu.co/sigedin/app_Login/app_Login.php', 'TrTJ');
/*!40000 ALTER TABLE `urls` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla imagenes.usuarios: ~17 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT IGNORE INTO `usuarios` (`id_usuario`, `nombre_usuario`, `apellido_usuario`, `user`, `password`, `validate`, `tokenPass`) VALUES
	(5, 'YILBER ', 'GUEVARA', 'yilber-88@hotmail.com', 'dbae2dd6daf2b924ac945f2220847e64c2673d89d751d8ae2b4735999539b51026aebf39cea53d47432fa656c696332e0a9f6e762f9f6f2506335230e309ca60', 'true', NULL),
	(6, 'YILBER ', 'GUEVARA', 'sauteuppegowu-1555@yopmail.com', '04ff751a451995fd412ed405fcace61984acffe7b1622af2d5a4230d2a34c34a25fb8da496e5929cf698a11d597774a79a1e9c98a54dfc4178596ccc365ee213', 'true', ''),
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
	(18, 'YILBER ', 'GUEVARA', 'freimeiwoxinnei-3676@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', 'lZFdFR1jYy'),
	(19, 'YILBER ', 'GUEVARA', 'grotausseheico-2663@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', ''),
	(20, 'YILBER ', 'GUEVARA', 'jabugucabroi-8449@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', ''),
	(21, 'YILBER ', 'GUEVARA', 'biseicrocrifreu-2881@yopmail.com', '05be276766564accacc6286ca0593d2b66ee9be012f2b35abc352df4bf044ab998cb72c71a940a853cb84e7defba48ee4220464e3676528d935dd307386ac0f3', 'si', '');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
