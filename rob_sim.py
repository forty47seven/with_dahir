#Robot Simulator

pos_x = int(input('Enter x-cordinate: '))
pos_y = int(input('Enter y-cordinate: '))
dirc = input('Enter direction (North, South, East, West): ')
dirc = dirc.lower()

inst = input('Enter instructions:\nExample: RAALA, for turn right, advance twice, turn left, advance once\n')
inst = inst.lower()

for i in inst:
    if i == 'r':
        if dirc == 'north':
            dirc = 'east'
        elif dirc == 'south':
            dirc = 'west'
        elif dirc == 'east':
            dirc = 'south'
        elif dirc == 'west':
            dirc = 'north'
    elif i == 'l':
        if dirc == 'north':
            dirc = 'west'
        elif dirc == 'south':
            dirc = 'east'
        elif dirc == 'east':
            dirc = 'north'
        elif dirc == 'west':
            dirc = 'south'
    elif i == 'a':
        if dirc == 'north':
            pos_y = pos_y + 1
        if dirc == 'south':
            pos_y = pos_y - 1
        if dirc == 'east':
            pos_x = pos_x + 1
        if dirc == 'west':
            pos_x = pos_x - 1

print ('({}, {}), facing {}' .format(pos_x, pos_y, dirc))