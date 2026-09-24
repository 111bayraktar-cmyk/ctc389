#ibayraktar09_389

#ibayraktar_Lab8_389

print ("Hello traveller!")

def game():
    name = input("Welcome! What is your name? ")
    print(name, ", you have been travelling for a long time, and you look very hungry. Your journey home has 5 stops, and the food choices you make along the way will affect your health.")
    print("Let's see how healthy you can stay by the time you get home!")

    places = ["Dominos Pizza", "McDonald's", "Subway", "Whole Foods", "Seafood Grill"]
    health_score = 0

    for stop in range(5):
        print(" ")
        print("Stop", stop + 1, "of 5: you arrive at", places[stop])

        if stop == 0:
            print("Welcome to Dominos Pizza! Our menu items are:")
            count1 = 1
            menu1 = ["Triple-cheese pizza", "Thin crust veggie-pizza", "Cauliflower dough veggie pizza"]
            for i in menu1:
                print(count1, i)
                count1 = count1 + 1
            select1 = int(input("Enter the item number(1-3) you want to order! :"))
            if select1 == 1:
                print("Oh no!, too much cheese, your blood pressure will increase!")
                health_score = health_score - 1
            else:
                print("Great choice, healthy and yummy!")
                health_score = health_score + 1

        if stop == 1:
            print("McDonalds! Our menu items are:")
            count2 = 1
            menu2 = ["Mc-chicken-Salad", "Triple-burger+extra cheese", "Large soda+Fries+Double cheese burger"]
            for i in menu2:
                print(count2, i)
                count2 = count2 + 1
            select2 = int(input("Enter the item number(1-3) you want to order! :"))
            if select2 == 1:
                print("A chicken salad, protein and fiber, excellent choice!")
                health_score = health_score + 1
            else:
                print("Shall we schedule a doctor appointment for a possible heart issue!!")
                health_score = health_score - 1

        if stop == 2:
            print("Subway! Our menu items are:")
            count3 = 1
            menu3 = ["Tuna Sandwich", "Veggie wrap", "Extra bacon + double cheese footlong"]
            for i in menu3:
                print(count3, i)
                count3 = count3 + 1
            select3 = int(input("Enter the item number(1-3) you want to order! :"))
            if select3 == 3:
                print("Oh no! High cholesterol in your blood!!")
                health_score = health_score - 1
            else:
                print("Well done, you made a healthy and tasty choice!")
                health_score = health_score + 1

        if stop == 3:
            print("Wholefoods! Our menu items are:")
            count4 = 1
            menu4 = ["Falafel + salad", "Lentil soup + bean salad", "Ice cream filled brownies"]
            for i in menu4:
                print(count4, i)
                count4 = count4 + 1
            select4 = int(input("Enter the item number(1-3) you want to order! :"))
            if select4 == 1 or select4 == 2:
                print("Great choice, keep travelling, you have a healthy diet!")
                health_score = health_score + 1
            else:
                print("Come on! Is this your best choice at the Whole Foods for hunger!!")
                health_score = health_score - 1

        if stop == 4:
            print("Seafood Grill! Our menu items are:")
            count5 = 1
            menu5 = ["Grilled tuna", "Salmon Salad", "Steamed mussels with crispy oysters"]
            for i in menu5:
                print(count5, i)
                count5 = count5 + 1
            select5 = int(input("Enter the item number(1-3) you want to order! :"))
            if select5 == 1 or select5 == 2:
                print("My favorite, you have good taste buds!")
                health_score = health_score + 1
            else:
                print("Heads-up!, Don't eat too much and make sure they are well cooked - high parasite risk!!")
                health_score = health_score - 1

    print(" ")
    print(name, ", you have made it home! Your final health score is", health_score)

    if health_score >= 3:
        print("You feel amazing! You are fit, full of energy, and your blood pressure is right where it should be.")
    elif health_score >= 0:
        print("You made it home okay, but a few of those choices could catch up with you. Try to eat healthier next trip!")
    else:
        print("You collapse onto the couch. The doctor says you are prediabetic and have high blood pressure. Time for a diet change!")


play = input("Would you like to play a game? ")

while play == "yes":
    game()
    play = input("Please enter -yes- if you would like to play again! ")
else:
    print("Bye!")
