-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2025 at 10:04 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `distracted_drivers`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_tips`
--

CREATE TABLE `add_tips` (
  `id` int(10) NOT NULL,
  `title` varchar(50) NOT NULL,
  `tips` varchar(300) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `police_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_tips`
--

INSERT INTO `add_tips` (`id`, `title`, `tips`, `photo`, `police_id`) VALUES
(1, 'Wear Seatbelts', 'Always wear your seatbelt, whether youre the driver or a passenger. Seatbelts save lives.', 'p1.jpg', 'nedumangad12'),
(2, 'Follow Speed Limits', 'Adhere to the speed limits and drive at a safe speed according to road conditions.', 'p2.jpg', 'nedumangad12'),
(3, 'Dont Drink and Drive', 'Never drive under the influence of alcohol or drugs. It impairs your ability to drive safely.', 'p3.jpg', 'pothencode12'),
(4, 'Wear Helmets', 'If youre riding a motorcycle or bicycle always wear a helmet to protect your head.', 'p4.jpg', 'pothencode12'),
(5, 'Maintain Safe Distance', 'Keep a safe distance from the vehicle in front of you to avoid collisions.', 'p5.jpg', 'pothencode12');

-- --------------------------------------------------------

--
-- Table structure for table `detecttb`
--

CREATE TABLE `detecttb` (
  `id` int(11) NOT NULL,
  `msg` varchar(100) NOT NULL,
  `date` varchar(20) NOT NULL,
  `user_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detecttb`
--

INSERT INTO `detecttb` (`id`, `msg`, `date`, `user_id`) VALUES
(1, 'demo message', '2024-04-12', 'user'),
(2, 'demo msg', '2024-08-10', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `logid` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `logid`, `password`, `utype`) VALUES
(1, 'admin', '123', 'admin'),
(2, 'nedumangad12', '123', 'police'),
(3, 'pothencode12', '123', 'police');

-- --------------------------------------------------------

--
-- Table structure for table `police_reg`
--

CREATE TABLE `police_reg` (
  `id` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `location` varchar(50) NOT NULL,
  `loginid` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `contact_person` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `police_reg`
--

INSERT INTO `police_reg` (`id`, `name`, `location`, `loginid`, `password`, `contact`, `contact_person`, `photo`) VALUES
(1, 'Nedumangad Police Station', 'Sathramuke, Nedumangad', 'nedumangad12', '123', '9446569876', 'Sreekumar', 'a12.jpg'),
(2, 'Pothencode Police Station', 'Pothencode', 'pothencode12', '123', '9876564567', 'Rajeev S S', 'pothencode.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `unsafe_driving_logs`
--

CREATE TABLE `unsafe_driving_logs` (
  `id` int(11) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `timestamp` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `unsafe_driving_logs`
--

INSERT INTO `unsafe_driving_logs` (`id`, `filename`, `timestamp`) VALUES
(1, 'reaching behind_20250305_142038.jpg', '2025-03-05'),
(2, 'drinking_20250305_142044.jpg', '2025-03-05'),
(3, 'drinking_20250305_142048.jpg', '2025-03-05'),
(4, 'drinking_20250305_142052.jpg', '2025-03-05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `add_tips`
--
ALTER TABLE `add_tips`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `detecttb`
--
ALTER TABLE `detecttb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `police_reg`
--
ALTER TABLE `police_reg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `unsafe_driving_logs`
--
ALTER TABLE `unsafe_driving_logs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `add_tips`
--
ALTER TABLE `add_tips`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `detecttb`
--
ALTER TABLE `detecttb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `police_reg`
--
ALTER TABLE `police_reg`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `unsafe_driving_logs`
--
ALTER TABLE `unsafe_driving_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
