-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 26, 2024 at 05:55 AM
-- Server version: 8.0.36
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
  `id` char(36) NOT NULL DEFAULT (uuid()),
  `nama` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `fasilitas_layanan_kesehatan`
--

INSERT INTO `fasilitas_layanan_kesehatan` (`id`, `nama`, `alamat`, `create_at`, `update_at`) VALUES
('080509d2-15ec-11ef-a992-0a002700000c', 'RS Panti Rapih', 'Jalan Cik Di Tiro', '2024-05-19 07:28:16', '2024-05-19 07:28:16'),
('555799ce881c488890242154a6392b92', 'RS UGM', 'Jalan Kaliurang', '2024-05-19 09:58:35', '2024-05-19 09:58:35'),
('5a64db3aafd340b8b2c3c394542bf896', 'RS Bethesda', 'Jalan Pancura', '2024-05-19 08:26:22', '2024-05-19 08:26:22');

-- --------------------------------------------------------

--
-- Table structure for table `fleet_kamar`
--

CREATE TABLE `fleet_kamar` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_flk` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `nama` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `jenis_kamar` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `informasi_pembayaran` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fleet_kamar`
--

INSERT INTO `fleet_kamar` (`id`, `fk_flk`, `nama`, `jenis_kamar`, `informasi_pembayaran`, `create_at`, `update_at`) VALUES
('7d6e4d3b-1722-11ef-9fd4-38f3ab6d2057', '5a64db3aafd340b8b2c3c394542bf896', 'kamar 1', 'umum', 'debit', '2024-05-20 20:30:37', '2024-05-20 20:30:37'),
('9529d21e-1722-11ef-9fd4-38f3ab6d2057', '5a64db3aafd340b8b2c3c394542bf896', 'kamar 2', 'umum', 'kredit', '2024-05-20 20:31:17', '2024-05-25 03:00:50'),
('a53866c9-1722-11ef-9fd4-38f3ab6d2057', '080509d2-15ec-11ef-a992-0a002700000c', 'isolasi 1', 'isolasi', 'both', '2024-05-20 20:31:44', '2024-05-20 20:31:44');

-- --------------------------------------------------------

--
-- Table structure for table `fleet_kamar`
--

CREATE TABLE `fleet_kamar` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `fk_flk` char(36) NOT NULL DEFAULT uuid(),
  `nama` varchar(255) DEFAULT NULL,
  `jenis_kamar` varchar(255) DEFAULT NULL,
  `informasi_pembayaran` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fleet_kamar`
--

INSERT INTO `fleet_kamar` (`id`, `fk_flk`, `nama`, `jenis_kamar`, `informasi_pembayaran`, `create_at`, `update_at`) VALUES
('7d6e4d3b-1722-11ef-9fd4-38f3ab6d2057', '5a64db3aafd340b8b2c3c394542bf896', 'kamar 1', 'umum', 'debit', '2024-05-21 03:30:37', '2024-05-21 03:30:37'),
('9529d21e-1722-11ef-9fd4-38f3ab6d2057', '5a64db3aafd340b8b2c3c394542bf896', 'kamar 2', 'umum', 'kredit', '2024-05-21 03:31:17', '2024-05-25 10:00:50'),
('a53866c9-1722-11ef-9fd4-38f3ab6d2057', '080509d2-15ec-11ef-a992-0a002700000c', 'isolasi 1', 'isolasi', 'both', '2024-05-21 03:31:44', '2024-05-21 03:31:44');

-- --------------------------------------------------------

--
-- Table structure for table `jenis_tempat_tidur`
--

CREATE TABLE `jenis_tempat_tidur` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `jenis_tempat_tidur` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keterangan` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jenis_tempat_tidur`
--

INSERT INTO `jenis_tempat_tidur` (`id`, `jenis_tempat_tidur`, `keterangan`, `create_at`, `update_at`) VALUES
('3e041783ffe1442381d9d1c64ac05a8d', 'Suite', 'Mahal', '2024-05-20 09:29:05', '2024-05-20 17:34:51'),
('b9f4dfc363a84534961aa82957699202', 'Single', 'Satu ranjang', '2024-05-20 08:17:13', '2024-05-20 08:17:13'),
('de3744c5586a4a4195448d2347ed1a9c', 'Bunk', 'Ranjang bertingkat updated', '2024-05-20 09:32:48', '2024-05-20 09:33:43');

-- --------------------------------------------------------

--
-- Table structure for table `kasur`
--

CREATE TABLE `kasur` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_fkr` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_sk` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_jtt` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_fdk` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `tingkat_fasilitas_kesehatan` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `biaya_pakai_per_hari` double DEFAULT NULL,
  `kode_kamar` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pendingin_ruangan`
--

CREATE TABLE `pendingin_ruangan` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `nama` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pendingin_ruangan`
--

INSERT INTO `pendingin_ruangan` (`id`, `nama`, `create_at`, `update_at`) VALUES
('0567a8ff61cc42038a00d7203c82608e', 'Kipas angin', '2024-05-21 01:16:25', '2024-05-21 01:16:25'),
('62866c0b9afa4993b6ee0767ba62a406', 'AC', '2024-05-21 00:19:17', '2024-05-21 01:16:04');

-- --------------------------------------------------------

--
-- Table structure for table `status_kamar`
--

CREATE TABLE `status_kamar` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `status` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status_kamar`
--

INSERT INTO `status_kamar` (`id`, `status`, `create_at`, `update_at`) VALUES
('2f5c201d1bd4487db722f84027465c35', 'Tersedia', '2024-05-20 19:46:10', '2024-05-20 19:46:10'),
('8f59627643824d6b83a98e9bca2a3bcd', 'Penuh', '2024-05-20 19:46:20', '2024-05-20 19:46:20'),
('fe76f7a01ca5403dac6101e49d0f6302', 'Perbaikan', '2024-05-20 19:46:35', '2024-05-20 19:46:35');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fasilitas_layanan_kesehatan`
--
ALTER TABLE `fasilitas_layanan_kesehatan`
  ADD PRIMARY KEY (`id`);


--
-- Indexes for table `fleet_kamar`
--
ALTER TABLE `fleet_kamar`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `fk_flk` (`fk_flk`);

--
-- Indexes for table `jenis_tempat_tidur`
--
ALTER TABLE `jenis_tempat_tidur`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `kasur`
--
ALTER TABLE `kasur`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `pendingin_ruangan`
--
ALTER TABLE `pendingin_ruangan`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `status_kamar`
--
ALTER TABLE `status_kamar`
  ADD UNIQUE KEY `id` (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fleet_kamar`
--
ALTER TABLE `fleet_kamar`
  ADD CONSTRAINT `fleet_kamar_ibfk_1` FOREIGN KEY (`fk_flk`) REFERENCES `fasilitas_layanan_kesehatan` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
