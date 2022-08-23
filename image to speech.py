#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[1]:


import pyttsx3
text_speech=pyttsx3.init()

answer=input("what to u want to convert to audio")
text_speech.say(answer)
text_speech.runAndWait()


# In[4]:


pip install pytesseract


# In[1]:


pip install pillow


# In[1]:


pip install pytesseract


# In[1]:


pip install pillow


# In[9]:


from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = "C:/Users/ELCOT/Desktop/images/quotes1.png"

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)


# In[1]:


from PIL import Image
from pytesseract import pytesseract
import pyttsx3
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = "C:/Users/ELCOT/Desktop/images/quotes1.png"

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)
#text to speech
text_speech=pyttsx3.init()

answer=(text)
text_speech.say(answer)
text_speech.runAndWait()


# In[ ]:





# In[ ]:




