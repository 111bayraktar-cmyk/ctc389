#ibayraktar7_Lab #1/#2 Review


x=14

y=int(input("Guess my number: "))

if y>16:
    print ("You lost, my number is smaller than, ", y)

if y<12:
    print ("You lost, my number is bigger than, ", y)

while y>11 and  y<14:
    y=int(input("You are close, try again; "))

while y>14 and y<17:
    y=int(input("You are to close, try again; "))

if y==x:
    print ("Well done, you guessed my number")



