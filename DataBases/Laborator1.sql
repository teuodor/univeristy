
CREATE DATABASE	VinylSqlShop1

USE VinylSqlShop1;

CREATE TABLE Shop(
	IdShop int NOT NULL PRIMARY KEY,
	Adresa varchar(50)
)

CREATE TABLE Crate(
	IdCrate int NOT NULL PRIMARY KEY,
	IdShop int FOREIGN KEY REFERENCES Shop(IdShop)
)

CREATE TABLE Vinyl (
	IdVinyl int NOT NULL PRIMARY KEY,
	NameOf varchar(50),
	Genre varchar(50),
	Price int,
	IdCrate int FOREIGN KEY REFERENCES Crate(IdCrate)
)


CREATE TABLE Artist(
	Nume varchar(50) NOT NULL PRIMARY KEY,
	Genre varchar(50),
	Birthday date,
	Studio varchar(50)
)

CREATE TABLE ArtistVinyl(
	NumeArtist varchar(50) FOREIGN KEY REFERENCES Artist(Nume),
	IdVinyl int FOREIGN KEY REFERENCES Vinyl(IdVinyl),
	PRIMARY KEY(NumeArtist,IdVinyl)
)

CREATE TABLE Customer(
	IdCustomer int NOT NULL PRIMARY KEY,
	LastName varchar(50),
	FirstName varchar(50),
	IdCard int
)

CREATE TABLE Cards(
	IdCard int NOT NULL PRIMARY KEY,
	SerieCard int,
	IdCustomer int FOREIGN KEY REFERENCES Customer(IdCustomer)
)

CREATE TABLE Orders(
	IdOrder int NOT NULL PRIMARY KEY,
	DateOf date,
	Price int,
	IdCustomer int FOREIGN KEY REFERENCES Customer(IdCustomer)
)

CREATE TABLE OrdersVinyls(
	IdOrder int FOREIGN KEY REFERENCES Orders(IdOrder),
	IdVinyl int FOREIGN KEY REFERENCES Vinyl(IdVinyl),
	PRIMARY KEY(IdOrder,IdVinyl)
)

CREATE TABLE Rental(
	IdRental int NOT NULL PRIMARY KEY,
	DateOf date,
	IdVinyl int FOREIGN KEY REFERENCES Vinyl(IdVinyl),
	IdCustomer int FOREIGN KEY REFERENCES Customer(IdCustomer)
)

INSERT INTO Artist(Nume,Genre,Birthday,Studio)
VALUES ('Salut','Rock','12.08.2000','Salutare')

INSERT INTO Artist(Nume,Genre,Birthday,Studio)
VALUES ('Chris','Pop','1998-11-13','Incredibil')

INSERT INTO Artist(Nume,Genre,Birthday,Studio)
VALUES ('Mihai','Rock','1989-02-22','Sucevita Bucovina')

INSERT INTO Artist(Nume,Genre,Birthday,Studio)
VALUES ('Buna','Techno','1967-11-18','Salutare')

INSERT INTO Artist(Nume,Genre,Birthday,Studio)
VALUES ('Parizer','Manele','2000-08-12','Rock and roll')

INSERT INTO Shop(IdShop,Adresa)
VALUES (1,'Strada Uliului')

INSERT INTO Shop(IdShop,Adresa)
VALUES (2,'Strada Turcului 13')

INSERT INTO Shop(IdShop,Adresa)
VALUES (3,'Strada General 12')

INSERT INTO Crate(IdCrate,IdShop)
VALUES(1,1)

INSERT INTO Crate(IdCrate,IdShop)
VALUES(2,1)

INSERT INTO Crate(IdCrate,IdShop)
VALUES(3,1)

INSERT INTO Crate(IdCrate,IdShop)
VALUES(4,2)

INSERT INTO Crate(IdCrate,IdShop)
VALUES(5,2)

INSERT INTO Crate(IdCrate,IdShop)
VALUES(6,3)

INSERT INTO Crate(IdCrate,IdShop)
VALUES(7,3)

INSERT INTO Vinyl(IdVinyl, NameOf, Genre, Price, IdCrate)
VALUES(1, 'Undeva in Carpati' , 'Rap', 80, 1)


Select *
from Crate