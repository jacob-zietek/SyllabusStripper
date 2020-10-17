import PyPDF2
import textract

from dateutil.parser import parse

from datetime import datetime

from icalendar import Calendar, Event

import tempfile, os

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


filename = 'test.pdf'

pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""


while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text

text = text.replace("\r","")

text = text.replace("\n", "")

textArray = text.split("!")

# Contains tuples of the dates text and where the index of that date 
# is in textArray to be used for parsing later
datesArray = []

for i in range(len(textArray)):
    if is_date(textArray[i]):
        datesArray.append((textArray[i], i))
        #print(textArray[i]) 
        
# This next bit of code is designed to take the dates and the indexes of
# the dates to ultimately convert everything into a iCalendar file

dates = []
descriptions = []

# Assuming the description is one index over to the right of the date
# (this is a valid assumption in something like a table) we can update 
# the dates and descriptions arrays appropriately

for i in range(len(datesArray)):
    dates.append(datesArray[i][0])
    descriptions.append(textArray[datesArray[i][1]+1])
    
# This cleans up the data a little bit, it removes the end from - onward
# and replaces it with the current year. This should ensure it works for
# any semester. It then runs it through dateutil's parse function to standardize
# the layout of the data, it should be 'YYYY-MM-DD HH:MM:SS'

currentYear = datetime.now().year

for i in range(len(dates)):
    dates[i] = dates[i][:dates[i].find('-')] + " " + str(currentYear)
    dates[i] = parse(dates[i])

# !!! Note: dates now contains the dates in format 'YYYY-MM-DD HH:MM:SS'



# Initializes calendar class. Full documentation can be found here:
# https://icalendar.readthedocs.io/en/latest/usage.html
# !!! Note must include description and start time at least

cal = Calendar()

for i in range(len(dates)):
    event = Event() # Starts a new event
    dateComponents = str(dates[i]).split("-")
    year = int(dateComponents[0])
    month = int(dateComponents[1])
    day = int(dateComponents[2][:2])
    #print(dates[i])
    #print(day)
    timeComponents = str(dates[i]).split(":")
    hour = int(timeComponents[0][11:])
    minutes = int(timeComponents[1])
    seconds = int(timeComponents[2])
    #print(hour)
    
    # Formats date and time into something usable for event
    
    event.add('dtstart', datetime(year, month, day, hour, minutes, seconds))
    
    # Adds description
    
    event.add('summary', descriptions[i])
    
    # Can add more attributes to every event using afformentioned docs
    
    cal.add_component(event) # Writes event to calendar
    
    
# Writes calendar into "example.ics". Change this later, probably

f = open(os.path.join('example.ics'), 'wb')
f.write(cal.to_ical())
f.close()


'''
Code to write iCal file 
directory = tempfile.mkdtemp()
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()
'''
'''
# Finds deltas between dates
for i in range(len(datesArray)-1):
    print(textArray[datesArray[i][1]])
    print(datesArray[i+1][1] - datesArray[i][1])
'''

