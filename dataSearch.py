import pickle
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
def process_line(line):
	try:
	# Split the line into date part and pickled part
		date_part, source_part, pickled_part = line.strip().split('|--|')
	# Strip any extra whitespace from the date part
		date = date_part.strip()
		source = source_part.strip()

        # Unpickle the data (pickled_part is expected to be a valid Python bytes object as a string)
		pickled_data = pickle.loads(eval(pickled_part))
#		print(f"Date: {date}\nSource: {source}\nPickledData: {pickled_data}")
		return date, source, pickled_data
	except Exception as e:
        	print(f"Error processing line: {line}\n{e}")
	        return None, None, None

###begin
SAMPLE_SOURCE = input('Enter the site you wish to scrape:')

while True:
	try:
		SAMPLES = int(input('Enter number of search terms to be plotted: '))
		break
	except:
		print('Not a valid option.')


#gloabls
fullDataset = []
graphData = {}
allTerms = []

# Read the input file
with open('/home/slowikl/PythonPrograms/NewsScraper/News-Scraper/scrape_data.txt', 'r') as file:
    lines = file.readlines()

def printRawData():
	# Process each line in the file
	for line in lines:
		date, source, data = process_line(line)
		print(f"--- Date: {date} --- ")
		for entry in data:
			if TARGET.lower() in entry.lower():
				print(entry)
		print('*'*40)

def gatherDataset():
	earliestDate='00'
	#for each scrape run
	for line in lines:
		count = 0
		date, source, data = process_line(line)
		if earliestDate == '00':
			earliestDate = date
		#for each array element
		for entry in data:
			if TARGET.lower() in entry.lower() and SAMPLE_SOURCE.lower() in entry.lower():
				count+=1
			graphData[date] = count
		print(f"{count} results matched your query")
	return earliestDate


##### propgram below
for sample in range(SAMPLES):
	TARGET = input('Enter a search term (case insensitive): ')
	ed = gatherDataset()
	fullDataset.append(graphData.copy())
	allTerms.append(TARGET)

#print('Full dataset IS')
#print(fullDataset)
plt.figure(figsize=(10, 5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y %I:%M %p'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Number of articles')
titleText = "Source: " + SAMPLE_SOURCE
plt.title(titleText)

for searchTerm in fullDataset:
	dates = list(searchTerm.keys())
	#print(f"Dates: {dates}")
	values = list(searchTerm.values())
	#print(f"Vals: {values}")
	# Convert date strings to datetime objects
	dates = [datetime.strptime(date, '%m-%d-%Y %I:%M %p') for date in dates]
	plt.plot(dates, values, marker='o', label=allTerms.pop(0))
plt.legend(loc="upper left")
plt.savefig('image_out.png')
#plt.show()
