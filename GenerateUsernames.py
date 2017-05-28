"""
Using first and last name files to join entires to make usernames
Author: Fionn Mcguire
Date: 24/05/2017
"""

iterations = 10000
i=0
new_username = ''
max
with open('../SampleFiles/SampleFirstNames.txt', 'r') as firstnames:
    with open('../SampleFiles/SampleSurNames.txt', 'r') as lastnames:
        with open('../SampleFiles/SampleUsernames.txt', 'w') as usernames:
            first = firstnames.readlines()
            last = lastnames.readlines()
            #print(first[46])
            #print(last[46])
            while i < iterations:
                new_username = ''
                new_username = first[i%len(first)]
                new_username += last[i%len(last)]
                new_username = new_username.lower()
                new_username = new_username.title()
                new_username = new_username.replace('\n', '')
                new_username += '\n'
                usernames.write(new_username)
                i = i+1
            
                
        
    
