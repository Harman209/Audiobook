from gtts import gTTS
import PyPDF2
import pdfplumber

file = input("Name of the file: \n")
pdfFileObj = open(file, 'rb')
pdfeader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfeader.numPages
language = 'en'
# start = input('Enter the starting page no. - 1  Eg - if pg 4 enter 3 : ')

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)

def speak(text):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save('audiobook.mp3')

speak(text)



