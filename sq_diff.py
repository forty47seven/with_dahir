#Diffrence of Squares

n = int(input('Enter a value for N: '))

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 = sum1 + (i + 1)**2

for i in range(n):
    sum2 = sum2 + (i + 1)
sum2 = sum2 ** 2

if sum1 > sum2:
    diff = sum1 - sum2
elif sum2 > sum1:
    diff = sum2 - sum1
else:
    diff = 0

print (diff)