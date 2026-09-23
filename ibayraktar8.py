#ibayraktar_Lab8_389

print ("Hello traveller!")

def game():
    name = input("Welcome! What is your name? ")
    print( name, ", you have been travelling for a long time, and you look very hungry. You have 5 different places to eat. The choices you make will affect your health.")
    print ("Here are the five place you can order your food, and remember, healthy choices!")
    count = 1
    places = ["Dominos Pizza ", "McDonalds", "Subway", "Whole Foods", "Seafood Grill"]
    for i in places:
        print (count, i)
        count=count+1

    select=int(input("Where would you like to eat, select a number between 1-5 : "))
    
    if select==1:
        print ("Welcome to Dominos Pizza! Our menu items are:" )
        count1=1
        menu1 = ["Triple-cheese pizza","Thin crust veggie-pizza","Cauliflower dough veggie pizza"]
        for i in menu1:
            print (count1, i)
            count1=count1+1
        select1=int(input("Enter the item number(1-3) you want to order! :" ))
        if select1==1:
            print ("Oh no!, too much cheese, your blood pressure will increase!")
        else:
            print ("Great choice, healthy and yummy!")

    if select==2:
        print ("Mcdonalds! Our menu items are:" )
        count2=1
        menu2 = ["Mc-chicken-Salad","Triple-burger+extra cheese","Large soda+Fries+Double cheese burger"]
        for i in menu2:
            print (count2, i)
            count2=count2+1
        select2=int(input("Enter the item number(1-3) you want to order! :" ))
        if select2==1:
            print ("A chiken salad, proetin and fiber, excellent choice!")
        else:
            print ("Shall we schedule a doctor appointment for a possible heart issue!!")
     
    if select==3:
        print ("Subway! Our menu items are:" )
        count3=1
        menu3 = ["Tuna Sandwhich","Veggie wrap","Extra bacon + double cheese footlong"]
        for i in menu3:
            print (count3, i)
            count3=count3+1
        select3=int(input("Enter the item number(1-3) you want to order! :" ))
        if select3==3:
            print ("Oh no! High cholestrol in your blood!!")
        else:
            print ("Well done, you made a healthy and tasty choice!")

    if select==4:
        print ("Wholefoods! Our menu items are:" )
        count4=1
        menu4 = ["Falafel + salad","Lentil soup + bean salad","Ice cream filled brownies"]
        for i in menu4:
            print (count4, i)
            count4=count4+1
        select4=int(input("Enter the item number(1-3) you want to order! :" ))
        if select4==1 or select4==2:
            print ("Great choice, keep travelling, you have a healthy diet!")
        else:
            print ("Come on! Is this your best to order at the Whole foods for hunger!!")
    
    if select==5:
        print ("Seafood Grill! Our menu items are:" )
        count5=1
        menu5 = ["Grilled tuna","Salmon Salad","Steamed mussels with crispy oysters"]
        for i in menu5:
            print (count5, i)
            count5=count5+1
        select5=int(input("Enter the item number(1-3) you want to order! :" ))
        if select5==1 or select5==2:
            print ("My favorite, you have good taste buds!")
        else:
            print ("Heads-up!, Don't eat too much and make sure they are well cooked - high parasite risk!!")



play = input("Would you like to play a game? ")

while play == "yes":
    game()
    play = input("Please enter -yes- if you would like to play again! ")
else:
    print("Bye!")


