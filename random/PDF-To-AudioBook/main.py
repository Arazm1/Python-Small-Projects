import pyttsx3
import PyPDF2
from tkinter.filedialog import *

file = askopenfilename()
pdfreader = PyPDF2.PdfReader(file)

number_of_pages = len(pdfreader.pages)

player = pyttsx3.init()

for i in range(number_of_pages):
    page = pdfreader.pages[i]
    text = page.extract_text()
    
    if text:
        player.say(text)
    
    
player.runAndWait()