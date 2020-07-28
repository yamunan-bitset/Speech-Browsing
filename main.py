#!/usr/bin/python3

import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening")
    audio = r3.listen(source)
    get = r3.recognize_google(audio)
    print(get)
    url = "https://www.google.com/search?safe=active&client=new&sxsrf=ALeKk019uGkm8WC8G6VHPiU0MLB3YJcbww%3A1595959583927&ei=H2kgX6qVOIz0kwWQ87bYAg&q="
    wb.get().open_new(url+get)

