---inserare tabela Tables---
insert into Tables(Name) Values
('Artist'),
('ArtistVinyl'),
('Vinyl')
go

---creare View-uri---
create or alter view ViewArtist
as
select Nume, Genre, Studio
from Artist
go

create or alter view ViewVinyl
as
select V.NameOf, S.Adresa
from Shop S
inner join Crate C on C.IdShop = S.IdShop
inner join Vinyl V on V.IdCrate = C.IdCrate
go

create or alter view ViewArtistVinyl
as
select A.Genre, COUNT(A.Nume) as NrOfArtists
from Artist A
inner join ArtistVinyl AV on AV.NumeArtist = A.Nume
inner join Vinyl V on V.IdVinyl = AV.IdVinyl
group by A.Genre
go

---inserare tabela Views---
insert into Views values
('ViewArtist'),
('ViewVinyl'),
('ViewArtistVinyl')
go


---inserare tabela Tests---
insert into Tests values
('Inserare10'),
('Inserare100'),
('Inserare1000'),
('Sterge10'),
('Sterge100'),
('Sterge1000'),
('Evaluare')
go


---inserare tabela TestTables---
insert into TestTables values
(1,1,10,1),
(2,1,100,1),
(3,1,1000,1),
(1,2,10,2),
(2,2,100,2),
(3,2,1000,2),
(1,3,10,3),
(2,3,100,3),
(3,3,1000,3),

(4,1,10,3),
(5,1,100,3),
(6,1,1000,3),
(4,2,10,2),
(5,2,100,2),
(6,2,1000,2),
(4,3,10,1),
(5,3,100,1),
(6,3,1000,1)
go

---inserare TestViews---
insert into TestViews values
(7,1),
(7,2),
(7,3)
go


---inserare in tabela Artist---
create or alter procedure InsertArtist (@rows int)
as
begin
	declare @final varchar(50) 
	declare @name varchar(50)
	declare @genre varchar(50)
	declare @birthday date
	declare @studio varchar(50)
	declare @i int
	declare @genreG varchar(50)

	set @final = 'NumeArtist'
	set @genre = 'Genre'
	set @studio = 'Studio'
	set @birthday = GETDATE()
	set @i = 1

	while @i <= @rows
	begin
		set @name = @final + convert(varchar(50),@i)
		set @genreG = @genre + convert(varchar(50), floor(rand()*(10-5 + 1) + 5))
		insert into Artist values (@name,@genreG,@birthday,@studio)
		set @i = @i + 1
	end

end
go


---stergere din tabela Artist---
create or alter procedure DeleteArtist(@rows int)
as
begin
	declare @final varchar(50)
	declare @i int
	declare @name varchar(50)

	set @i = @rows
	set @final = 'NumeArtist'
	
	while @i > 0
	begin
		set @name = @final + convert(varchar(50),@i)
		delete from Artist where Artist.Nume = @name
		set @i = @i - 1

	end
	
end
go


---inserare in tabela Vinyl---
create or alter procedure InsertVinyl(@rows int)
as
begin
	declare @id int
	declare @name varchar(50)
	declare @genre varchar(50)
	declare @final varchar(50)
	declare @price int
	declare @idCrate int
	declare @i int

	set @name = 'NumeVinyl'
	set @final = 'Genre'
	set @price = 100
	set @idCrate = 1
	set @i = 1
	
	while @i <= @rows
	begin
		set @id = 1000 + @i
		set @genre = @final + convert(varchar(50), floor(rand()*(10-5 + 1) + 5))
		insert into Vinyl values (@id,@name,@genre,@price,@idCrate)
		set @i = @i + 1
	end

end

go

---stergere din tabela Vinyl---
create or alter procedure DeleteVinyl(@rows int)
as
begin 
	declare @id int
	declare @i int

	set @i = @rows

	while @i > 0
	begin
		set @id = 1000 + @i
		delete from Vinyl where Vinyl.IdVinyl = @id
		set @i = @i - 1
	
	end

end 

go

---inserare tabela ArtistVinyl---
create or alter procedure InsertArtistVinyl(@rows int)
as
begin
	declare @idV int
	declare @nume varchar(50)
	declare @final varchar(50)
	declare @i int

	set @i = 1
	set @final = 'NumeArtist'
	
	while @i <= @rows
	begin
		set @nume = @final + convert(varchar(50), @i)
		set @idV = 1000 + @i
		insert into ArtistVinyl values (@nume,@idV)
		set @i = @i + 1
	end

end

go

---stergere tabela ArtistVinyl---
create or alter procedure DeleteArtistVinyl(@rows int)
as
begin
	declare @idV int
	declare @i int
	set @i = @rows
	while @i > 0
	begin
		set @idV = 1000 + @i
		delete from ArtistVinyl where ArtistVinyl.IdVinyl = @idV
		set @i = @i - 1

	end
	
end

go

---Inserari si stergeri---
create or alter procedure Inserare10(@Tabela varchar(50))
as
begin
	if @Tabela = 'Vinyl'
		exec InsertVinyl 10
	if @Tabela = 'Artist'
		exec InsertArtist 10
	if @Tabela = 'ArtistVinyl'
		exec InsertArtistVinyl 10
	else
		print 'nume invalid'
end
go

create or alter procedure Inserare100(@Tabela varchar(50))
as
begin
	if @Tabela = 'Vinyl'
		exec InsertVinyl 100
	if @Tabela = 'Artist'
		exec InsertArtist 100
	if @Tabela = 'ArtistVinyl'
		exec InsertArtistVinyl 100
	else
		print 'nume invalid'
end
go

create or alter procedure Inserare1000(@Tabela varchar(50))
as
begin
	if @Tabela = 'Vinyl'
		exec InsertVinyl 1000
	if @Tabela = 'Artist'
		exec InsertArtist 1000
	if @Tabela = 'ArtistVinyl'
		exec InsertArtistVinyl 1000
	else
		print 'nume invalid'
end
go

create or alter procedure Delete10(@Tabela varchar(50))
as
begin
	if @Tabela = 'Vinyl'
		exec DeleteVinyl 10
	if @Tabela = 'Artist'
		exec DeleteArtist 10
	if @Tabela = 'ArtistVinyl'
		exec DeleteArtistVinyl 10
	else
		print 'nume invalid'
end
go

create or alter procedure Delete100(@Tabela varchar(50))
as
begin
	if @Tabela = 'Vinyl'
		exec DeleteVinyl 100
	if @Tabela = 'Artist'
		exec DeleteArtist 100
	if @Tabela = 'ArtistVinyl'
		exec DeleteArtistVinyl 100
	else
		print 'nume invalid'
end
go


create or alter procedure Delete1000(@Tabela varchar(50))
as
begin
	if @Tabela = 'Vinyl'
		exec DeleteVinyl 1000
	if @Tabela = 'Artist'
		exec DeleteArtist 1000
	if @Tabela = 'ArtistVinyl'
		exec DeleteArtistVinyl 1000
	else
		print 'nume invalid'
end
go


create or alter procedure Evaluare(@Tabela varchar(50))
as
begin 
	if @Tabela = 'Artist'
		select * from ViewArtist
	if @Tabela = 'Vinyl'
		select * from ViewVinyl
	if @Tabela = 'ArtistVinyl'
		select * from ViewArtistVinyl
	else
		print 'nume invalid'

end

go
---mainu---
create or alter procedure main(@Tabela varchar(50), @nrRows int)
as 
begin 
	declare @t1 datetime
	declare @t2 datetime
	declare @t3 datetime
	declare @desc varchar(50)
	declare @inserare varchar(50)

	set @inserare = 'Inserare' + convert(varchar(50),@nrRows)

	declare @testInserare varchar(50)
	
	if @Tabela = 'Artist'
	begin
		set @t1 = GETDATE()
		exec @inserare 'Artist'
		set @t2 = GETDATE()
		exec Evaluare 'Artist'
		set @t3 = GETDATE()
		set @desc = 'Testul s-a facut pe tabela Artist'
		insert into TestRuns (Description,StartAt,EndAt) values (@desc,@t1,@t3)
		insert into TestRunTables(TableID,StartAt,EndAt) values (1,@t1,@t2)
		insert into TestRunViews(ViewID,StartAt,EndAt) values (1,@t2,@t3)
	end
	if @Tabela = 'Vinyl'
	begin
		set @t1 = GETDATE()
		exec @inserare 'Vinyl'
		set @t2 = GETDATE()
		exec Evaluare 'Vinyl'
		set @t3 = GETDATE()
		set @desc = 'Testul s-a facut pe tabela Vinyl'
		insert into TestRuns (Description,StartAt,EndAt) values (@desc,@t1,@t3)
		insert into TestRunTables(TableID,StartAt,EndAt) values (2,@t1,@t2)
		insert into TestRunViews(ViewID,StartAt,EndAt) values (2,@t2,@t3)
	end
	if @Tabela = 'ArtistVinyl'
	begin
		set @t1 = GETDATE()
		exec @inserare 'ArtistVinyl'
		set @t2 = GETDATE()
		exec Evaluare 'ArtistVinyl'
		set @t3 = GETDATE()
		set @desc = 'Testul s-a facut pe tabela ArtistVinyl'
		insert into TestRuns (Description,StartAt,EndAt) values (@desc,@t1,@t3)
		insert into TestRunTables(TableID,StartAt,EndAt) values (3,@t1,@t2)
		insert into TestRunViews(ViewID,StartAt,EndAt) values (3,@t2,@t3)
	end
	else
	print 'Tabela invalida'
end

go

exec main Artist, 1000
exec main Vinyl, 1000
exec main ArtistVinyl, 1000

select * from TestRuns
select * from TestRunTables
select * from TestRunViews

exec Delete1000 ArtistVinyl
exec Delete1000 Artist
exec Delete1000 Vinyl


delete from TestRuns
delete from TestRunTables
delete from TestRunViews