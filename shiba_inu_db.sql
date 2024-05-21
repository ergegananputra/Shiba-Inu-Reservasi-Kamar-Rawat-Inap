-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2024 at 02:40 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shiba_inu_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `fasilitas_layanan_kesehatan`
--

CREATE TABLE `fasilitas_layanan_kesehatan` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `nama` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fasilitas_layanan_kesehatan`
--

INSERT INTO `fasilitas_layanan_kesehatan` (`id`, `nama`, `alamat`, `create_at`, `update_at`) VALUES
('080509d2-15ec-11ef-a992-0a002700000c', 'RS Panti Rapih', 'Jalan Cik Di Tiro', '2024-05-19 14:28:16', '2024-05-19 14:28:16'),
('555799ce881c488890242154a6392b92', 'RS UGM', 'Jalan Kaliurang', '2024-05-19 16:58:35', '2024-05-19 16:58:35'),
('5a64db3aafd340b8b2c3c394542bf896', 'RS Bethesda', 'Jalan Pancura', '2024-05-19 15:26:22', '2024-05-19 15:26:22');

-- --------------------------------------------------------

--
-- Table structure for table `jenis_tempat_tidur`
--

CREATE TABLE `jenis_tempat_tidur` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `jenis_tempat_tidur` varchar(255) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jenis_tempat_tidur`
--

INSERT INTO `jenis_tempat_tidur` (`id`, `jenis_tempat_tidur`, `keterangan`, `create_at`, `update_at`) VALUES
('3e041783ffe1442381d9d1c64ac05a8d', 'Suite', 'Mahal', '2024-05-20 16:29:05', '2024-05-21 00:34:51'),
('b9f4dfc363a84534961aa82957699202', 'Single', 'Satu ranjang', '2024-05-20 15:17:13', '2024-05-20 15:17:13'),
('de3744c5586a4a4195448d2347ed1a9c', 'Bunk', 'Ranjang bertingkat updated', '2024-05-20 16:32:48', '2024-05-20 16:33:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fasilitas_layanan_kesehatan`
--
ALTER TABLE `fasilitas_layanan_kesehatan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jenis_tempat_tidur`
--
ALTER TABLE `jenis_tempat_tidur`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
