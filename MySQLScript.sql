DROP SCHEMA IF EXISTS oblig2022;
CREATE SCHEMA oblig2022;

USE oblig2022;
SET FOREIGN_KEY_CHECKS=0;


CREATE TABLE Student
(
Studentnr CHAR (6),
fornavn CHAR (30),
Etternavn CHAR (20),
Epost CHAR (40),
Telefon CHAR (8) ,
CONSTRAINT StudentPK PRIMARY KEY (Studentnr)
);
CREATE TABLE Emne
(
Emnekode CHAR (8),
Emnenavn CHAR (40),
studiepoeng CHAR (3.1),
CONSTRAINT EmnePK PRIMARY KEY (Emnekode)
);
CREATE TABLE Rom
(
Romnr CHAR(4),
Antallplasser INTEGER(3),
CONSTRAINT RomPK PRIMARY KEY (Romnr)
);
CREATE TABLE Eksamen
(
Emnekode CHAR(8),
Dato DATE,
Romnr CHAR(4),
CONSTRAINT EksamenPK PRIMARY KEY (Emnekode,Dato),
CONSTRAINT EksamenEmneFK FOREIGN KEY (Emnekode) 
REFERENCES Emne (Emnekode),
CONSTRAINT EksamenRomFK FOREIGN KEY (Romnr) 
REFERENCES Rom (Romnr)
);
CREATE TABLE Eksamensresultat
(
Studentnr CHAR (6),
Emnekode CHAR (8),
Dato DATE,
Karakter CHAR (1),
CONSTRAINT EksamensresultatPK PRIMARY KEY (studentnr,emnekode,Dato),
CONSTRAINT EksamensresultatStudentFK FOREIGN KEY (Studentnr) 
REFERENCES student (studentnr),
CONSTRAINT EksamensresultatEmneFK FOREIGN KEY (Emnekode) 
REFERENCES Emne (Emnekode),
CONSTRAINT EksamensresultatEksamenFK FOREIGN KEY (emnekode,Dato) 
REFERENCES Eksamen (emnekode,Dato)
);
-- Round 2

INSERT INTO Student VALUES (252199,'Ole','Olsen','ole@live.no',12345678);
INSERT INTO Student VALUES (252200,'Hans','Hansen','hans@live.no',87654321);
INSERT INTO Student VALUES (252196,'Jens','Jensen','jens@live.no',11111111);
INSERT INTO Student VALUES (252198,'Trine','Trinesen','trine@look.no',00000000);
INSERT INTO Student VALUES (252197,'Kari','Karisen','kari@live.no',32323232);

INSERT INTO Emne VALUES (1000,'PRO1000',7.5);
INSERT INTO Emne VALUES (1001,'PRG1100',7.5);
INSERT INTO Emne VALUES (1002,'ØKAD3000',15);
INSERT INTO Emne VALUES (2000,'APP2000',15);
INSERT INTO Emne VALUES (2002,'SAMF3000',7.5);

INSERT INTO Rom VALUES (1, 45);
INSERT INTO Rom VALUES (2,30);
INSERT INTO Rom VALUES (3,10);
INSERT INTO Rom VALUES (4,20);
INSERT INTO Rom VALUES (5,13);

INSERT INTO Eksamen VALUES (1000,'2018-05-14',1);
INSERT INTO Eksamen VALUES (1001,'2022-02-14',2);
INSERT INTO Eksamen VALUES (1002,'2022-01-01',3);
INSERT INTO Eksamen VALUES (2000,'2020-01-30',3);
INSERT INTO Eksamen VALUES (2002,'2021-05-11',1);
INSERT INTO Eksamen VALUES (2002,'2021-02-11',1);
INSERT INTO Eksamen VALUES (2002,'2021-02-12',1);

INSERT INTO Eksamensresultat VALUES (252198,1000,'2018-05-13','F');
INSERT INTO Eksamensresultat VALUES (252197,1001,'2022-04-14','A');
INSERT INTO Eksamensresultat VALUES (252198,1000,'2020-11-11','C');
INSERT INTO Eksamensresultat VALUES (252198,2000,'2020-02-22','B');
INSERT INTO Eksamensresultat VALUES (252200,2000,'2022-05-05','B');
INSERT INTO Eksamensresultat VALUES (252197,1000,'2018-09-14','A');

