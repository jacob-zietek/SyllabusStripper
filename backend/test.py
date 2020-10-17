import PyPDF2
import textract

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
        print(textArray[i]) 
        

'''
# Finds deltas between dates
for i in range(len(datesArray)-1):
    print(textArray[datesArray[i][1]])
    print(datesArray[i+1][1] - datesArray[i][1])
'''

