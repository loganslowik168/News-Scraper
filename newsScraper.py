import requests
from bs4 import BeautifulSoup
import pickle
import datetime

url = 'https://www.bbc.com/news'
response = requests.get(url)
strippedLines = []
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')
date = datetime.datetime.now().strftime('%m-%d-%Y %I:%M %p')

#---
dataBreak = "|--|"
#---

filter = {"Follow BBC on:", "Presidential race", "Sport", "Also in news", "Most read", "Most watched", "Features & analysis"}

for x in headlines:
	strippedLines.append(x.text.strip())


filteredData = filtered_array = [item for item in strippedLines if item not in filter]


pickled = pickle.dumps(strippedLines)



#write data
with open('/home/slowikl/PythonPrograms/NewsScraper/News-Scraper/scrape_data.txt', 'a') as file:
	file.write(f"{date}{dataBreak}{pickled}\n")

