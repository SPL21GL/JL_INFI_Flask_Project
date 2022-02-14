create database if not exists businessApp;
use businessApp;


create table if not exists Arbeitsgruppe
(
ArbeitsgruppenID int auto_increment unique primary key,
Name varchar(64) not null,
Raum varchar(16) not null
)