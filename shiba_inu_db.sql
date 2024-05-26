-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 26, 2024 at 01:52 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

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
-- Table structure for table `fasilitas_detail_kamar`
--

CREATE TABLE `fasilitas_detail_kamar` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'uuid()',
  `fk_fpr` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `tabung_oksigen` int DEFAULT NULL,
  `kamar_mandi` int DEFAULT NULL,
  `infus` int DEFAULT NULL,
  `nurse_call` int DEFAULT NULL,
  `kasur_pendamping` int DEFAULT NULL,
  `sofa` int DEFAULT NULL,
  `lemari` int DEFAULT NULL,
  `meja_makan_pasien` int DEFAULT NULL,
  `meja_makan_pendamping` int DEFAULT NULL,
  `televisi` int DEFAULT NULL,
  `dispenser` int DEFAULT NULL,
  `kulkas` int DEFAULT NULL,
  `wastafel` int DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fasilitas_detail_kamar`
--

INSERT INTO `fasilitas_detail_kamar` (`id`, `fk_fpr`, `tabung_oksigen`, `kamar_mandi`, `infus`, `nurse_call`, `kasur_pendamping`, `sofa`, `lemari`, `meja_makan_pasien`, `meja_makan_pendamping`, `televisi`, `dispenser`, `kulkas`, `wastafel`, `create_at`, `update_at`) VALUES
('5091e4d9bf4d465f8a9ddfcd7c0533f9', '4be14015823b4f94bacf3da5a714abec', 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, '2024-05-26 12:52:13', '2024-05-26 12:52:13');

-- --------------------------------------------------------

--
-- Table structure for table `fasilitas_layanan_kesehatan`
--

CREATE TABLE `fasilitas_layanan_kesehatan` (
  `id` char(36) COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `nama` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `alamat` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fasilitas_layanan_kesehatan`
--

INSERT INTO `fasilitas_layanan_kesehatan` (`id`, `nama`, `alamat`, `create_at`, `update_at`) VALUES
('0e77ed8a440646499be3af447b6c6cf0', 'RS Panti Rapih', 'Jalan Cik Di Tiro No 9', '2024-05-26 12:53:16', '2024-05-26 12:53:16');

-- --------------------------------------------------------

--
-- Table structure for table `fleet_kamar`
--

CREATE TABLE `fleet_kamar` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_flk` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `nama` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `jenis_kamar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `informasi_pembayaran` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fleet_kamar`
--

INSERT INTO `fleet_kamar` (`id`, `fk_flk`, `nama`, `jenis_kamar`, `informasi_pembayaran`, `create_at`, `update_at`) VALUES
('245b256470324a59b53382644af5fdb1', '0e77ed8a440646499be3af447b6c6cf0', 'kamar 1', 'umum', 'debit', '2024-05-26 13:41:25', '2024-05-26 13:41:25'),
('86aa13a2ed3a482e83b6f9894e97e809', '0e77ed8a440646499be3af447b6c6cf0', 'kamar 2', 'umum', 'both', '2024-05-26 13:37:10', '2024-05-26 13:42:26'),
('d414bdb48b394c559269064055f39d6d', '0e77ed8a440646499be3af447b6c6cf0', 'kamar 3', 'umum', 'kredit', '2024-05-26 12:58:31', '2024-05-26 13:42:30');

-- --------------------------------------------------------

--
-- Table structure for table `jenis_tempat_tidur`
--

CREATE TABLE `jenis_tempat_tidur` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `jenis_tempat_tidur` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keterangan` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jenis_tempat_tidur`
--

INSERT INTO `jenis_tempat_tidur` (`id`, `jenis_tempat_tidur`, `keterangan`, `create_at`, `update_at`) VALUES
('ee6e7614b7a1487e85205af2953815ee', 'single', 'Kamar hanya terdiri dari satu kasur', '2024-05-26 13:45:30', '2024-05-26 13:45:30');

-- --------------------------------------------------------

--
-- Table structure for table `kasur`
--

CREATE TABLE `kasur` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_fkr` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_sk` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_jtt` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `fk_fdk` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `tingkat_fasilitas_kesehatan` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `biaya_pakai_per_hari` double DEFAULT NULL,
  `kode_kamar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kasur`
--

INSERT INTO `kasur` (`id`, `fk_fkr`, `fk_sk`, `fk_jtt`, `fk_fdk`, `tingkat_fasilitas_kesehatan`, `biaya_pakai_per_hari`, `kode_kamar`, `create_at`, `update_at`) VALUES
('bff758629b034d0a8a4328cbd8b1c86d', '86aa13a2ed3a482e83b6f9894e97e809', '95284db6378c4ab99ba2d5e6a3d9194c', 'ee6e7614b7a1487e85205af2953815ee', '5091e4d9bf4d465f8a9ddfcd7c0533f9', 'KRIS', 100000, 'Kasatra 5', '2024-05-26 13:51:26', '2024-05-26 13:51:26');

-- --------------------------------------------------------

--
-- Table structure for table `pendingin_ruangan`
--

CREATE TABLE `pendingin_ruangan` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `nama` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pendingin_ruangan`
--

INSERT INTO `pendingin_ruangan` (`id`, `nama`, `create_at`, `update_at`) VALUES
('4be14015823b4f94bacf3da5a714abec', 'Kipas Angin', '2024-05-26 12:04:43', '2024-05-26 12:04:43'),
('70265bf315c943e0a892db7f50b0c2e6', 'AC', '2024-05-26 12:05:02', '2024-05-26 12:05:02');

-- --------------------------------------------------------

--
-- Table structure for table `status_kamar`
--

CREATE TABLE `status_kamar` (
  `id` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT (uuid()),
  `status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status_kamar`
--

INSERT INTO `status_kamar` (`id`, `status`, `create_at`, `update_at`) VALUES
('95284db6378c4ab99ba2d5e6a3d9194c', 'terpakai', '2024-05-26 13:44:17', '2024-05-26 13:44:17'),
('95f2f217b3d74954811ae846dae5d265', 'perbaikan', '2024-05-26 13:44:32', '2024-05-26 13:44:32'),
('b1ef7b9b13734536b625e40684bc1937', 'kosong', '2024-05-26 13:44:25', '2024-05-26 13:44:25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fasilitas_detail_kamar`
--
ALTER TABLE `fasilitas_detail_kamar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `fdk_fk_fpr` (`fk_fpr`);

--
-- Indexes for table `fasilitas_layanan_kesehatan`
--
ALTER TABLE `fasilitas_layanan_kesehatan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `fleet_kamar`
--
ALTER TABLE `fleet_kamar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `fkr_fk_flk` (`fk_flk`);

--
-- Indexes for table `jenis_tempat_tidur`
--
ALTER TABLE `jenis_tempat_tidur`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `kasur`
--
ALTER TABLE `kasur`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `k_fk_fkr` (`fk_fkr`),
  ADD KEY `k_fk_sk` (`fk_sk`),
  ADD KEY `k_fk_jtt` (`fk_jtt`),
  ADD KEY `k_fk_fdk` (`fk_fdk`);

--
-- Indexes for table `pendingin_ruangan`
--
ALTER TABLE `pendingin_ruangan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `status_kamar`
--
ALTER TABLE `status_kamar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fasilitas_detail_kamar`
--
ALTER TABLE `fasilitas_detail_kamar`
  ADD CONSTRAINT `fdk_fk_fpr` FOREIGN KEY (`fk_fpr`) REFERENCES `pendingin_ruangan` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT;

--
-- Constraints for table `fleet_kamar`
--
ALTER TABLE `fleet_kamar`
  ADD CONSTRAINT `fkr_fk_flk` FOREIGN KEY (`fk_flk`) REFERENCES `fasilitas_layanan_kesehatan` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT;

--
-- Constraints for table `kasur`
--
ALTER TABLE `kasur`
  ADD CONSTRAINT `k_fk_fdk` FOREIGN KEY (`fk_fdk`) REFERENCES `fasilitas_detail_kamar` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `k_fk_fkr` FOREIGN KEY (`fk_fkr`) REFERENCES `fleet_kamar` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `k_fk_jtt` FOREIGN KEY (`fk_jtt`) REFERENCES `jenis_tempat_tidur` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  ADD CONSTRAINT `k_fk_sk` FOREIGN KEY (`fk_sk`) REFERENCES `status_kamar` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
