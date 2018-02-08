import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1

answer = pg.prompt(
"""
How would you like to spend your day?

a)Relaxing
b)Outside (hiking, biking, etc.)
c)Sight seeing

"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question 2

answer = pg.prompt(
"""
What do you like to do on the weekends?

a)Stay home
b)Sports
c)Hang out with friends

"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question 3

answer = pg.prompt(
"""
Who would you rather spend a day with?

a)Family
b)Your pet
c)Friends

"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



    # Question 4

answer = pg.prompt(
"""
What's your favorite color?

a)Blue
b)Green
c)Red

"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



    # Question 5

answer = pg.prompt(
"""
What do you usually do on planes?

a)Sleep
b)Look out the window
c)Watch a movie

"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# END OF SURVEY

pg.alert("you sould go to...")

# Beach
if points < 8:
    pg.alert("the beach")
    webbrowser.open("https://169j6v4ensbt3ahsnlytw5ut-wpengine.netdna-ssl.com/wp-content/uploads/sites/12/2018/01/6196292-beach-pictures.jpg")

# Mountains
elif points >= 8 and points < 12:
    pg.alert("the mountains")
    webbrowser.open("https://ac4fa7708134a70c34d3-66da2307b23609a8f8a6d8a13d2f16e2.ssl.cf1.rackcdn.com/974/1/large.jpg")
    
# City
elif points >= 12:
    pg.alert("a city")
    webbrowser.open("http://resourceglobalnetwork.com/wp-content/uploads/2016/09/newyorkcity.jpg")

