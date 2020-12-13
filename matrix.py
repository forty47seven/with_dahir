#Matrix

matrix = '''
9 8 7
5 3 2
6 6 7
'''

def row(row_num):
    rows = []
    for i in range(3):
        rows.append(int(matrix[(1 +((row_num - 1) * 6)) + (i * 2)]))
    print (rows)


def column(col_num):
    columns = []
    for i in range(3):
         columns.append(int(matrix[(col_num + (col_num - 1) ) + 1 * (i * 6)]))
    print (columns)

for i in range(3):
    row(i + 1)

for i in range(3):
    column(i + 1)