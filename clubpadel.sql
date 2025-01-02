-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3307
-- Tiempo de generación: 02-01-2025 a las 17:36:55
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `clubpadel`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `alquiler_cancha` (IN `id_cancha` INT, IN `fecha` DATE, IN `hora_inicio` TIME, IN `hora_fin` TIME)   BEGIN
    DECLARE conflictos INT;

    -- Verifica conflictos de horario
    SELECT COUNT(*) INTO conflictos
    FROM horarios
    WHERE id_canchas = id_cancha
      AND fecha = fecha_consulta
      AND (
          (hora_inicio_consulta >= hora_inicio AND hora_inicio_consulta < hora_fin) OR
          (hora_fin_consulta > hora_inicio AND hora_fin_consulta <= hora_fin) OR
          (hora_inicio_consulta <= hora_inicio AND hora_fin_consulta >= hora_fin)
      );

    IF conflictos = 0 THEN
        SELECT 'Puedes alquilar esta cancha' AS disponibilidad;
    ELSE
        SELECT 'La cancha no está disponible en ese horario' AS disponibilidad;
    END IF;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `canchas`
--

CREATE TABLE `canchas` (
  `id_canchas` int(11) NOT NULL,
  `superficie` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `canchas`
--

INSERT INTO `canchas` (`id_canchas`, `superficie`) VALUES
(1, 'Césped'),
(2, 'Concreto'),
(3, 'Concreto'),
(4, 'Césped');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios`
--

CREATE TABLE `horarios` (
  `id_horario` int(11) NOT NULL,
  `id_socio` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `id_canchas` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horarios`
--

INSERT INTO `horarios` (`id_horario`, `id_socio`, `fecha`, `hora_inicio`, `hora_fin`, `id_canchas`) VALUES
(4, 2, '2024-05-06', '19:00:00', '20:00:00', 1),
(5, 3, '2024-10-30', '21:00:00', '22:00:00', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socios`
--

CREATE TABLE `socios` (
  `id_socio` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `socios`
--

INSERT INTO `socios` (`id_socio`, `nombre`, `apellido`, `telefono`, `email`) VALUES
(1, 'Teo', 'Fernandez', '11-3857-4290', 'teo@gmail.com'),
(2, 'carlos', 'nuñes', '1125647895', 'mmm@hotmail'),
(3, 'Noelia', 'Nicocia', '11-2543-1234', 'noelia@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `canchas`
--
ALTER TABLE `canchas`
  ADD PRIMARY KEY (`id_canchas`);

--
-- Indices de la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`id_horario`),
  ADD KEY `socios_id_socios_horarios` (`id_socio`),
  ADD KEY `canchas_id_canchas_horarios` (`id_canchas`);

--
-- Indices de la tabla `socios`
--
ALTER TABLE `socios`
  ADD PRIMARY KEY (`id_socio`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `canchas`
--
ALTER TABLE `canchas`
  MODIFY `id_canchas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `horarios`
--
ALTER TABLE `horarios`
  MODIFY `id_horario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `socios`
--
ALTER TABLE `socios`
  MODIFY `id_socio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD CONSTRAINT `canchas_id_canchas_horarios` FOREIGN KEY (`id_canchas`) REFERENCES `canchas` (`id_canchas`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `socios_id_socios_horarios` FOREIGN KEY (`id_socio`) REFERENCES `socios` (`id_socio`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
