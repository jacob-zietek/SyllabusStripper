import re
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

#Multiple Regex Expressions
#User Input?


# Creates and reads a docx file
document = Document("docWithTableTests/412.docx")

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

regArray = ["Jan[^0-9]+[0-2][0-9]" , "Feb[^0-9]+[0-2][0-9]" , "Mar[^0-9]+[0-2][0-9]" , "Apr[^0-9]+[0-2][0-9]" , "May[^0-9]+[0-2][0-9]" , "Jun[^0-9]+[0-2][0-9]" , "Jul[^0-9]+[0-2][0-9]" , "Aug[^0-9]+[0-2][0-9]" , "Sep[^0-9]+[0-2][0-9]" , "Oct[^0-9]+[0-2][0-9]" , "Nov[^0-9]+[0-2][0-9]" , "Dec[^0-9]+[0-2][0-9]" , 
    "Jan[^0-9]+[0-9]" , "Feb[^0-9]+[0-9]" , "Mar[^0-9]+[0-9]" , "Apr[^0-9]+[0-9]" , "May[^0-9]+[0-9]" , "Jun[^0-9]+[0-9]" , "Jul[^0-9]+[0-9]" , "Aug[^0-9]+[0-9]" , "Sep[^0-9]+[0-9]" , "Oct[^0-9]+[0-9]" , "Nov[^0-9]+[0-9]" , "Dec[^0-9]+[0-9]" ,
    "[0-1][0-9][/][0-2][0-9]" , "[0-1][0-9][/][0-9]" , "[0-9][/][0-2][0-9]" , "[0-9][/][0-9]" , "[0-1][0-9][-][0-2][0-9]" , "[0-1][0-9][-][0-9]" , "[0-9][-][0-2][0-9]" , "[0-9][-][0-9]"]

for i in data:
    for j in range(len(i)):
        #Checks if j is a date and not numeric, used to prevent integers, such as 1, to pass as dates            
       
        for u in range(len(regArray)):
            regDate = re.findall(regArray[u],i[j])
            if (regDate != None):
                #Gets sublist from j to the end, ensures that the date will be the first indexreg
                for reg in regDate:
                    if(u < 24 or is_date(reg)):
                        datesArray.append((reg,) + i[j:])
                        datesArray.append((reg,) + i[j:])
                        break
                else:
                    continue
                break
        #Breaks out of inner 2 loops if the prior if statement evaulates
        else:
            continue
        break
        

print("test")
