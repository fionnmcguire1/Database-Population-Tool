"""
Database populator is designed primarily for populating the tables of a new database.
The parameters specify the database language as well as the structure of that table. This file
uses a series of other text files to populate the various fields in the tables.

Author: Fionn Mcguire
Date: 21/05/2017

"""

"""
TODO LIST
 - Take files as variables
 - Allow users to specify seperators such as \n or ,
 - Allow users to specify table structure as parameters
 - Convert all parameters to lowercase
 - Distinguish the parameters as variable types
 - Check the data in the file match the datatype specified
 - Create text file with series of insert statements 
"""



"""
Parameter spec:
language: postgres, oracle, mysql
"""
CreateTable = "CREATE TABLE 'authentication' ('id' SERIAL PRIMARY KEY,'username' TEXT NOT NULL,'password' TEXT NOT NULL);"

def fmdbp(CreateTable, Language = 'postgres', NumRows = 1000):

    #Extract table name from create table query
    start = "CREATE TABLE"
    end = "("
    tablename = ((CreateTable.split(start))[1].split(end)[0])
    print(tablename)

    #cut and split string to prepare for analysis
    first_remove_string = "CREATE TABLE"
    first_remove_string = first_remove_string + tablename + "("
    
    CreateTable = CreateTable.replace(first_remove_string, '')
    CreateTable = CreateTable.replace(");", '')
    CreateTable = CreateTable.split(',')
    print(CreateTable)

    postgres_datatypes = ['CHAR', 'VARCHAR', 'INT', 'SERIAL', 'PRIMARY KEY', 'CHARACTER', 'TEXT', 'BIT', 'VAR BIT', 'SMALLINT', 'INTEGER', 'BIGINT'
                 'SMALLSERIAL', 'BIGSERIAL', 'MONEY', 'BOOL', 'BOOLEAN', 'DATE', 'TIMESTAMP', 'TIME','PRIMARY KEY', 'REFERENCES']
    
    



fmdbp(CreateTable)

"""
select * from student;

select * from authentication;

CREATE TABLE "authentication" (
  "id" SERIAL PRIMARY KEY,
  "username" TEXT NOT NULL,
  "password" TEXT NOT NULL
);

INSERT INTO authentication ( username, password) values ('richLyncher', 'mysecret5');


CREATE TABLE "student" (
  "studentid" SERIAL PRIMARY KEY,
  "firstname" VARCHAR(20) NOT NULL,
  "surname" VARCHAR(40) NOT NULL,
  "dob" DATE NOT NULL,
  "addressline1" VARCHAR(50) NOT NULL,
  "addressline2" VARCHAR(50) NOT NULL,
  "addressline3" VARCHAR(50) NOT NULL,
  "gender" BOOLEAN NOT NULL,
  "phonenumber" INTEGER,
  "email" TEXT NOT NULL,
  "authentication" INTEGER NOT NULL
);


INSERT INTO student (firstname, surname, dob, addressline1, addressline2, addressline3, gender, phonenumber, email, authentication)
VALUES ('Kevin', 'O Connell', '1994-05-04', '742 evergreen terrace', 'Springfield', 'Arizona', true, 0864472981, 'example@gmail.com', 1);
"""
    
