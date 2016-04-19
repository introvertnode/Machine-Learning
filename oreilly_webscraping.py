from bs4 import BeautifulSoup
import requests 
import re

def isVideo(td):
    pricelabel=td('span','pricelabel')
    return (len(pricelabel)==1 and pricelabel[0].text.strip().startswith('Video'))

def book_info(td):
    title = td.find('div','thumbheader').a.text
    by_author = td.find('div','AuthorName').text
    authors=[name.strip() for name in re.sub("^By ", "", by_author).split(',')] 
    isbn_link = td.find('div','thumbheader').a.get('href')
    isbn = re.match("/product/(.*)\.do",isbn_link).group(1)
    date=td.find('span','directorydate').text.strip()
    
    return {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "date": date    
    }

from time import sleep

base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
               "data.do?sortby=publicationDate&page="
NUM_PAGES = 44
    
books=[]

for page_num in range(1, NUM_PAGES+1):
    print "scraping page " + str(page_num)
    url = base_url+str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    tds = soup('td', 'thumbtext') 
    for td in tds:
        if not isVideo(td):
            books.append(book_info(td))        
    
    sleep(30) # respecting the website's instructions
    

import matplotlib.pyplot as plt
from collections import Counter

year_counts = Counter(int(book['date'].split()[1]) for book in books)

years=[k for k in year_counts if int(k) < 2016]
counts = [year_counts[year] for year in year_counts if int(year)<2016]
plt.plot(years,counts) 
plt.ylabel("Number of books")
plt.xlabel("Year")
plt.title("Number of books per year")


