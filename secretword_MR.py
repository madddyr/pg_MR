import random

number = random.randint(0,3)

words = ["cat","shoe","pizza","dragon"]
hint1 = ["chases mice","tastes great","laces","breathes fire"]
hint2 = ["meow","cheese and sauce","soles","flies"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess a word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer")
    guess = input()

    if guess == secretword:
        print("You win!!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print( hint2[number] )

    elif guess == "first letter":
        print( secretword[0] )

    elif guess == "give up":
        print("Ha! you gave up. Nice going.")
        print("You failed " + str(counter) + " times.")
        print("The word was " + secretword)
        break


    else:
        print("Nope, try again.")
        counter += 1
