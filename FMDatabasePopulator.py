"""
Author: Fionn Mcguire
Date: 21-05-2017
Description: 
Database populator is designed primarily for populating the tables of a new database.
The parameters specify the database language as well as the structure of that table. This file
uses a series of other text files to populate the various fields in the tables.

"""
#import random

class FMDBPT:
    
    def configurePT(self,tableStructure,lang):
        self.tableName = (tableStructure.split('\'')[1].split('\'')[0])
        self.tableStructure = (tableStructure.split('(')[1].split(');')[0]).split(',') 
        self.lang = lower(lang)
        self.fieldNames = []
        self.configured = True
        postgres_datatypes = [ 'PRIMARY KEY', 'CHAR', 'VARCHAR', 'INT', 'SERIAL', 'CHARACTER', 'TEXT', 'BIT', 'VAR BIT', 'SMALLINT', 'INTEGER', 'BIGINT'
                'SMALLSERIAL', 'BIGSERIAL', 'MONEY', 'BOOL', 'BOOLEAN', 'DATE', 'TIMESTAMP', 'TIME', 'REFERENCES']    
        if self.lang == 'postgres':
            self.databaseSelected = postgres_datatypes


        for datatypeProvided in self.tableStructure:
            datatypeProvided = datatypeProvided.split(' ')
            length = len(datatypeProvided)
            checker = False
            self.fieldNames+=datatypesProvided[0]
            for i in range(1,length):
                if datatypeProvided[i] in self.databaseSelected: 
                    checker = True
                    break
            if checker == False:
                print('Datatype:'+datatypeProvided[i]+' Not Recognised')
                self.configured = False
                

    def configWritingMethod(self,method,location=None):
        self.method = method
        self.location = None

    #def FMwriteData(self,numLines,fieldModes):
        
        

### Edge Cases ###
# lang to lower case
# check location
# Get datafrom online sources
# Provide contingencies
# fieldModes must be list as long as tableStructure
# Must have items contained in the datatypes
# UNLESS the data has been extracted from online

CreateTable = "CREATE TABLE 'authentication' ('id' SERIAL PRIMARY KEY,'username' TEXT NOT NULL,'password' TEXT NOT NULL);"
newTool = FMDBPT()
newTool.configurePT(CreateTable,'postgres')
newTool.configWritingMethod('p')
