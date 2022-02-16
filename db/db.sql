create database if not exists businessApp;
use businessApp;


create table if not exists Arbeitsgruppe
(
ArbeitsgruppenID int auto_increment unique primary key,
Name varchar(64) not null,
Raum int not null
)

create table if not exists Abteilung
(
AbteilungsID int auto_increment unique primary key,
Name varchar(64) not null,
Gebäude int not null
)
create table if not exists Mitarbeiter
(
MitarbeiterID int auto_increment unique primary key,
Voname varchar(32) not null,
Nachname varchar(32),
Lohn int not null,
Adresse varchar(64),
Beschäftigung varchar(64),
Geburtsdatum date
)
create table if not exists Arbeitsgruppe_Mitarbeiter
(
 Arbeitsgruppe_MitarbeiterID int auto_increment unique primary key
)
alter table Arbeitsgruppe_Mitarbeiter
add FOREIGN KEY (ArbeitsgruppenID) REFERENCES Arbeitsgruppe(ArbeitsgruppenID),
FOREIGN KEY (MitarbeiterID) REFERENCES Mitarbeiter(MitarbeiterID)

alter table Mitarbeiter
add FOREIGN KEY (ArbeitsgruppenID) REFERENCES Arbeitsgruppe_Mitarbeiter(ArbeitsgruppenID)

alter table Arbeitsgruppe
add FOREIGN KEY (AbteilungsID) REFERENCES Arbeitsgruppe_Mitarbeiter(AbteilungsID)