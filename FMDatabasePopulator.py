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
 - Figure out the best way to link files to fields
"""



"""
Parameter spec:
language: postgres, oracle, mysql
"""
CreateTable = "CREATE TABLE 'authentication' ('id' SERIAL PRIMARY KEY,'username' TEXT NOT NULL,'password' TEXT NOT NULL);"

def fmdbp(CreateTable, Language = 'postgres', NumRows = 1000, *args):

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

    postgres_datatypes = [ 'PRIMARY KEY', 'CHAR', 'VARCHAR', 'INT', 'SERIAL', 'CHARACTER', 'TEXT', 'BIT', 'VAR BIT', 'SMALLINT', 'INTEGER', 'BIGINT'
                 'SMALLSERIAL', 'BIGSERIAL', 'MONEY', 'BOOL', 'BOOLEAN', 'DATE', 'TIMESTAMP', 'TIME', 'REFERENCES']

    database_chosen = []
    datatypes = []
    fieldnames = []
    if Language == 'postgres':
        database_chosen = postgres_datatypes
        
    i = 0
    while i < len(CreateTable):
        j = 0
        while j < len(database_chosen):
            if database_chosen[j] in CreateTable[i]:
                if j == 0:
                    pass
                else:
                    datatypes.append(database_chosen[j])
                    fieldnames +=  ((CreateTable[i].split('\''))[1].split('\''))
                #print(database_chosen[j])
                j = len(database_chosen)
            j +=1
        i+=1
    print(datatypes)
    print(fieldnames)

    if len(fieldnames) != len(args):
        return
        
    i = 0
    j = 0
    checker = True
    while i < len(args):
        try:
            file1 = open(args[i], 'r')
            if datatypes[i] == postgres_datatypes[3] or datatypes[i] == postgres_datatypes[4] or \
            datatypes[i] == postgres_datatypes[7] or datatypes[i] == postgres_datatypes[8] or \
            datatypes[i] == postgres_datatypes[9] or datatypes[i] == postgres_datatypes[10] or \
            datatypes[i] == postgres_datatypes[11]:
                
                j = 0
                while j < len(file1):
                    if file1[j].isnumeric() == False:
                        checker = False
                    j +=1
                if checker == False:
                    print("Incorrect Data type in file "+arg[i])
        except OSError:
            print()
        i = i+1


fmdbp(CreateTable,'postgres',1000,'../SampleFiles/SampleFirstNames.txt','../SampleFiles/SampleSurNames.txt')

# '0-100' this is how you define a range
# 'random35' random character generation of strings length 35 characters

"""
Test datatypes in the files
Program the randomiser and number range as well as the boolean values
"""

    
