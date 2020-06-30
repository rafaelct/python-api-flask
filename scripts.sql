create database store;

create table Auth (
	id serial primary key,
	loginname character varying(30) not null,
	password character varying(20) not null,
	fullname character varying(50),
	registration date not null,
	token character varying(200),
	lastRequest bigint);

create table Customers (
	id serial primary key,
	name character varying(30) not null,
	fullname character varying(50) not null,
	birth date not null,
	document character varying(11) not null,
	gender character varying(1) not null);

create table Products (
	id serial primary key,
	name character varying(200) not null,
	brand character varying(50) not null,
	Registration date not null,
	codProduct integer not null,
	linkImg character varying(500) not null,
	qtd integer not null);

create table Carts (
	id serial primary key,
	customerId integer not null,
	productId integer not null,
	registration date not null);

create table Orders (
	id serial primary key,
	customerId integer not null,
	productId integer not null,
	registration date not null,
	orderStatus character varying(200));