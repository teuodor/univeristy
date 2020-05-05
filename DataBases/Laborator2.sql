Insert into Vinyl(IdVinyl,NameOf,Genre,Price,IdCrate)
Values (2,'Wroom Wroom','Trap',100,1);

Insert into Vinyl(IdVinyl,NameOf,Genre,Price,IdCrate)
Values (3,'Richie Rich','Trap',100,1);

Insert into Vinyl(IdVinyl,NameOf,Genre,Price,IdCrate)
Values (4,'Enter Sandman','Rock',70,2);

Insert into Vinyl(IdVinyl,NameOf,Genre,Price,IdCrate)
Values (5,'Californication','Rock',60,2);

Insert into Vinyl(IdVinyl,NameOf,Genre,Price,IdCrate)
Values (6,'Meds','Rock',65,1);

--1interogare : where + > 2 tabele + m-n
SELECT V.NameOf, A.Nume, V.Genre
FROM ArtistVinyl AV
INNER JOIN Vinyl V on AV.IdVinyl = V.IdVinyl
INNER JOIN Artist A on AV.NumeArtist = A.Nume
WHERE V.Genre = 'Minimal'

--2interogare : distinct + > 2 tabele + m-n
SELECT DISTINCT V.Genre
FROM ArtistVinyl AV
INNER JOIN Vinyl V on AV.IdVinyl = V.IdVinyl
INNER JOIN Artist A on AV.NumeArtist = A.Nume
WHERE A.Birthday > '2000-01-01'
ORDER BY V.Genre DESC

--3interogare : distinct + where
SELECT DISTINCT V.Genre
FROM Vinyl V
WHERE V.Price < 50

--4interogare : group by + having
SELECT COUNT(Vinyl.NameOf), Vinyl.Genre
FROM Vinyl
GROUP BY Vinyl.Genre
HAVING COUNT(Vinyl.NameOf) > 3

--5interogare : group by + having + >= 2 tabele
SELECT COUNT(C.IdShop) AS NumberOfCrates, S.Adresa
FROM Shop S
INNER JOIN Crate C ON C.IdShop = S.IdShop 
GROUP BY S.Adresa
HAVING COUNT(C.IdShop) < 3

--6interogare : where + > 2 tabele
SELECT *, R.IdVinyl , V.NameOf
FROM Customer C
INNER JOIN Rental R on R.IdCustomer = C.IdCustomer
INNER JOIN Vinyl V ON V.IdVinyl = R.IdVinyl
WHERE C.IdCustomer > 1

--7interogare group by + > 2 tabele
SELECT O.DateOf, MIN(V.Price)
FROM Orders O
LEFT OUTER JOIN OrdersVinyls OV on O.IdOrder = OV.IdOrder
RIGHT OUTER JOIN Vinyl V ON V.IdVinyl = OV.IdVinyl
GROUP BY O.DateOf

--8interogare : where + > 2 tabele
SELECT Cards.SerieCard, C.FirstName
FROM Cards
INNER JOIN Customer C ON Cards.IdCustomer = C.IdCustomer
WHERE C.FirstName LIKE 'T%'

--9interogare : where + > 2 tabele
SELECT C.FirstName, Cards.SerieCard, R.DateOf
FROM Customer C
INNER JOIN Cards ON Cards.IdCustomer = C.IdCustomer
INNER JOIN Rental R ON R.IdCustomer = C.IdCustomer
ORDER BY C.FirstName ASC

--10interogare group by + > 2 tabele
SELECT COUNT(V.Genre) AS numGenres, Cards.SerieCard
FROM Vinyl V
INNER JOIN Rental R ON V.IdVinyl = R.IdVinyl
INNER JOIN Customer C ON R.IdCustomer = C.IdCustomer
INNER JOIN Cards ON Cards.IdCustomer = C.IdCustomer
GROUP BY Cards.SerieCard
