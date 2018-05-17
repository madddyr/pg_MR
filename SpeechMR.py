import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name?")
answer = pg.prompt("Enter in your name")

speak.Speak("Hello " + answer + ". Nice to meet you.")

speak.Speak("What is your favorite color?")
color = pg.prompt("Enter in your favorite color")

if color == "Blue":
    speak.Speak("Blue is my favorite too.")

elif color == "Black":
    speak.Speak("Black, just like my soul.")

else:
    speak.Speak(color + " is an... interesting color. But whatever. Apparently you are entitled to your own opinion or something")

speak.Speak("What video would you like to watch?")
video = pg.prompt("Enter video here")
wb.open("https://www.youtube.com/results?search_query=" + video)
