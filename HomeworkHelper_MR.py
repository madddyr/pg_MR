import webbrowser
import pyautogui as pg

english = ["https://accounts.google.com/ServiceLogin/signinchooser?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin","https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin","http://www.thesaurus.com/","http://www.dictionary.com/"]

spanish = ["http://www.wordreference.com/","https://senorsalazarspanishclass.wordpress.com/","https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin"]

history = ["http://gcds-library.gcds.net/home","https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin"]

science = ["https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin","https://accounts.google.com/ServiceLogin/signinchooser?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"]

math = ["https://accounts.google.com/ServiceLogin/signinchooser?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin","https://www.desmos.com/","https://kahoot.it/"]



answer = pg.prompt(
"""
Which class do you want to work on?
a) english
b) spanish
c) history
d) science
e) math

"""
    )

if answer == "a":
    for i in english:
        webbrowser.open(i)


elif answer == "b":
    for i in spanish:
        webbrowser.open(i)


elif answer == "c":
    for i in history:
        webbrowser.open(i)


elif answer == "d":
    for i in science:
        webbrowser.open(i)


elif answer == "e":
    for i in math:
        webbrowser.open(i)
