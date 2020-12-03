x = input('Enter a number: ')
y = int(x)
drop = 0

if y % 3 == 0:
    drop = 'pling'
if len(str(drop)) > 1 and y % 5 == 0:
    drop = drop + 'Plang'
elif y % 5 == 0:
    drop = 'Plang'
if len(str(drop)) > 1 and y % 7 == 0:
    drop = drop + 'Plong'
elif y % 7 == 0:
    drop = 'Plong'

print(drop)