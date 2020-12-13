#Armstrong Number

num = input('Enter a number to test: ')
sum = 0

for i in range(len(num)):
    sum = sum + int(num[i])**len(num)

if sum == int(num):
    print (num, 'is an Armstrong number')
else:
    print (num, 'is not an Armstrong number')