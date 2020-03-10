import pyttsx3
import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
from playsound import playsound
import datetime
import time
from glob import glob
import os
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("550x350")
root.title("Voice Language Translator")
label1 = Label(text="Using the most advance AI technology to translate voice")
label1.pack()


def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

def trans():

    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty("voice",voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def speak2(audio1):
        language = 'ur'
        myobj = gTTS(text=audio1, lang=language, slow=False)
        millis = int(round(time.time()))
        file_name = "\\audio\\"+str(millis)+".mp3"
        myobj.save(file_name)
        playsound(file_name)
        #for filename in glob("F:\\Audio\\*.mp3"):
            #os.remove(filename)
        

    def takeCommand():
        r=sr.Recognizer() 
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold=0.3
            audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language="en-in")
            print("user said: ",query)
        except Exception as e:
            print('say again')
            return "None"
        return query

    def forurdu():
        r=sr.Recognizer() 
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold=0.4
            audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language="ur")
            print("user said: ",query)
        except Exception as e:
            print('say again')
            return "None"
        return query

    def translation(x):
        a = TextBlob(x)
        z = a.translate(to = "en")
        return z

    def translation1(x):
        a = TextBlob(x)
        z = a.translate(to = "ur")
        return z


    if __name__ == "__main__":
        speak("please tell me your target language")
        a =takeCommand().lower()
        if a == "urdu":
            speak("speak your sentences")
            while True:
                line = takeCommand().lower()
                a = translation1(line)
                speak2(str(a))
                if "stop" == line:
                    speak("ok")
                    break
        elif a == "english":
            speak("please speak your sentences")
            while True:
                
                try:
                    line2 = forurdu()
                    x = translation(line2)
                    speak(x)
                except Exception as e:
                    speak("please speak valid sentence")
                if "روک دو" == line2:
                    speak("ok")
                    break
Button(root,text="Start Translator", command=trans).pack()
Button(root,text="Stop", command=stop).pack()
root.mainloop()
    
    