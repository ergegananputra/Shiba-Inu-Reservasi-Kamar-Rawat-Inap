-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 26 Bulan Mei 2024 pada 11.48
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

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
-- Struktur dari tabel `fasilitas_detail_kamar`
--

CREATE TABLE `fasilitas_detail_kamar` (
  `id` char(36) NOT NULL DEFAULT 'uuid()',
  `fk__fpr` char(36) NOT NULL DEFAULT 'uuid()',
  `tabung_oksigen` int(11) DEFAULT NULL,
  `kamar_mandi` int(11) DEFAULT NULL,
  `infus` int(11) DEFAULT NULL,
  `nurse_call` int(11) DEFAULT NULL,
  `kasur_pendamping` int(11) DEFAULT NULL,
  `sofa` int(11) DEFAULT NULL,
  `lemari` int(11) DEFAULT NULL,
  `meja_makan_pasien` int(11) DEFAULT NULL,
  `meja_makan_pendamping` int(11) DEFAULT NULL,
  `televisi` int(11) DEFAULT NULL,
  `dispenser` int(11) DEFAULT NULL,
  `kulkas` int(11) DEFAULT NULL,
  `wastafel` int(11) DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `fasilitas_layanan_kesehatan`
--

CREATE TABLE `fasilitas_layanan_kesehatan` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `nama` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `fasilitas_layanan_kesehatan`
--

INSERT INTO `fasilitas_layanan_kesehatan` (`id`, `nama`, `alamat`, `create_at`, `update_at`) VALUES
('080509d2-15ec-11ef-a992-0a002700000c', 'RS Panti Rapih', 'Jalan Cik Di Tiro', '2024-05-19 14:28:16', '2024-05-19 14:28:16'),
('555799ce881c488890242154a6392b92', 'RS UGM', 'Jalan Kaliurang', '2024-05-19 16:58:35', '2024-05-19 16:58:35'),
('5a64db3aafd340b8b2c3c394542bf896', 'RS Bethesda', 'Jalan Pancura', '2024-05-19 15:26:22', '2024-05-19 15:26:22');

-- --------------------------------------------------------

--
-- Struktur dari tabel `fleet_kamar`
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
-- Dumping data untuk tabel `fleet_kamar`
--

INSERT INTO `fleet_kamar` (`id`, `fk_flk`, `nama`, `jenis_kamar`, `informasi_pembayaran`, `create_at`, `update_at`) VALUES
('7d6e4d3b-1722-11ef-9fd4-38f3ab6d2057', '5a64db3aafd340b8b2c3c394542bf896', 'kamar 1', 'umum', 'debit', '2024-05-21 03:30:37', '2024-05-21 03:30:37'),
('9529d21e-1722-11ef-9fd4-38f3ab6d2057', '5a64db3aafd340b8b2c3c394542bf896', 'kamar 2', 'umum', 'kredit', '2024-05-21 03:31:17', '2024-05-25 10:00:50'),
('a53866c9-1722-11ef-9fd4-38f3ab6d2057', '080509d2-15ec-11ef-a992-0a002700000c', 'isolasi 1', 'isolasi', 'both', '2024-05-21 03:31:44', '2024-05-21 03:31:44');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jenis_tempat_tidur`
--

CREATE TABLE `jenis_tempat_tidur` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `jenis_tempat_tidur` varchar(255) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `jenis_tempat_tidur`
--

INSERT INTO `jenis_tempat_tidur` (`id`, `jenis_tempat_tidur`, `keterangan`, `create_at`, `update_at`) VALUES
('3e041783ffe1442381d9d1c64ac05a8d', 'Suite', 'Mahal', '2024-05-20 16:29:05', '2024-05-21 00:34:51'),
('b9f4dfc363a84534961aa82957699202', 'Single', 'Satu ranjang', '2024-05-20 15:17:13', '2024-05-20 15:17:13'),
('de3744c5586a4a4195448d2347ed1a9c', 'Bunk', 'Ranjang bertingkat updated', '2024-05-20 16:32:48', '2024-05-20 16:33:43');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pendingin_ruangan`
--

CREATE TABLE `pendingin_ruangan` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `nama` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pendingin_ruangan`
--

INSERT INTO `pendingin_ruangan` (`id`, `nama`, `create_at`, `update_at`) VALUES
('0567a8ff61cc42038a00d7203c82608e', 'Kipas angin', '2024-05-21 08:16:25', '2024-05-21 08:16:25'),
('62866c0b9afa4993b6ee0767ba62a406', 'AC', '2024-05-21 07:19:17', '2024-05-21 08:16:04');

-- --------------------------------------------------------

--
-- Struktur dari tabel `status_kamar`
--

CREATE TABLE `status_kamar` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `status` varchar(255) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `status_kamar`
--

INSERT INTO `status_kamar` (`id`, `status`, `create_at`, `update_at`) VALUES
('2f5c201d1bd4487db722f84027465c35', 'Tersedia', '2024-05-21 02:46:10', '2024-05-21 02:46:10'),
('8f59627643824d6b83a98e9bca2a3bcd', 'Penuh', '2024-05-21 02:46:20', '2024-05-21 02:46:20'),
('fe76f7a01ca5403dac6101e49d0f6302', 'Perbaikan', '2024-05-21 02:46:35', '2024-05-21 02:46:35');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `fasilitas_detail_kamar`
--
ALTER TABLE `fasilitas_detail_kamar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `fk_fpr` (`fk__fpr`);

--
-- Indeks untuk tabel `fasilitas_layanan_kesehatan`
--
ALTER TABLE `fasilitas_layanan_kesehatan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indeks untuk tabel `fleet_kamar`
--
ALTER TABLE `fleet_kamar`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `fk_flk` (`fk_flk`);

--
-- Indeks untuk tabel `jenis_tempat_tidur`
--
ALTER TABLE `jenis_tempat_tidur`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indeks untuk tabel `pendingin_ruangan`
--
ALTER TABLE `pendingin_ruangan`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indeks untuk tabel `status_kamar`
--
ALTER TABLE `status_kamar`
  ADD UNIQUE KEY `id` (`id`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `fleet_kamar`
--
ALTER TABLE `fleet_kamar`
  ADD CONSTRAINT `fleet_kamar_ibfk_1` FOREIGN KEY (`fk_flk`) REFERENCES `fasilitas_layanan_kesehatan` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
