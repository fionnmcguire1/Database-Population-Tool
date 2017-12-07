"""
Author: Fionn Mcguire
Date: 21-05-2017
Description: 
Database populator is designed primarily for populating the tables of a new database.
The parameters specify the database language as well as the structure of that table. This file
uses a series of other text files to populate the various fields in the tables.

"""

class FMDBPT:
    
    def configurePT(self,tableStructure,lang):
        self.tableName = (tableStructure.split('\'')[1].split('\'')[0])
        self.tableStructure = (tableStructure.split('(')[1].split(');')[0]).split(',') 
        self.lang = lang.lower()
        self.fieldNames = []
        self.configured = True
        postgres_datatypes = [ 'PRIMARY KEY', 'CHAR', 'VARCHAR', 'INT', 'SERIAL', 'CHARACTER', 'TEXT', 'BIT', 'VAR BIT', 'SMALLINT', 'INTEGER', 'BIGINT'
                'SMALLSERIAL', 'BIGSERIAL', 'MONEY', 'BOOL', 'BOOLEAN', 'DATE', 'TIMESTAMP', 'TIME', 'REFERENCES']    
        if self.lang == 'postgres':
            self.databaseSelected = postgres_datatypes
        print(self.tableStructure)

        for datatypeProvided in self.tableStructure:
            datatypeProvided = datatypeProvided.split(' ')
            length = len(datatypeProvided)
            checker = False
            AlreadyDeleted = False
            self.fieldNames.append(datatypeProvided[0])
            for i in range(1,length):
                if datatypeProvided[i].upper() in self.databaseSelected: 
                    checker = True
                if datatypeProvided[i].upper() in self.databaseSelected[0] or datatypeProvided[i].upper() == self.databaseSelected[-1]:
                    if AlreadyDeleted == False:
                        del self.fieldNames[-1]
                        AlreadyDeleted = True
                        print(self.tableStructure)
                        self.tableStructure.remove(" ".join(datatypeProvided))
                        print(self.tableStructure)
            if checker == False:
                print('Datatype:'+datatypeProvided[i]+' Not Recognised')
                self.configured = False
                

    def configWritingMethod(self,method,location=None):
        self.method = method
        self.location = None

    def FMwriteData(self,numLines,fieldModes):
        if len(fieldModes) != len(self.fieldNames):
            print(fieldModes)
            print("Wassup")
            print(self.fieldNames)
            return False
        output = ""
        import random
        def randomRange(rows,start=0,end=10):
            start,end = int(start),int(end)
            if start > end:
                end = start+10
            rangeList = []
            for i in range(rows):
                rangeList.append(random.randrange(start, end))
            return rangeList
            
        def randomSeq(start=0,end=10):
            start,end = int(start),int(end)
            if start > end:
                end = start+10
            seqList = [x for x in range(start,end)]
            return seqList

        def randomChar(rows,specifiedString = None):
            if specifiedString == None or type(specifiedString) != str:
                specifiedString = 'abcdefghijklmnopqrstuvwxyz' 
            charList = []
            for i in range(rows):
                charList.append(random.choice([letter for letter in specifiedString]))
            return charList

        def randomBool(rows,pattern=None):
            boolList = []
            if pattern == None:
                for i in range(rows):
                    boolList.append(random.choice['True','False'])
            else:
                for i in range(rows):
                    if pattern[i%len(pattern)] == 'T':
                        boolList.append('True')
                    else:
                        boolList.append('False')
            return boolList

        def randomFloat(rows,start=0.0,end=10.0):
            start,end = float(start),float(end)
            floatList = []
            if start > end:
                end = start+10.0
            for i in rows:
                floatList.append(random.uniform(start,end))
            return floatList

        dataGenerated = []
        for mode in fieldModes:
            mode = mode.split(' ')
            if len(mode) > 1:
                start = mode[1]
            if len(mode) > 2:
                end = mode[2]

            if mode[0] == 'rr':       
                dataGenerated.append(randomRange(numLines,start,end))
            elif mode[0] == 'rs':
                dataGenerated.append(randomSeq(start,end))
            elif mode[0] == 'rc':
                dataGenerated.append(randomChar(numLines,mode[1]))
            elif mode[0] == 'rb':
                dataGenerated.append(randomBool(numLines,mode[1]))
            elif mode[0] == 'rf':
                dataGenerated.append(randomFloat(numLines,start,end))
        #print(dataGenerated)
        lengthOfDG = len(dataGenerated)
        for insert in range(numLines):
            output+= "INSERT INTO '"+self.tableName+"'("
            
            output+=(", ".join(self.fieldNames))
            output+=field+") VALUES("
            #Need to cycle through the len of arrays if you're less than

            for column in range(lengthOfDG):
                output+= str(dataGenerated[column][insert])+", "
            output+=");"
        print(output)
        #print("Hello")
            
### Edge Cases ###
# Provide contingencies
# fieldModes must be list as long as tableStructure
# Must have items contained in the datatypes
# UNLESS the data has been extracted from online
# check location
CreateTable = "CREATE TABLE 'authentication' ('id' SERIAL PRIMARY KEY,'username' TEXT NOT NULL,'password' TEXT NOT NULL);"
newTool = FMDBPT()
newTool.configurePT(CreateTable,'postgres')
newTool.configWritingMethod('p')
newTool.FMwriteData(50,['rc abcde','rb TTF'])
