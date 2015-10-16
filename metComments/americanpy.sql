-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Gegenereerd op: 16 okt 2015 om 14:15
-- Serverversie: 5.6.26
-- PHP-versie: 5.6.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `americanpy`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `aanbieders`
--

CREATE TABLE IF NOT EXISTS `aanbieders` (
  `id` int(5) NOT NULL,
  `naam` varchar(40) NOT NULL,
  `achternaam` varchar(60) NOT NULL,
  `film` varchar(255) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1005 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `aanbieders`
--

INSERT INTO `aanbieders` (`id`, `naam`, `achternaam`, `film`, `username`, `password`) VALUES
(1000, 'David', 'Meulenbeld', '', 'David', '1234'),
(1001, 'Mitchell ', 'Bloemink', '', 'Mitchell', '2345'),
(1002, 'Dennis', 'van Valderen', '', 'Dennis', '3456'),
(1003, 'Tarik', 'Otman', 'Scream 2', 'Tarik', '4567'),
(1004, 'Rik', 'Ruttenberg', '', 'Rik', '5678');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `bezoekers`
--

CREATE TABLE IF NOT EXISTS `bezoekers` (
  `id` int(5) NOT NULL,
  `naam` varchar(32) NOT NULL,
  `email` varchar(32) NOT NULL,
  `aanbiederid` int(5) NOT NULL,
  `uniekecode` varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1012 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `bezoekers`
--

INSERT INTO `bezoekers` (`id`, `naam`, `email`, `aanbiederid`, `uniekecode`) VALUES
(1009, 'Piet', 'Piet@gmail.com', 1003, 'SlhwZlog#Krjv'),
(1010, 'AmericanPy', 'jos@gmail.com', 1003, 'DphulfdqS|P|vwlf#Uly'),
(1011, 'Jos', 'hu@hu.nl', 1003, 'MrvVfuhdp#5');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `films`
--

CREATE TABLE IF NOT EXISTS `films` (
  `id` int(5) NOT NULL,
  `titel` varchar(100) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `synopsis` varchar(255) NOT NULL,
  `genres` varchar(255) NOT NULL,
  `filmduur` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `zender` varchar(255) NOT NULL,
  `rating` varchar(255) NOT NULL,
  `starttijd` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `aanbieders`
--
ALTER TABLE `aanbieders`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `bezoekers`
--
ALTER TABLE `bezoekers`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `films`
--
ALTER TABLE `films`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `aanbieders`
--
ALTER TABLE `aanbieders`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1005;
--
-- AUTO_INCREMENT voor een tabel `bezoekers`
--
ALTER TABLE `bezoekers`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1012;
--
-- AUTO_INCREMENT voor een tabel `films`
--
ALTER TABLE `films`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
