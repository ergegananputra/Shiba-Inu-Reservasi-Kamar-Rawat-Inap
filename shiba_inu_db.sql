-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2024 at 07:00 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fasilitas_layanan_kesehatan`
--
ALTER TABLE `fasilitas_layanan_kesehatan`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
