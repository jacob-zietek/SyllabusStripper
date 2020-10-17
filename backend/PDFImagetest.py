import pytesseract
import cv2 
import pdf2image
import PyPDF2
import textract
from dateutil.parser import parse
try:
    from PIL import Image
except ImportError:
    import Image
    
        #below converts the pdf file into image file
from pdf2image import convert_from_path
pages = convert_from_path('test.pdf', 500)

#below divide the converted image filed
for page in pages:
    page.save('test-1.png', 'PNG')

#below takes out the text from the pdf file
text = pytesseract.image_to_string(Image.open('test-1.png'))


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


filename = text

text = text.replace("\r","")

text = text.replace("\n", "")

textArray = text.split("!")


# Contains tuples of the dates text and where the index of that date 
# is in textArray to be used for parsing later
datesArray = []

print(textArray)

for i in range(len(textArray)):
    if is_date(textArray[i]):
        datesArray.append((textArray[i], i))
        print(textArray[i]) 
      

# Finds deltas between dates
for i in range(len(datesArray)-1):
    print(textArray[datesArray[i][1]])
    print(datesArray[i+1][1] - datesArray[i][1])
    
    
    

