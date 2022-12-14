USE [master]
GO
/****** Object:  Database [scraping]    Script Date: 12/11/2022 22:43:54 ******/
CREATE DATABASE [scraping]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'scraping', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\scraping.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'scraping_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\scraping_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [scraping] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [scraping].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [scraping] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [scraping] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [scraping] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [scraping] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [scraping] SET ARITHABORT OFF 
GO
ALTER DATABASE [scraping] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [scraping] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [scraping] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [scraping] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [scraping] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [scraping] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [scraping] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [scraping] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [scraping] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [scraping] SET  ENABLE_BROKER 
GO
ALTER DATABASE [scraping] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [scraping] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [scraping] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [scraping] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [scraping] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [scraping] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [scraping] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [scraping] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [scraping] SET  MULTI_USER 
GO
ALTER DATABASE [scraping] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [scraping] SET DB_CHAINING OFF 
GO
ALTER DATABASE [scraping] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [scraping] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [scraping] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [scraping] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [scraping] SET QUERY_STORE = OFF
GO
USE [scraping]
GO
/****** Object:  Table [dbo].[inflacion]    Script Date: 12/11/2022 22:43:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[inflacion](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[fecha] [varchar](50) NULL,
	[porcentaje] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ventas]    Script Date: 12/11/2022 22:43:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ventas](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[indice_tiempo] [varchar](255) NOT NULL,
	[ventas_precios_corrientes] [float] NULL,
	[ventas_precios_constantes] [float] NULL,
	[ventas_totales_canal_venta] [float] NULL,
	[salon_ventas] [float] NULL,
	[canales_on_line] [float] NULL,
	[ventas_totales_medio_pago] [float] NULL,
	[efectivo] [float] NULL,
	[tarjetas_debito] [float] NULL,
	[tarjetas_credito] [float] NULL,
	[otros_medios] [float] NULL,
	[ventas_totales_grupo_articulos] [float] NULL,
	[subtotal_ventas_alimentos_bebidas] [float] NULL,
	[bebidas] [float] NULL,
	[almacen] [float] NULL,
	[panaderia] [float] NULL,
	[lacteos] [float] NULL,
	[carnes] [float] NULL,
	[verduleria_fruteria] [float] NULL,
	[alimentos_preparados_rotiseria] [float] NULL,
	[articulos_limpieza_perfumeria] [float] NULL,
	[indumentaria_calzado_textiles_hogar] [float] NULL,
	[electronicos_articulos_hogar] [float] NULL,
	[otros] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [scraping] SET  READ_WRITE 
GO
