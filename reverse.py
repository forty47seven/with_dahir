#Reverse

text= input('Enter the text you want reversed: ')
r_text = text[-1]

for i in range(len(text) - 1):
    r_text = r_text + text[-(i + 2)]

print (r_text)