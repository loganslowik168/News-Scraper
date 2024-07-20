import pickle

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


# Read the input file
with open('/home/slowikl/PythonPrograms/NewsScraper/News-Scraper/scrape_data.txt', 'r') as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
	date, data = process_line(line)
	print(f"--- Date: {date} --- ")
	for entry in data:
		if TARGET.lower() in entry.lower():
			print(entry)
	print('*'*40)

