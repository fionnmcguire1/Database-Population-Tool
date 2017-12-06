"""
Author: Fionn Mcguire
Date: 21-05-2017
Description: 
Database populator is designed primarily for populating the tables of a new database.
The parameters specify the database language as well as the structure of that table. This file
uses a series of other text files to populate the various fields in the tables.

"""
#import random

CreateTable = "CREATE TABLE 'authentication' ('id' SERIAL PRIMARY KEY,'username' TEXT NOT NULL,'password' TEXT NOT NULL);"

class FMDBPT:
    def configurePT(self,tableStructure,lang):
        self.tableName = (tableStructure.split('\'')[1].split('\'')[0])
        self.tableStructure = (tableStructure.split('(')[1].split(');')[0])
        self.lang = lang

    def configWritingMethod(self,method,location=None):
        self.method = method
        self.location = None

    def FMwriteData(self,numLines,fieldModes):
        
        

### Edge Cases ###
# lang to lower case
# programatically disect tableStructure
# check location
# Get datafrom online sources
# Provide contingencies
# fieldModes must be list as long as tableStructure
# Must have items contained in the datatypes
# UNLESS the data has been extracted from online

newTool = FMDBPT()
newTool = newTool.configurePT(CreateTable,'postgres')
