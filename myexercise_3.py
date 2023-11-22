my_list = input('enter a list please: ').split(',')
my_list = [int(x) for x in my_list]
shift = int(input('enter the shift amount: '))
n = shift % len(my_list)

if n > 0:
    output = my_list[-n:] + my_list[:-n]
else:
    output = my_list[n:] + my_list[:n]
print('output',output)

# exercise 2
your_sentence = input('please write a sentence ')

letters = [x for x in your_sentence.lower() if x.isalpha()]

counter = {letter: letters.count(letter) for letter in list(letters)}

counts = tuple(sorted(counter.items()))
print(counts)
