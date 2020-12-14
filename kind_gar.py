#Kindergarten Garden

row1 = input ('Enter the plants(1st row, hit the enter key and then 2nd row):\n[window][window][window]\n')
row1 = row1.lower()
p_row1 = []
row2 = input()
row2 = row2.lower()
p_row2 = []

for i in range(len(row1)):
    if row1[i] == 'g':
        p_row1.append('Grass')
    elif row1[i] == 'c':
        p_row1.append('Clover')
    elif row1[i] == 'r':
        p_row1.append('Radishes')
    elif row1[i] == 'v':
        p_row1.append('Violets')

for i in range(len(row2)):
    if row2[i] == 'g':
        p_row2.append('Grass')
    elif row2[i] == 'c':
        p_row2.append('Clover')
    elif row2[i] == 'r':
        p_row2.append('Radishes')
    elif row2[i] == 'v':
        p_row2.append('Violets')

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

for i in range(len(students)):
    print ("{}'s plants are {}, {}, {}, and {}" .format(students[i], p_row1[i * 2], p_row1[(i * 2) + 1], p_row2[i * 2], p_row2[(i * 2) + 1]))