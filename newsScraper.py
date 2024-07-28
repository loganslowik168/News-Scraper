import requests
from bs4 import BeautifulSoup
import pickle
import datetime

def scrape(url, htmlHeaderType):

	response = requests.get(url)
	strippedLines = []
	soup = BeautifulSoup(response.text, 'html.parser')
	headlines = soup.find('body').find_all(htmlHeaderType)
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
		file.write(f"{url}{dataBreak}{date}{dataBreak}{pickled}\n")

###function call(s)
scrape('https://www.bbc.com/news', 'h2')
scrape('https://www.washingtonpost.com/', 'h2')
