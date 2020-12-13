#Rotational Cipher

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

inp = input ('Enter key and text\nEg. ROT4 encrypt this\nFor key = 4, text = encrypt this\n')
inp = inp.split()

rot = inp[0]
key = int(rot[3:])

text = inp[1 :]

cypher = []

for i in text:
    new_word = ''
    for j in i:
        pos = alfa.index(j) + key
        if pos > 25:
            pos = pos - 26
        new_word = new_word + alfa[pos]
    cypher.append(new_word)

print (*cypher)