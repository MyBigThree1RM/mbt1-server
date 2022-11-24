set sql_safe_updates=0;

create database IF NOT EXISTS mbt1;
use mbt1;
alter database mbt1 default character set utf8mb4;

set foreign_key_checks = 0;
drop table IF EXISTS User cascade; 
drop table IF EXISTS Center cascade;
drop table IF EXISTS Record cascade;  
drop table IF EXISTS Challenge cascade; 
set foreign_key_checks = 1;


create table Center (
CCODE INT NOT NULL,
Cname varchar(20) NOT NULL,
lat DOUBLE NULL,
lon DOUBLE NULL,
primary key(CCODE));


create table User (
UID varchar(20) NOT NULL,
UPW varchar(20) NOT NULL,
primary key(UID));
    

create table Record (
REvent varchar(10) NOT NULL,
RDate varchar(10) NOT NULL,
R1rm INT default 0,
UID varchar(10) NOT NULL,
primary key(REvent, RDate, UID),
foreign key (UID) references User(UID));

create table Challenge (
CEvent varchar(10) NOT NULL,
CWeight INT default 0,
UID varchar(10) NOT NULL,
CCODE INT NOT NULL,
primary key(CEvent, UID, CCODE),
foreign key (UID) references User(UID),
foreign key (CCODE) references Center(CCODE));



insert into Center
values(1, 'T GYM', 37.550117, 126.924654);
insert into Center
values(2, 'R GYM', 37.552609, 126.924997);
insert into Center
values(3, 'G GYM', 37.551317, 126.926260);
insert into Center
values(4, 'I GYM', 37.551502, 126.927278);
insert into Center
values(5, 'C GYM', 37.549186, 126.926041);
insert into Center
values(6, 'U GYM', 37.550209, 126.926487);


insert into User
values('kms', '1234');
insert into User
values('psy', '1234');
insert into User
values('kim', '1234');
insert into User
values('park', '1234');
insert into User
values('lee', '1234');

insert into Record
values('Squat', '22-11-23', 0, 'kim');
insert into Record
values('BenchPress', '22-11-23', 0, 'kim');
insert into Record
values('Deadlift', '22-11-23', 0, 'kim');

insert into Record
values('Squat', '22-11-23', 0, 'lee');
insert into Record
values('BenchPress', '22-11-23', 0, 'lee');
insert into Record
values('Deadlift', '22-11-23', 0, 'lee');

insert into Record
values('Squat', '22-11-23', 0, 'park');
insert into Record
values('BenchPress', '22-11-23', 0, 'park');
insert into Record
values('Deadlift', '22-11-23', 0, 'park');

insert into Record
values('Squat', '22-11-01', 80, 'kms');
insert into Record
values('Squat', '22-11-02', 60, 'kms');
insert into Record
values('Squat', '22-11-03', 70, 'kms');
insert into Record
values('Squat', '22-11-05', 90, 'kms');

insert into Record
values('BenchPress', '22-11-01', 60, 'kms');
insert into Record
values('BenchPress', '22-11-02', 80, 'kms');
insert into Record
values('BenchPress', '22-11-03', 100, 'kms');
insert into Record
values('BenchPress', '22-11-05', 80, 'kms');

insert into Record
values('Deadlift', '22-11-01', 100, 'kms');
insert into Record
values('Deadlift', '22-11-02', 110, 'kms');
insert into Record
values('Deadlift', '22-11-03', 100, 'kms');
insert into Record
values('Deadlift', '22-11-05', 110, 'kms');

insert into Record
values('Squat', '22-05-05', 120, 'psy');
insert into Record
values('BenchPress', '22-05-05', 200, 'psy');
insert into Record
values('Deadlift', '22-05-05', 80, 'psy');


insert into Challenge
values('Squat', 120, 'kms', 3);
insert into Challenge
values('Deadlift', 180, 'kms', 3);
insert into Challenge
values('Squat', 20, 'psy', 3);
insert into Challenge
values('Deadlift', 80, 'psy', 3);
insert into Challenge
values('Deadlift', 280, 'park', 3);

insert into Challenge
values('Squat', 220, 'kms', 2);
insert into Challenge
values('Deadlift', 180, 'kms', 2);
insert into Challenge
values('Squat', 120, 'psy', 2);
insert into Challenge
values('Deadlift', 180, 'psy', 2);

insert into Challenge
values('Squat', 150, 'lee', 6);
insert into Challenge
values('Deadlift', 135, 'lee', 6);
insert into Challenge
values('Squat', 170, 'psy', 6);
insert into Challenge
values('Deadlift', 120, 'kim', 6);
insert into Challenge
values('BenchPress', 120, 'kim', 6);

insert into Challenge
values('Squat', 150, 'lee', 4);
insert into Challenge
values('Deadlift', 135, 'lee', 4);
insert into Challenge
values('Squat', 170, 'psy', 4);
insert into Challenge
values('Deadlift', 120, 'kim', 4);
insert into Challenge
values('BenchPress', 120, 'kim', 4);

insert into Challenge
values('Squat', 150, 'lee', 5);
insert into Challenge
values('Deadlift', 135, 'park', 5);
insert into Challenge
values('Squat', 170, 'psy', 5);
insert into Challenge
values('Deadlift', 120, 'kms', 5);
insert into Challenge
values('BenchPress', 140, 'kim', 5);


insert into Challenge
values('Deadlift', 230, 'lee', 1);
insert into Challenge
values('Deadlift', 180, 'park', 1);



insert into Record
values('Squat', '22-11-25', 90, 'kms');
insert into Record
values('Deadlift', '22-11-25', 130, 'kms');
insert into Record
values('BenchPress', '22-11-25', 110, 'kms');


