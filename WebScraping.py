import requests
from bs4 import BeautifulSoup
import re 
import csv 
   
URL = "https://exampledomain.com" 
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content,'html5lib') 
   
emails=[]  
   
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
for text in soup.stripped_strings:
    for email in email_pattern.findall(text):
        entry = {}
        entry['url'] = email
        emails.append(entry)

for row in soup.find_all('a',href=True):
    if 'mailto:'in row['href']:
        entry = {} 
        entry['url'] = row['href'][7:] #remove the mailto: part from the link
        emails.append(entry) 
   
filename = 'emails.csv'
with open(filename,'w',newline='') as f: 
    w = csv.DictWriter(f,['emails']) 
    w.writeheader() 
    for email in emails: 
        w.writerow(email) 
