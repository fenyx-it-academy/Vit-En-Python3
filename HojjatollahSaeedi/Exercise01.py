# This is first exercise of week 3
# Shift the elements of a list

mylist = []

listnum = int(input("Enter number of elements of your list: "))
i = 1
while i <= listnum:
    if i == 1:
        print("Enter", i, "st element for your list: ")
    else:
        print("Enter", i, "th element for your list: ")

    mylist.append(input())
    i += 1

print("your list is: ", mylist)


lenofmylist = len(mylist)
print("the length of my list is: ", lenofmylist)

shiftnum = int(input("Enter a number for shift in your list: "))

if (shiftnum > 0) and (shiftnum <= lenofmylist):
    wraplist = []
    counter = (lenofmylist - shiftnum)
    x = counter
    while counter <= (lenofmylist - 1):
        wraplist.append(mylist[x])
        del mylist[x]
        counter += 1

    wraplist.extend(mylist)
    mylist = wraplist

elif (shiftnum < 0) and ((-1 * shiftnum) <= lenofmylist):
    wraplist = []
    counter = (shiftnum * -1) - 1

    while counter >= 0:
        wraplist.insert(0, mylist[counter])
        del mylist[counter]
        counter -= 1

    mylist.extend(wraplist)
else: print("You enter a wrong number for shift")

print("Your list after shifting is : ", mylist)

# End of the exercise