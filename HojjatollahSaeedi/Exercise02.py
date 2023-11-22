# This is second exercise of week 3
# This program count number of letters in a sentences

lstalphabet = (['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0],
               ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0],
               ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0],
               ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0],
               ['y', 0], ['z', 0])




lenoflstalphabet = len(lstalphabet)

mysentence = input("Please, Enter your sentence for counting the letters: ")
mysentence = mysentence.lower()

lenofsentence = len(mysentence)

x = 0

while x < lenofsentence:
    i = 0
    while i < lenoflstalphabet:
        if mysentence[x] == lstalphabet[i][0]:
            lstalphabet[i][1] += 1
        i +=1
    x += 1

list_lstalphabet = list(lstalphabet)

i = 0
while i <= lenoflstalphabet-1 :
    if list_lstalphabet[i][1] == 0:
        del list_lstalphabet[i]
        lenoflstalphabet -= 1
        continue
    else: i += 1


lstalphabet = tuple(list_lstalphabet)
print("The number of every letters in your sentence is: ")

i = 0
x = 0
while i < int(len(lstalphabet)):
    if x % 4 == 0:
        print('\n')
    print('****', lstalphabet[i][0], '==>', lstalphabet[i][1], end = ' ****')
    i += 1
    x += 1


# End of the exercise