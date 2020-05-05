alter procedure update1
as
alter table Cards
	alter column SerieCard varchar(50)
	print 'done update1' + char(13)
go

alter procedure down1
as
alter table Cards
	alter column SerieCard int
	print 'done down1' + char(13)
go

alter procedure update2
as
alter table Orders
	add constraint con_DateOf
	default GETDATE() for DateOf
	print 'done update2' + char(13)
go

alter procedure down2
as
alter table Orders
	drop constraint con_DateOf
	print 'done down2' + char(13)
go

alter procedure update3
as
create table Mall(
	id int primary key,
	nume varchar(30),
	adresa varchar (50),
	idshop int
)
print 'done update3' + char(13)
go

alter procedure down3
as
drop table Mall
print 'done down3' + char(13)
go

alter procedure update4
as
alter table Mall
	add constraint fk_adresa foreign key(idshop) references Shop(IdShop)
print 'done update4' + char(13)
go

alter procedure down4
as
alter table Mall
	drop constraint fk_adresa
print 'done down4' + char(13)
go


alter procedure update5
as
alter table Cards
	add CuloareCard varchar(30)
print 'done update5' + char(13)
go

alter procedure down5
as
alter table Cards
	drop column CuloareCard
print 'done down5' + char(13)
go


create table Version( current_version int )
set current_version = 5 from Version
go

alter procedure setVersion
@version int as
begin
	if @version < 0 or  @version > 5
		print 'There is no such verison'
	else
		begin
			declare @current_version int
			declare @proc_name nvarchar(50)
			set @current_version = (select current_version from Version);

			while @current_version < @version
			begin
					set @current_version = @current_version + 1
					set @proc_name = 'update' + convert(nvarchar(50),@current_version)
					print @proc_name
					execute @proc_name
			end

			while @current_version > @version - 1
			begin
				set @proc_name = 'down' + convert(nvarchar(50),@current_version)
				print @proc_name
				if @current_version != 0
				begin
					execute @proc_name
				end
				set @current_version = @current_version - 1
			end

			update Version set current_version = @version

		end

end;
go

execute setVersion @version = 5
go

execute down1