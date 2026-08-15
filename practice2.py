#bayraktar, Finding class average grades - for practice purpose

y = "yes"
total = 0
students = 0
while y == "yes":
    score = float(input("Enter the next stundet test score. "))
    y = input("Will you add another student test score?")
    total = score + total
    students = students + 1
    average = total/students
    print (" ")

if y == "no":
    print ("Your class average is ", average)
    print ("Have a great day.")
