word = input('Enter a word: ')
special = input('Enter \'t\' for triple word and \'d\' for double word: ')

d_word = {
    'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1, 'l' : 1, 'n' : 1, 'r' : 1, 's' : 1, 't' : 1,
    'd' : 2, 'g' : 2,
    'b' : 3, 'c' : 3, 'm' : 3, 'p': 3,
    'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4,
    'k' : 5,
    'j' : 5, 'x' : 8,
    'q' : 10, 'z' : 10
}

count = 0

for i in range(len(word)):
    count = count + d_word[word[i].lower()]

if special.lower() == 't':
    print (count * 3)
elif special.lower() == 'd':
    print (count * 2)
else:
    print (count)