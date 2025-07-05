create database interfichas;
use interfichas;

alter table lista_equipos add column estado enum('Clasificado', 'Eliminado');
insert into lista_equipos(equipo,ficha,jornada,estado) values 
('Argentina', '2998608', 'Mañana', 'Clasificado'),
('Belgica', '2928649', 'Mañana', 'Eliminado'),
('Bosnia', '2877050', 'Mañana', 'Clasificado'),
('Brasil', '2998584', 'Mañana', 'Eliminado'),
('China', '3001583', 'Tarde', 'Clasificado'),
('Colombia', '3063988', 'Mañana', 'Eliminado'),
('Costa Rica', '2928719', 'Tarde', 'Clasificado'),
('Croacia', '2827605','Mañana', 'Eliminado')
;

truncate table lista_equipos;

delete from lista_equipos where id = 2;

select * from lista_equipos;

select * from users;

insert into users (username, password) values ('admin','123');

show tables;