from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import speech_recognition as sr
import nltk
from google_images_download import google_images_download 
response = google_images_download.googleimagesdownload()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    
data = r.recognize_google(audio).encode("utf-8")
print (data)
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
 
into_string = str(wordsFiltered)
print(into_string)
arguments = {"keywords":into_string,"limit":2,"print_urls":True}   #creating list of arguments
response.download(arguments)   #passing the arguments to the function