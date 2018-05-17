import pyautogui as pg
import webbrowser
import time

emergency = pg.prompt(
    """
What is your emergency?
a)Weather
b)Fire
c)Health

""")

if emergency == "a":
    category = pg.prompt(
        """
What kind of weather incident?
a)Tornado
b)Flood
c)Hurricane
d)Snowstorm/Blizzard
e)Earthquake
f)Dust Storm

        """)

elif emergency == "b":
    category = pg.prompt(
        """
What kind of fire?
a)House Fire
b)Wildfire

""")


elif emergency == "c":
    category = pg.prompt(
        """
What kind of health emergency?
a)Heart attack
b)Choking

""")


    
pg.alert("""
If you are in immediate danger, please call 911 immediately.
Follow the instructions in the webpages that open following this message for other guidance.
""")
if emergency == "a":
    if category == "a":
        webbrowser.open("http://www.spc.noaa.gov/faq/tornado/safety.html")
    elif category == "b":
        webbrowser.open("https://www.ready.gov/floods")
    elif category == "c":
        webbrowser.open("https://www.livescience.com/3817-hurricane-preparation.html")
    elif category == "d":
        webbrowser.open("https://www.ready.gov/winter-weather")
    elif category == "e":
        webbrowser.open("https://www.ses.vic.gov.au/get-ready/quakesafe/what-to-do-in-an-earthquake")
    elif catefory == "f":
        webbrowser.open("https://ein.az.gov/hazards/dust-storms", "http://www.safebee.com/holiday/how-survive-dust-storm")


elif emergency == "b":
    if category == "a":
        webbrowser.open("http://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts")
    elif category == "b":
        webbrowser.open("http://www.readyforwildfire.org/What-To-Do-If-Trapped/")




elif emergency == "c"
    ir category == "a"

        
