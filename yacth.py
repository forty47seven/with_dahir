#Yacth

cate = input ("Enter the category: 'Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Full House', 'Four of a Kind', 'little Straight', 'Big Straight', 'Choice', 'Yacth'\n")
cate = cate.lower()

dice = input('Enter value of five dice separated by single spaces: ')
dice = dice.lower()

l_dice = dice.split()
l_dice = sorted(l_dice)
d_dice = {'ones' : 1, 'twos' : 2, 'threes' : 3, 'fours' : 4, 'fives' : 5, 'sixes' : 6}

for j in d_dice:
    if cate == j:
        print (j.upper())
        count = 0
        for i in l_dice:
            if int(i) == d_dice[cate]:
                count += 1

        print (d_dice[cate] * count)

if cate == 'full house':
    print ('FULL HOUSE')

    if  l_dice[0] == l_dice[1] == l_dice[2]:
        result1 = int(l_dice[0]) * 3
    elif l_dice[-1] == l_dice[-2] == l_dice[-3]:
        result1 = int(l_dice[-1]) * 3
    else:
        result1 = 0
    
    if l_dice[0] == l_dice[1] != l_dice[2]:
        result2 = int(l_dice[0]) * 2
    elif l_dice[-1] == l_dice[-2] != l_dice[-3]:
        result2 = int(l_dice[-1]) * 2
    else:
        result2 = 0

    if result1 > 0 and result2 > 0:
        print (result1 + result2)

if cate == 'four of a kind':
    print ('FOUR OF A KIND')

    if  l_dice[0] == l_dice[1] == l_dice[2] == l_dice[3]:
        result = int(l_dice[0]) * 4
    elif l_dice[-1] == l_dice[-2] == l_dice[-3] == l_dice [-4]:
        result = int(l_dice[-1]) * 4
    else:
        result = 0
    
    print (result)

if cate == 'little straingt':
    print ('LITTLE STRAIGHT')

    if l_dice[0] == '1' and l_dice[1] == '2' and l_dice[2] == '3' and l_dice[3] == '4' and l_dice[4] == '5':
        print (30)

if cate == 'big straingt':
    print ('BIG STRAIGHT')

    if l_dice[0] == '2' and l_dice[1] == '3' and l_dice[2] == '4' and l_dice[3] == '5' and l_dice[4] == '6':
        print (30)

if cate == 'choice':
    print(int(l_dice[0]) + int(l_dice[1]) + int(l_dice[2]) + int(l_dice[3]) + int(l_dice[4]))

if cate == 'yacth':
    if l_dice[0] == l_dice[1] == l_dice[2] == l_dice[3] == l_dice[4]:
        print (50)