import pickle
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
def process_line(line):
    try:
        # Split the line into date part and pickled part
        date_part, pickled_part = line.strip().split('|--|')

        # Strip any extra whitespace from the date part
        date = date_part.strip()

        # Unpickle the data (pickled_part is expected to be a valid Python bytes object as a string)
        pickled_data = pickle.loads(eval(pickled_part))

        return date, pickled_data
    except Exception as e:
        print(f"Error processing line: {line}\n{e}")
        return None, None

###begin
TARGET = input('Enter a search term (case insensitive): ')

#gloabls
graphData = {}


# Read the input file
with open('/home/slowikl/PythonPrograms/NewsScraper/News-Scraper/scrape_data.txt', 'r') as file:
    lines = file.readlines()

def printRawData():
	# Process each line in the file
	for line in lines:
		date, data = process_line(line)
		print(f"--- Date: {date} --- ")
		for entry in data:
			if TARGET.lower() in entry.lower():
				print(entry)
		print('*'*40)

def plotData():
	earliestDate='00'
	#for each scrape run
	for line in lines:
		count = 0
		date, data = process_line(line)
		if earliestDate == '00':
			earliestDate = date
		#for each array element
		for entry in data:
			if TARGET.lower() in entry.lower():
				count+=1
			graphData[date] = count

	return earliestDate

GOAL = input('What to do with this data? (Choose: echo/plot)')
if GOAL == 'echo':
	printRawData()
elif GOAL == 'plot':
	ed = plotData()
	dates = list(graphData.keys())
	values = list(graphData.values())
	print(f"dates: {dates}\nvalues: {values}")
	# Convert date strings to datetime objects
	dates = [datetime.strptime(date, '%m-%d-%Y %I:%M %p') for date in dates]
	plt.figure(figsize=(10, 5))
	plt.plot(dates, values, marker='o')
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y %I:%M %p'))
	plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
	plt.gcf().autofmt_xdate()
	plt.xlabel('Date')
	plt.ylabel('Number of articles')
	plt.title('Articles about ' + TARGET)
	plt.savefig('image_out.png')
	plt.show()
