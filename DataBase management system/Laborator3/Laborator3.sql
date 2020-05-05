create or alter procedure InsertAVTrans @name varchar(50), @studio varchar(50),
@nameVinyl varchar(50), @genre varchar(50), @price varchar(50), @idCrate varchar(50)
as
	begin tran
	declare @idArtist int
	declare @idVinyl int
	declare @priceInt int
	declare @idCrateInt int
	declare @ok bit
	set @ok = 1
	
	if (select ISNUMERIC(@price)) = 1
		set @priceInt = CONVERT(int, @price)
	else
		set @priceInt = null;

	if (select ISNUMERIC(@idCrate)) = 1
		set @idCrateInt = CONVERT(int, @idCrate)
	else
		set @idCrateInt = null;

	save tran saveArtist
	
	begin try

		insert into Artist (Name, Studio) values (@name, @studio)
		
		if len(@name) <= 3
			set @name = null

		if len(@studio) <= 3
			set @studio = null

		insert into [dbo].[Log] (Descriere, Moment) values ('S-a adaugat artistul ' + @name + ' ' + @studio, GETDATE())

		set @idArtist = (select max(ID) from Artist)
	end try
	begin catch
		set @ok = 0
		rollback tran saveArtist
		if @name is null
			set @name = 'Invalid'
		if @studio is null
			set @studio = 'Invalid'
		insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat artistul ' + @name + ' ' + @studio, GETDATE())
	end catch

	save tran saveVinyl
	begin try
		
		insert into Vinyl (Name, Genre, Price, IDCrate) values (@nameVinyl, @genre, @priceInt, @idCrateInt)
		
		if len(@nameVinyl) <= 3
			set @nameVinyl = null
	
		if len(@genre) < 3
			set @genre = null

		if @idCrateInt < 0 or @idCrateInt > 6
		begin
			set @idCrateInt = null
			RAISERROR('error id',16,1)
		end
		
		if @priceInt < 0 
		begin
			set @priceInt = null;
			RAISERROR('error price',16,1)
		end
		
		insert into [dbo].[Log] (Descriere, Moment) values ('S-a adaugat vinilul ' + @nameVinyl + ' ' + @genre + convert(varchar(10), @priceInt), GETDATE())
	
		set @idVinyl = (select max(ID) from Vinyl)
	end try
	begin catch
		set @ok = 0
		rollback tran saveVinyl
		if @nameVinyl is null
			set @nameVinyl = 'Invalid'
		if @genre is null
			set @genre = 'Invalid'
		if @priceInt is null
			set @priceInt = 0
		insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat vinilul ' + @nameVinyl + ' ' + @genre + convert(varchar(10), @priceInt), GETDATE())
	end catch

	save tran saveAV
	if @ok = 1
	begin
		begin try
			
			insert into ArtistVinyl values (@idVinyl, @idArtist)
			insert into [dbo].[Log] (Descriere, Moment) values ('S-a adaugat in ArtistVinyl ' + convert(varchar(50), @idVinyl) + ' ' + convert(varchar(50), @idArtist), GETDATE())
		end try
		begin catch
			rollback tran saveAV
			if @idVinyl is null
				set @idVinyl = 0
			if @idArtist is null
				set @idArtist = 0

			insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat in ArtistVinyl ' + convert(varchar(50), @idVinyl) + ' ' + convert(varchar(50), @idArtist), GETDATE())
		end catch
	end
	else
		insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat in ArtistVinyl ', GETDATE())
	commit tran
go

execute InsertAVTrans Mihai, Solcan, Salut, Rock,  13, 1
execute InsertAVTrans Mi, Solcan, Salut, Rock,  13, 1
execute InsertAVTrans Mihai, Solcan, Salut, Rock,  abc, 1
execute InsertAVTrans Mi, Solcan, Salut, Rock,  abc, 1



select * from Vinyl
select * from Artist
select * from ArtistVinyl

select * from Log

go

create or alter procedure InsertAVTrans6 @name varchar(50), @studio varchar(50),
@nameVinyl varchar(50), @genre varchar(50), @price varchar(50), @idCrate varchar(50)
as
	begin tran
	save tran insertAV

	declare @idArtist int
	declare @idVinyl int
	declare @priceInt int
	declare @idCrateInt int
	declare @ok bit

	set @ok = 1
	if len(@name) <= 3
		set @name = null
	if len(@nameVinyl) <= 3
		set @nameVinyl = null
	if len(@studio) <= 3
		set @studio = null
	if len(@genre) < 3
		set @genre = null
	if (select isnumeric(@price)) = 1
	begin
		set @priceInt = CONVERT(int, @price)
		if @priceInt< 0 
			set @priceInt = null
	end
	else
		set @priceInt = null
	if (select ISNUMERIC(@idCrate)) = 1
	begin
		set @idCrateInt = CONVERT(int, @idCrate)
		if @idCrateInt < 0 or @idCrateInt > 6
			set @idCrateInt = null
	end
	else
		set @idCrateInt = null
	
	begin try

		insert into Artist (Name, Studio) values (@name, @studio)

		set @idArtist = (select max(ID) from Artist)
		insert into [dbo].[Log] (Descriere, Moment) values ('S-a adaugat artistul ' + @name + ' ' + @studio, GETDATE())

		insert into Vinyl (Name, Genre, Price, IDCrate) values (@nameVinyl, @genre, @priceInt, @idCrateInt)

		set @idVinyl = (select max(ID) from Vinyl)
		insert into [dbo].[Log] (Descriere, Moment) values ('S-a adaugat vinilul ' + @nameVinyl + ' ' + @genre + convert(varchar(10), @priceInt), GETDATE())
		
		insert into ArtistVinyl values (@idVinyl, @idArtist)
		insert into [dbo].[Log] (Descriere, Moment) values ('S-a adaugat in ArtistVinyl ' + convert(varchar(50), @idVinyl) + ' ' + convert(varchar(50), @idArtist), GETDATE())
	
	end try
	begin catch
		set @ok = 0
		rollback tran insertAV
		if @name is null
			set @name = 'Invalid'
		if @studio is null
			set @studio = 'Invalid'
		insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat artistul ' + @name + ' ' + @studio, GETDATE())

		if @nameVinyl is null
			set @nameVinyl = 'Invalid'
		if @genre is null
			set @genre = 'Invalid'
		if @priceInt is null
			set @priceInt = 0
		insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat vinilul ' + @nameVinyl + ' ' + @genre + convert(varchar(10), @priceInt), GETDATE())

		if @idVinyl is null
			set @idVinyl = 0
		if @idArtist is null
			set @idArtist = 0

		insert into [dbo].[Log] (Descriere, Moment) values ('Nu s-a adaugat in ArtistVinyl ' + convert(varchar(50), @idVinyl) + ' ' + convert(varchar(50), @idArtist), GETDATE())
	end catch

	commit tran
go

execute InsertAVTrans6 Mihai, Solcan, Salut, Rock,  13, 1
execute InsertAVTrans6 Mi, Solcan, Salut, Rock,  13, 1
execute InsertAVTrans6 Mihai, Solcan, Salut, Rock,  abc, 1
execute InsertAVTrans6 Mi, Solcan, Salut, Rock,  abc, 1


delete from Log

