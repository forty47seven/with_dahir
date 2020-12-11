que = input('Enter Question: ')

if que == '':
    print('Fine. Be that way!')

elif que.isupper() == True and que[-1] == '?':
    print ('Calm down, I know what I\'m doing!')

elif que[-1] == '?':
    print ('Sure')

elif que.isupper() == True:
    print ('Whoa, chill out!')

else:
    print ('Whatever')