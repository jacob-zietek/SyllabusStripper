import PyPDF2
import textract

from dateutil.parser import parse

from datetime import datetime

import pandas as pd

import datefinder

import tabula

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


print(is_date("10/16- 10/30"))

df = tabula.read_pdf("anotherTable.pdf", pages='all')

maxI = -1;

bestIndex = -1;

for i in range(len(df)):
    if len(df[i]) * len(df[i].columns) > maxI:
        maxI = len(df[i]) * len(df[i].columns)
        bestIndex = i
        
dfOfInterest = df[bestIndex]

dfOfInterest = pd.DataFrame(dfOfInterest).to_numpy()

datesArray = []

for i in range(len(dfOfInterest)):
    for j in range(len(dfOfInterest[i])):
        
        matches = list(datefinder.find_dates(str(dfOfInterest[i][j])))
        print(matches)
        print((i,j))
        '''
        if is_date(str(dfOfInterest[i][j])):
            datesArray.append((dfOfInterest[i][j], (i,j)))
        '''
    


'''

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
# any semester. 

currentYear = datetime.now().year

for i in range(len(dates)):
    dates[i] = dates[i][:dates[i].find('-')] + " " + str(currentYear)
    dates[i] = parse(dates[i])
'''

'''
# Finds deltas between dates
for i in range(len(datesArray)-1):
    print(textArray[datesArray[i][1]])
    print(datesArray[i+1][1] - datesArray[i][1])
'''

