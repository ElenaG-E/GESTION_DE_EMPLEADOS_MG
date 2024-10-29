

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `asignacion` (
  `ID_ASIG` int(11) NOT NULL,
  `ID_DEPTO` int(11) NOT NULL,
  `ID_RUT` int(11) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



CREATE TABLE `clientes` (
  `ID_RUT` int(11) NOT NULL,
  `NOMBRE` varchar(50) DEFAULT NULL,
  `FECHA_NAC` date DEFAULT NULL,
  `FECHA_CONTRATO` date DEFAULT NULL,
  `SALARIO` int(11) DEFAULT NULL,
  `CORREO` varchar(50) DEFAULT NULL,
  `TELEFONO` varchar(15) DEFAULT NULL,
  `DIRECC` varchar(100) DEFAULT NULL,
  `ID_ROL` int(11) DEFAULT NULL,
  `ID_TIPO` int(11) DEFAULT NULL,
  `NOM_USUARIO` varchar(50) DEFAULT NULL,
  `PASSWORD` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--

CREATE TABLE `departamento` (
  `ID_DEPTO` int(11) NOT NULL,
  `NOMBRE` varchar(60) NOT NULL,
  `ID_RUT` int(11) NOT NULL,
  PRIMARY KEY (ID_DEPTO),
  CONSTRAINT FOREIGN KEY (ID_RUT) REFERENCES EMPLEADOS(ID_RUT)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `ID_RUT` int(11) NOT NULL,
  `NOMBRE` varchar(100) NOT NULL,
  `FECHA_NAC` date DEFAULT NULL,
  `FECHA_CONTRATO` date DEFAULT NULL,
  `SALARIO` int(11) NOT NULL,
  `CORREO` varchar(30) NOT NULL,
  `TELEFONO` varchar(13) NOT NULL,
  `DIRECC` varchar(100) NOT NULL,
  `ID_ROL` int(11) NOT NULL,
  `ID_TIPO` int(11) NOT NULL,
  `NOM_USUARIO` varchar(50) NOT NULL,
  `PASSWORD` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

CREATE TABLE `informe` (
  `ID_INFORME` int(11) NOT NULL,
  `ID_RUT` int(11) NOT NULL,
  `FECHA_HORA` date NOT NULL,
  `REPORTE` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `ID_MODULO` int(11) NOT NULL,
  `NOMODULO` varchar(100) NOT NULL,
  `ID_ROL` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `ID_PROYECTO` int(11) NOT NULL,
  `NOMBRE` varchar(100) NOT NULL,
  `DESCRIPCION` varchar(200) NOT NULL,
  `FECHA_INICIO` date NOT NULL,
  `FECHA_PLAZO` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto_emp`
--

CREATE TABLE `proyecto_emp` (
  `ID_PROYEMP` int(11) NOT NULL,
  `ID_PROYECTO` int(11) NOT NULL,
  `ID_TIPO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

CREATE TABLE `registro_tiempo` (
  `ID_REG_TIEMPO` int(11) NOT NULL,
  `FECHA` date NOT NULL,
  `CANT_HORAS` int(11) NOT NULL,
  `DESCRIPCION` varchar(200) NOT NULL,
  `HORAS EXTRAS` int(11) NOT NULL,
  `OBSERVACIÓN` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `ID_ROL` int(11) NOT NULL,
  `ROL` varchar(60) NOT NULL,
  `PERMISOS` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleados`
--

CREATE TABLE `tipo_empleados` (
  `ID_TIPO` int(11) NOT NULL,
  `TIPO` varchar(60) DEFAULT NULL,
  `ID_ROL` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignacion`
--
ALTER TABLE `asignacion`
  ADD PRIMARY KEY (`ID_ASIG`),
  ADD KEY `ID_DEPTO` (`ID_DEPTO`),
  ADD KEY `ID_RUT` (`ID_RUT`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID_RUT`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`ID_DEPTO`),
  ADD KEY `ID_RUT` (`ID_RUT`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`ID_RUT`),
  ADD KEY `ID_ROL` (`ID_ROL`),
  ADD KEY `ID_TIPO` (`ID_TIPO`);

--
-- Indices de la tabla `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`ID_INFORME`),
  ADD KEY `ID_RUT` (`ID_RUT`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`ID_MODULO`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`ID_PROYECTO`);

--
-- Indices de la tabla `proyecto_emp`
--
ALTER TABLE `proyecto_emp`
  ADD PRIMARY KEY (`ID_PROYEMP`),
  ADD KEY `ID_PROYECTO` (`ID_PROYECTO`),
  ADD KEY `ID_TIPO` (`ID_TIPO`);

--
-- Indices de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`ID_REG_TIEMPO`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`ID_ROL`);

--
-- Indices de la tabla `tipo_empleados`
--
ALTER TABLE `tipo_empleados`
  ADD PRIMARY KEY (`ID_TIPO`),
  ADD KEY `ID_ROL` (`ID_ROL`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD CONSTRAINT `departamento_ibfk_1` FOREIGN KEY (`ID_RUT`) REFERENCES `empleados` (`ID_RUT`);

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`ID_ROL`) REFERENCES `roles` (`ID_ROL`),
  ADD CONSTRAINT `empleados_ibfk_2` FOREIGN KEY (`ID_TIPO`) REFERENCES `tipo_empleados` (`ID_TIPO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
