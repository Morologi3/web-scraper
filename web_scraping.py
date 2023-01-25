import csv
import requests
from bs4 import BeautifulSoup
import regex as re

HTMLTags = re.compile('<.*?>')

headers={'User-Agent': 'Mozilla/5.0'}
url = 'https://www.bayt.com/en/uae/jobs/computer-science-jobs/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

lists = soup.find_all('li', class_="has-pointer-d")

# Open a CSV file to write the data
with open('job_listings.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Title', 'Company', 'Description', 'Salary']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for list in lists:
        title = list.find('h2', class_="jb-title m0 t-large")
        title = list.find('a')
        title = re.sub(HTMLTags, '', str(title))

        company = list.find('b', class_ = 'jb-company')
        company = re.sub(HTMLTags, '', str(company))

        description = list.find('div', class_ = 'jb-descr')
        description = re.sub(HTMLTags, '', str(description))

        salary = list.find('li', class_="p0 m10r jb-label-salary")
        salary = re.sub(HTMLTags, '', str(salary))
        # Write the data to the CSV file
        writer.writerow({'Title': title, 'Company': company, 'Description': description, 'Salary': salary})

