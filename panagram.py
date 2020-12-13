#Pangram

sentence = input('Enter a sentence: ')
sent = sentence.lower()

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

check =0

for i in alfa:
    count = 0
    for j in sent:
        if i == j:
            count += 1
    if count > 0:
        check += 1

if check == 26:
    print ('The sentence is a pangram')
else:
    print ('The sentence is not a pangram')