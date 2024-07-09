-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-07-2024 a las 15:55:09
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sitio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `who` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `nombre`, `imagen`, `who`) VALUES
(6, 'El Psicoanalista', '20240701155807_lib-cat-3.png', 'John Katzenbach - 2002'),
(8, 'Metro 2033', '20240701155820_lib-cat-4.png', 'Dmitry Gluhovsky - 2002'),
(10, 'Al costado de la luna', '20240703120000_lib-cat-1.jpeg', 'Graciela Geller - 2006'),
(13, 'Prueba', '20240705095813_fire.webp', 'Anonymus'),
(14, 'Javascript', '20240703131909_20240701092859_profilePic.png', 'https://www.google.com'),
(16, 'PYTHON', '20240704115744_arg.jpg', 'nose.com'),
(22, 'REQUIRED', '20240705101255_Characters.jpg', 'REQUIRED 2'),
(23, 'OTRO REQUIRED', '20240705101207_The-abbys-3-removebg.png', 'OTRO REQUIRED'),
(24, 'HIDE', '20240705101603_fondoGaleria.jpg', '...!'),
(25, 'editado', '20240705101648_Guns.jpg', 'dasd');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
