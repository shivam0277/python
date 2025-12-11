-- There are several relational database software packages. Some are free and open source, while others are paid 
-- and proprietary. Here some popular relational database distributions:
-- MySQL
-- Postgres
-- SQLite
-- Microsoft SQL Server
-- MariaDB
-- Oracle
-- IBM DB2


-- There are three types of SQL statements:

-- 1. Data Definition Language(DDL):
-- The Data Definition Language contains commands that are less frequently used. DDL commands modify the actual structure of a database, rather than the database’s contents. example:
-- Generating a table
-- Modifying a structure of a table (altering)

-- 2. Data Control Language(DCL):
-- The Data Control Language allows you to manipulate and manage user access rights on database objects. It consists of two commands:
-- the GRANT command, used to add database permissions for a user,
-- and the REVOKE command, used to remove existing permissions.
-- These two commands form the core of the relational database security model.

-- 3. Data Manipulation Language (DML):
-- Data Manipulation Language contains the subset of SQL commands used most frequently. It is used for searching, inserting, updating, and deleting data that we will see in this notebook.

-- SQL is case insensitive. You can type statements in upper case, lowercase or a mixture of both
-- Database names can be typed with or without backquotes i.e. classicmodels or `classicmodels`
-- SQL statement can span over multiple lines and must end with a semicolon ;


show databases; 
-- This SQL command lists all the databases available on the SQL server.

CREATE DATABASE classicmodels;
-- This SQL command creates a new database named classicmodels.
USE classicmodels;
-- This SQL command selects the classicmodels database to be used for subsequent operations.

-- CREATE DATABASE IF NOT EXISTS classicmodels1;

-- DROP DATABASE classicmodels1;
-- This SQL command deletes the classicmodels1 database if it exists.

DROP TABLE IF EXISTS offices;
-- This SQL command deletes the offices table if it exists.

CREATE TABLE offices (
  officeCode varchar(10) NOT NULL,
  city varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50),
  state varchar(50),
  country varchar(50) NOT NULL,
  postalCode varchar(15) NOT NULL,
  territory varchar(10) NOT NULL,
  PRIMARY KEY (officeCode)
);

-- This SQL command creates a new table named offices with specified columns and their data types.