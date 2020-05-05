use VinylSqlShop1;
go

create or alter function validate(@param int)
returns int
as
begin
	declare @valid int = 1
	if (@param <= 0)
	begin
		set @valid = 0
	end
	return @valid
end
go

create or alter procedure crud_artist(@cantitate int)
as
begin
	if dbo.validate(@cantitate) = 0
	begin
		print('parametru invalid')
		return
	end
	else
	begin
		declare @id int
		declare @i int
		set @i = 1
		declare @Nume varchar(50)
		set @id = (select max(id) from Artist)
		set @id = 1
		if @id is null set @id = 1
		
		while @i <= @cantitate
		begin
			set @Nume = convert(varchar(50),'Artist' + convert(varchar(50),@id))
			set identity_insert Artist on
			insert into Artist(id,nume,Genre,Birthday,Studio)
			values(@id,@Nume,'Genre',getdate(),'studio')
			set identity_insert Artist off
			set @id = @id + 1
			set @i = @i + 1
		end

		select * from Artist

		update Artist set Nume = 'altNume'
		where id % 5 = 0

		delete from Artist where id % 2 = 0

		print 'Crud for Artist'
	end
end

exec crud_artist 20
select * from Artist
delete from Artist 
go

create or alter procedure crud_vinyl(@cantitate int)
as
begin
	if dbo.validate(@cantitate) = 0
	begin
		print('parametru invalid')
		return
	end
	else
	begin
		declare @id int
		declare @i int
		set @i = 1
		declare @Nume varchar(50)
		--set @id = (select max(IdVinyl) from Vinyl)
		set @id =  1
		--if @id is null set @id = 1
		
		while @i <= @cantitate
		begin
			set @Nume = convert(varchar(50),'Vinyl' + convert(varchar(50),@id))
			
			insert into Vinyl(IdVinyl,NameOf,Genre,Price,IdCrate)
			values(@id,@Nume,'Genre',12,1)
			
			set @id = @id + 1
			set @i = @i + 1
		end

		select * from Vinyl

		update Vinyl set NameOf = 'altNume'
		where IdVinyl % 5 = 0

		delete from Vinyl where IdVinyl % 2 = 0

		print 'Crud for Vinyl'
	end
end

exec crud_vinyl 20
select * from Vinyl
delete from Vinyl
go

create or alter procedure crud_crate(@cantitate int)
as
begin
	if dbo.validate(@cantitate) = 0
	begin
		print('parametru invalid')
		return
	end
	else
	begin
		declare @id int
		declare @i int
		set @i = 1
		declare @Nume varchar(50)
		--set @id = (select max(IdCrate) from Crate)
		set @id =  1
		--if @id is null set @id = 1
		
		while @i <= @cantitate
		begin
			set @Nume = convert(varchar(50),'Artist' + convert(varchar(50),@id))
			
			insert into Crate(IdCrate,IdShop)
			values(@id,1)
			
			set @id = @id + 1
			set @i = @i + 1
		end

		select * from Crate

		update Crate set IdShop = 3
		where IdCrate % 5 = 0

		delete from Crate where IdCrate % 2 = 0

		print 'Crud for Crate'
	end
end


exec crud_crate 10
select* from Crate
delete from Crate
go

create or alter procedure crud_shop(@cantitate int)
as
begin
	if dbo.validate(@cantitate) = 0
	begin
		print('parametru invalid')
		return
	end
	else
	begin
		declare @id int
		declare @i int
		set @i = 1
		declare @Adresa varchar(50)
		--set @id = (select max(IdShop) from Shop)
		set @id = 1
		--if @id is null set @id = 1
		
		while @i <= @cantitate
		begin
			set @Adresa = convert(varchar(50),'Adresa' + convert(varchar(50),@id))
			
			insert into Shop(IdShop,Adresa)
			values(@id,@Adresa)
			
			set @id = @id + 1
			set @i = @i + 1
		end

		select * from Shop

		update Shop set Adresa = 'altNume'
		where IdShop % 5 = 0

		delete from Shop where IdShop % 2 = 0

		print 'Crud for Artist'
	end
end

exec crud_shop 10
select * from Shop
delete from Shop
go

create or alter procedure crud_artistvinyl(@cantitate int)
as
begin
	if dbo.validate(@cantitate) = 0
	begin
		print('parametru invalid')
		return
	end
	else
	begin
		declare @id int
		declare @i int
		set @i = 1
		set @id = 1

		while @i <= @cantitate
		begin
			insert into ArtistVinyl(idArtist,idVinyl)
			values(@id,@id)
			
			set @id = @id + 2
			set @i = @i + 1
		end

		select * from ArtistVinyl

		update ArtistVinyl set idArtist = 1
		where idVinyl % 5 = 0

		delete from ArtistVinyl where idArtist % 2 = 0

		print 'Crud for ArtistVinyl'
	end
end

exec crud_artistvinyl 10
select * from ArtistVinyl
delete from ArtistVinyl
go

alter table Vinyl 
add constraint chk_Price check (Price >= 1)

alter table Artist
add constraint chk_birthday check (Birthday <= getdate())

if exists (select name from sys.indexes where name='N_idx_vinylsqlshop1_nameof')
drop index N_idx_vinylsqlshop1_nameof on Vinyl
create nonclustered index N_idx_vinylsqlshop1_nameof on Vinyl(NameOf)
go

create or alter view vw_vinyl
as
select * from Vinyl
where NameOf like 'V%'
go

exec crud_vinyl 50

select * from vw_vinyl
order by NameOf

delete from Vinyl

if exists (select name from sys.indexes where name='N_idx_vinylsqlshop_nume')
drop index N_idx_vinylsqlshop_nume on Artist
create nonclustered index N_idx_vinylsqlshop_nume on Artist(nume)
go

create or alter view vw_artist
as
select * from Artist
where nume like 'alt%'
go

exec crud_artist 50

select * from vw_artist
order by nume

delete from Artist