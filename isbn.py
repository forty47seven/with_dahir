#ISBN Verifier

isbn = input('Enter an ISBN: ')

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

l_isbn = []

for i in isbn:
    for j in nums:
        if i == j:
            l_isbn.append(i)

sum = 0
for i in range(10):
    sum += (int(l_isbn[i]) * (10 - i))

if sum % 11 == 0:
    print ('Valid')
else:
    print('Invalid')