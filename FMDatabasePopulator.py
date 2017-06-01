"""
Database populator is designed primarily for populating the tables of a new database.
The parameters specify the database language as well as the structure of that table. This file
uses a series of other text files to populate the various fields in the tables.

Author: Fionn Mcguire
Date: 21/05/2017

"""
import random

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
            if 'RANDOMRANGE' in args[i] or  'RANDOMFLOATRANGE' in args[i] or  'RANDOMSEQ' in args[i] or 'RANDOMBOOL' in args[i] or  'RANDOMCHAR' in args[i] :
                pass
            else:
                file1 = open(args[i], 'r')
                if datatypes[i] == postgres_datatypes[3] or datatypes[i] == postgres_datatypes[4] or \
                datatypes[i] == postgres_datatypes[7] or datatypes[i] == postgres_datatypes[8] or \
                datatypes[i] == postgres_datatypes[9] or datatypes[i] == postgres_datatypes[10] or \
                datatypes[i] == postgres_datatypes[11]:
                
                    j = 0
                    while j < len(file1):
                        if ''.join(file1[j]).isnumeric() == False:
                            checker = False
                        j +=1
                else:
                    j = 0
                    while j < len(file1.readlines()):
                        if ''.join(file1.readlines(j)).isdigit() == True:
                            checker = False
                        j +=1
                if checker == False:
                    print("Incorrect Data type in file "+arg[i])
            

        except OSError:
            print()
        i = i+1
    tablename = tablename.replace('\'','')
    tablename = tablename.replace(' ','')
    with open('../SampleFiles/InsertStatementsOn'+tablename+'.txt', 'w') as inserts:
        j = 0
        while j < NumRows:
            insertStatement = "INSERT INTO "+tablename+" ("
            l = 0
            while l < len(fieldnames):
                insertStatement += fieldnames[l]+", "
                l = l+1
            insertStatement = insertStatement[:-2]
            insertStatement += ") VALUES ("
            l = 0
            while l < len(fieldnames):
                if 'RANDOMRANGE' in args[l] or  'RANDOMFLOATRANGE' in args[l] or  'RANDOMSEQ' in args[l] or 'RANDOMBOOL' in args[l] or  'RANDOMCHAR' in args[l] :
                    a = DataGenerator(args[l])
                    print(a)
                    insertStatement += str(a)+"', "                  
                else:
                    file1 = open(args[l], 'r')
                    a = file1.readlines()
                    insertStatement += "'"+a[j].replace('\n','')+"', "
                l = l+1
            insertStatement = insertStatement[:-2]            
            inserts.write(insertStatement+");\n")
            j=j+1

#fmdbp(CreateTable,'postgres',1,'../SampleFiles/SampleUsernames.txt','../SampleFiles/SamplePasswords.txt')



def DataGenerator(SpecifiedRange):
    if 'RANDOMRANGE' in SpecifiedRange:
        SpecifiedRange = SpecifiedRange.replace('RANDOMRANGE','')
        SpecifiedRange = SpecifiedRange.replace(' ','')
        SpecifiedRange = SpecifiedRange.split('-')
        #print(random.randint(int(SpecifiedRange[0]), int(SpecifiedRange[1])))
        return random.randint(int(SpecifiedRange[0]), int(SpecifiedRange[1]))

    elif 'RANGESEQ' in SpecifiedRange:
        SpecifiedRange = SpecifiedRange.replace('RANGESEQ','')
        SpecifiedRange = SpecifiedRange.replace(' ','')
        SpecifiedRange = SpecifiedRange.split('-')
        if len(SpecifiedRange) == 2:
            print(SpecifiedRange[0])
            position = int(SpecifiedRange[0]) + 1
            return ('RANGESEQ '+SpecifiedRange[0]+'-'+SpecifiedRange[1]+'-'+str(position))
        if len(SpecifiedRange) == 3:
            if int(SpecifiedRange[2]) < int(SpecifiedRange[1]) and int(SpecifiedRange[2]) > int(SpecifiedRange[0]):
                print(SpecifiedRange[2])
                position = int(SpecifiedRange[2]) + 1
                return ('RANGESEQ '+SpecifiedRange[0]+'-'+SpecifiedRange[1]+'-'+str(position))
            elif int(SpecifiedRange[2]) > int(SpecifiedRange[1]):
                print(SpecifiedRange[0])
                position = int(SpecifiedRange[0])
                return ('RANGESEQ '+SpecifiedRange[0]+'-'+SpecifiedRange[1]+'-'+str(position))
                
                
    elif 'RANDOMCHAR' in SpecifiedRange:
        SpecifiedRange = SpecifiedRange.replace('RANDOMCHAR','')
        SpecifiedRange = SpecifiedRange.replace(' ','')
        iterator = int(SpecifiedRange)
        i = 0
        returnedString = ''
        while i < iterator:            
            returnedString += random.choice('abcdefghijklmnopqrstuvwxyz')
            i+=1
        return returnedString

    elif 'RANDOMBOOL' in SpecifiedRange:
        boolReturned = random.uniform(0, 1)
        if boolReturned > 0.5:
            return 'TRUE'
        else:
            return 'FALSE'
    elif 'RANDOMFLOATRANGE' in SpecifiedRange:
        SpecifiedRange = SpecifiedRange.replace('RANDOMFLOATRANGE','')
        SpecifiedRange = SpecifiedRange.replace(' ','')
        SpecifiedRange = SpecifiedRange.split('-')
        return random.uniform(float(SpecifiedRange[0]), float(SpecifiedRange[1]))
    else:
        print("Not a valid parameter specified")
    
    #random.randint(1, 10)     //Random integer between 1 and 10
    #random.uniform(1, 10)     //Random float between 1 and 10
    #random.choice('abcdefghij')     //Random element within list

#TESTING the DATAGENERATOR function
'''
DataGenerator('RANDOMRANGE 3-100')
DataGenerator('RANDOMCHAR 9')

i = 0
ie = 10
parameter = ''
while i < ie:
    if parameter == '':
        parameter = DataGenerator('RANGESEQ 3-100')
    else:
        parameter = DataGenerator(parameter)
    DataGenerator('RANDOMBOOL')
    DataGenerator('RANDOMFLOATRANGE 3-100')
    i +=1

'''

fmdbp(CreateTable,'postgres',10,'../SampleFiles/SampleUsernames.txt','RANDOMRANGE 3-100')

