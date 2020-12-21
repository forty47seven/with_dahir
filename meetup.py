#Meetup

meet = input('Enter meet up date in December 2020:\nFormat: First Monday of December 2020\n')
meet = meet.lower()

l_meet = meet.split()

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

dates = {'monday' : [7, 14, 21, 28],
'tuesday' : [1, 8, 15, 22, 29],
'Wednesday' : [2, 9, 16, 23, 30],
'thursday' : [3, 10, 17, 24, 31],
'friday' : [4, 11, 18, 25],
'saturday' : [5, 12, 19, 26],
'sunday' : [6, 13, 20, 27]}

for i in days:
    if i == l_meet[1]:
        if l_meet[0] == 'first':
            day = dates[i][0]
        elif l_meet[0] == 'second':
            day = dates[i][1]
        elif l_meet[0] == 'third':
            day = dates[i][2]
        elif l_meet[0] == 'fourth':
            day = dates[i][3]
        elif l_meet[0] == 'fifth':
            day = dates[i][4]
        elif l_meet[0] == 'last':
            day = dates[i][-1]

print ('2020/12/{}' .format(day))
