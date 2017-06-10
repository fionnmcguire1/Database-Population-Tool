"""
Generating a list of emails from usernames
Author: Fionn Mcguire
Date: 8/06/2017
"""

iterations = 10000
i=0
new_email = ''
max
with open('../SampleFiles/SampleUsernames.txt', 'r') as usernames:
    with open('../SampleFiles/SampleEmails.txt', 'w') as emails:
        user = usernames.readlines()

        while i < iterations:
            new_email = ''
            new_email = user[i]
            new_email = new_email.lower()
            new_email = new_email.replace('\n', '')
            new_email += '@gmail.com'
            new_email += '\n'
            emails.write(new_email)
            i = i+1
            
                
        
    
