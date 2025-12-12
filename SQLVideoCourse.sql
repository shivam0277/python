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

INSERT INTO offices
(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) VALUES 

(1,'San Francisco','+1 650 219 4782','100 Market Street','Suite 300','CA','USA','94080','NA'),
(2,'Boston','+1 215 837 0825','1550 Court Place','Suite 102','MA','USA','02107','NA'),
(3,'NYC','+1 212 555 3000','523 East 53rd Street','apt. 5A','NY','USA','10022','NA');

select officeCode, city from offices;
--This SQL command retrieves the officeCode and city columns from the offices table.


-- EXERCISES:
-- Add some more entires into the offices table, using just the required (NOT NULL) columns.
-- Explore what happens if you don't provide a value for a column marked as not null.
-- Try adding an entry with a primary key matching the an existing entry.
-- Retrieve and display just the city and phone number information for each office.


DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
  employeeNumber int(11) NOT NULL,
  lastName varchar(50) NOT NULL,
  firstName varchar(50) NOT NULL,
  extension varchar(10) NOT NULL,
  email varchar(100) NOT NULL,
  officeCode varchar(10) NOT NULL,
  reportsTo int(11) DEFAULT NULL,
  jobTitle varchar(50) NOT NULL,
  PRIMARY KEY (employeeNumber),
  FOREIGN KEY (reportsTo) REFERENCES employees (employeeNumber),
  FOREIGN KEY (officeCode) REFERENCES offices (officeCode)
);


INSERT INTO employees VALUES
(1002,'Murphy','Diane','x5800','dmurphy@classicmodelcars.com','1',NULL,'President'),
(1056,'Patterson','Mary','x4611','mpatterso@classicmodelcars.com','1',1002,'VP Sales'),
(1076,'Firrelli','Jeff','x9273','jfirrelli@classicmodelcars.com','1',1002,'VP Marketing'),
(1088,'Patterson','William','x4871','wpatterson@classicmodelcars.com','6',1056,'Sales Manager (APAC)'),
(1102,'Bondur','Gerard','x5408','gbondur@classicmodelcars.com','4',1056,'Sale Manager (EMEA)'),
(1143,'Bow','Anthony','x5428','abow@classicmodelcars.com','1',1056,'Sales Manager (NA)'),
(1165,'Jennings','Leslie','x3291','ljennings@classicmodelcars.com','1',1143,'Sales Rep'),
(1166,'Thompson','Leslie','x4065','lthompson@classicmodelcars.com','1',1143,'Sales Rep'),
(1188,'Firrelli','Julie','x2173','jfirrelli@classicmodelcars.com','2',1143,'Sales Rep'),
(1216,'Patterson','Steve','x4334','spatterson@classicmodelcars.com','2',1143,'Sales Rep'),
(1286,'Tseng','Foon Yue','x2248','ftseng@classicmodelcars.com','3',1143,'Sales Rep');


-- EXERCISES:
-- Try inserting an entry into employees with an invalid value for officeCode.
-- Try inserting an entry into employees with an invalid value for reportsTo.
-- Create a new office location and add some employees for the new location.