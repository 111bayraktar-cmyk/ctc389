#ibayraktar7b_ Lab 3-4 Review

def game():
    x=14
    y=int(input("Guess my number: "))
    while x!=y and y>x-3 and y<x+3:
        y= int(input("Close, try again: "))

    if x==y:
        print("Well done! You guessed my number")
    elif y>x:
        print("Sorry, you lost. Your guess was higher than my number which is", x)
    else:
        print("Sorry, you lost. Your guess was lower than my number which is", x)

play = input("Would you like to play my game? ")

while play == "yes":
    game()
    play = input("Would you like to play my game? ")
