import time
### Source: https://cdn-images-1.medium.com/max/1600/1*-i97l3xkz-bhk5k0YgvBEg.jpeg


print("Write a noun")
noun1 = input()

print("Write another noun")
noun2 = input()

print("Write another noun")
noun3 = input()

print("Write another noun")
noun4 = input()

print("Write an adjective")
adjective1 = input()

print("Write another adjective")
adjective2 = input()

print("Write another adjective")
adjective3 = input()

print("Write a plural noun")
pluralnoun1 = input()

print("Write another plural noun")
pluralnoun2 = input()

print("Write another plural noun")
pluralnoun3 = input()

print("Write a type of food")
typeoffood = input()

print("Write a type of liquid")
typeofliquid = input()

print("Write a part of the body")
partofthebody = input()

print("Write an animal")
animal = input()

print("Write an article of clothing")
articleofclothing = input()


### BEGIN MAD LIB ###

print("An amusement park is always fun to visit on a hot summer "
      + noun1 + "."" When you get there, you can wear your "
      + articleofclothing + " and go for a swim. And there are lots of "
      + adjective1 + " things to eat. You can start off whith a/an " + adjective2
      + "-dog on a/an " + noun2 + " with mustard, relish, and "
      + pluralnoun1 + " on it. Then you can have a buttered ear of "
      + noun3 + " with a nice " + adjective3 + " slice of "
      + typeoffood + " and a big bottle of cold " + typeofliquid
      + ". When you are full, it's time to go on the roller coaster, which should settle your "
      + partofthebody + ". Other amusement park rides are the bumper cars, which have little "
      + pluralnoun2 + " that you drive and run into other "
      + pluralnoun3 + ", and the merry-go-round, where you can sit on a big "
      + animal + " and try to grab the gold " + noun4 + " as you ride past it.")

time.sleep(100)
