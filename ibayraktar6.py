#ibayraktar 389, Lab 6

print ("Current Student List:")
slist = ["Mary", "Lisa", "Andy", "Peter", "Nolan"]
for i in slist:
    print (i)


print ("To add a new student name, type 1 .")

print ("To modify a student name, type 2 .")

print ("To remove a student name, type 3 .")

x  = int(input("Select your choice 1-3: "))

if x==1:
    new = input("Please enter the new student name. ")
    slist.append(new)
    print ("~~New Student List~~")
    for i in slist:
        print (i)

if x==2:
    print ("Enter the student number that you want to modify : ")
    count=1
    for i in slist:
        print (count, i)
        count = count+1
    y = int(input("Select the student number you want to modify :"))
    z = input("Enter the modifed name : ")

    slist[y-1]=z
    
    print ("~~~ New Student List ~~~")
    count2=1
    for i in slist:
        print (count2, i)
        count2=count2+1

if x==3:

    count3=1
    for i in slist:
        print (count3, i)
        count3=count3+1
    a = int(input("Select the student number to delete from the list : "))
    slist.pop(a-1)
    print ("~~~~~ New Student List ~~~~~")
    count4=1
    for i in slist:
        print (count4, i)
        count4=count4+1

   




