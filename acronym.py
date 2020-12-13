#Acronym

name = input('Enter the name: ')

l_name = name.split()
x = ''

for i in range(len(l_name)):
    y = l_name[i]
    x = x + y[0]
    

print (x.upper())