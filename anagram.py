#Anagram

word = input('Emter main word: ')
cand = input('Enter candidate, separated with spaces: ')
l_cand = cand.split()

for i in l_cand:
    check = 0
    for j in i:
        count = 1
        for k in word:
            if j == k:
                count += 1
                if count > 1:
                    check += 1
    if check == len(word):
        print (i)