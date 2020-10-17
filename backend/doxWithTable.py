from docx import Document
from dateutil.parser import parse
from datetime import datetime

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




# Creates and reads a docx file
document = Document("docWithTableTests/cs191.docx")

#Stores rows and columns of a table
data = []

keys = None

for table in document.tables:
    for i, row in enumerate(table.rows):
        text = (cell.text for cell in row.cells)

        # Establish the mapping based on the first row
        # headers; these will become the keys of our dictionary
        if i == 0:
            keys = tuple(text)
            continue

        # Construct a dictionary for this row, mapping
        # keys to values for this row
        row_data = tuple(text)
        data.append(row_data)

datesArray = []

#Iterates through rows and columns, if it encounters a date, adds it to data array

for i in data:
    for j in range(len(i)):
        #Checks if j is a date and not numeric, used to prevent integers, such as 1, to pass as dates
        if(is_date(i[j]) and i[j].isnumeric() == False):
            #Gets sublist from j to the end, ensures that the date will be the first index
            datesArray.append(i[j:])
            break
        #Splits j into a word array seperated by spaces
        wordArray = i[j].split(" ")
        for k in wordArray: 
            #Checks if k is a date and not numeric, used to prevent integers from passing
            if(is_date(k) and k.isnumeric() == False):
                #Gets sublist from j to the end, ensures that the date will be the first index
                datesArray.append((k,) + i[j:])
                break
        #Breaks out of inner 2 loops if the prior if statement evaulates
        else:
            continue
        break

print("test")
