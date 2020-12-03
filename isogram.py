text = input('Enter a word: ')
count = 0
for i in range(len(text)):
    for j in range(len(text) - 1):
        if count < 1 and i != j:
            if text[i] == text[j]:
                count += 1
                print ('The word is not an isogram')
        elif count < 1:
            count += 1
            print ('The word is an isogram')