#Isogram

text = input('Enter a word: ')
count = 0

for i in range(len(text)):

    for j in range(len(text) - (1 + i)):

        if count < 1 and text[i] == text[j + (i + 1)]:
            print (text + ' is not an isogram')
            
            count += 1
        
if count == 0:
    print (text + ' is an isogram')