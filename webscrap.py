import requests
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://en.wikipedia.org/wiki/Deep_learning'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# printing page title in console and in a text file also
print('Page Title is : ' + '\033[1m' + soup.title.string)
print("{}".format(soup.title.string), file=open("output.txt", "a"))

# finding all elements with <a> tag
atag = soup.findAll('a')
i=0

for link in atag:
    # extracting href elements fron <a> tag elements and printing them
    print(link.get('href'))
    print("{}".format(link.get('href')), file=open("output.txt", "a"))
    i+=1

# total number of links in a page
print('total links in this page are : ' + str(i))

