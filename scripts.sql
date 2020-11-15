create database store;

\c store


--select * from Orders;
drop table Auth;
drop table Orders;
drop table Carts;
drop table Products;
drop table Customers;

create table Auth (
	id serial primary key,
	loginname character varying(30) not null UNIQUE,
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
	codProduct integer not null UNIQUE,
	linkImg character varying(500) not null,
	qtd integer not null,
	price money not null);

create table Carts (
	id serial primary key,
	customerId integer not null,
	productId integer not null,
	registration date not null,
	FOREIGN KEY (customerId) REFERENCES Customers (id),
	FOREIGN KEY (productId) REFERENCES Products (id));

create table Orders (
	id serial primary key,
	customerId integer not null,
	productId integer not null,
	registration date not null,
	orderStatus character varying(200),
	FOREIGN KEY (customerId) REFERENCES Customers (id),
	FOREIGN KEY (productId) REFERENCES Products (id));

