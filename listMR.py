name = "Maddy"

subjects = ["English","Math","Science","Spanish","History"]

print("Hello " + name)

for i in subjects:
    print("One of my subjects is " + i)


sports = ["soccer","hockey","basketball","lacrossse","field hockey"]

for i in sports:
    if i == "field hockey":
        print(i + " isn't a sport")
    elif i == "hockey":
        print(i + " is awesome")
    elif i == "soccer":
        print(i + " is the best sport")
    else:
         print("One of my favorite sports is " + i)



food = []

while True:
    print("What food do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        food.append(answer)


for i in food:
    print("One of your favorite foods is " + i)
