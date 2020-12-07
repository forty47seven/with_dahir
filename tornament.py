table = {'chelsea': 0, 'man utd': 0, 'arsenal': 0, 'liverpool': 0}

result = input('Enter result in this format: home team;away team;win/loose/draw for home team (no spaces beforw semi colon): ')

while result != '0':

    l_result = result.split(';')
    if l_result[2].lower() == 'win':
        table[l_result[0]] = table[l_result[0]] + 3

    elif l_result[2].lower() == 'loose':
        table[l_result[1]] = table[l_result[1]] + 3

    elif l_result[2].lower() == 'draw':
        table[l_result[0]] = table[l_result[0]] + 1
        table[l_result[1]] = table[l_result[1]] + 1
    
    print (table)
    result = input('Enter result in this format: home team;away team;win/loose/draw for home team (no spaces beforw semi colon). Enter 0 to: ')


print('Done')