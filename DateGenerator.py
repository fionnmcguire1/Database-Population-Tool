"""
Generating a List of dates appropriote for the field, in this case the Date of birth Field
Author: Fionn Mcguire
Date: 08/06/2017
"""
import random

iterations = 10000
i=0
new_date = ''

with open('../SampleFiles/SampleDates.txt', 'w') as dates:
    while i < iterations:
        new_date += str(random.randint(1999, 2005))+'-'
        new_date += str(random.randint(1, 12))+'-'
        new_date += str(random.randint(1, 28))
        new_date += '\n'
        dates.write(new_date)
        i = i+1
            
                
        
    
