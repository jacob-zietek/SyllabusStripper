from docx import Document
from dateutil.parser import parse

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
document = Document("demo.docx")

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
    for j in i:
        try:
            if(is_date(j)):
                datesArray.append(i)
        except ValueError:
            continue
  