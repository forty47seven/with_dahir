#Luhn

cc_num = input('Enter Credit Card Number: ')

num_list = []

for i in range(len(cc_num)):
    num_list.append(int(cc_num[i]))

for i in range(len(num_list)//2):
    x = num_list[-(i + 1) * 2] * 2
    if x > 9:
        x = x - 9
    else:
        x = x
    num_list[-(i + 1) * 2] = x

sum = 0
for i in range(len(num_list)):
    sum = sum + num_list[i]

if sum % 10 == 0:
    print ('Valid')
else:
    print ('Invalid')