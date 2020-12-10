book_list = ['Harry Potter: ', 'Bourne: ', 'Lord of the Rings: ', 'The Broker: ', 'Hamlet: ']

print ('We have five books for you\nYou get 5 percent discount if you buy 2 different titles\n10 percent for 3\n20 percent for 4\n25 for all 5\nEnter the amount of each book you want')

buy_list = []

for i in range(5):
    book = int(input(book_list[i]))
    
    buy_list.append(book)

cost = 0

while (buy_list[0] + buy_list[1] + buy_list[2] + buy_list[3] + buy_list[4]) > 0:
    
    for i in range(5):
        count = 0

        if buy_list[0] > 0:
            count += 1
            buy_list[0] -= 1
        if buy_list[1] > 0:
            count += 1
            buy_list[1] -= 1
        if buy_list[2] > 0:
            count += 1
            buy_list[2] -= 1
        if buy_list[3] > 0:
            count += 1
            buy_list[3] -= 1
        if buy_list[4] > 0:
            count += 1
            buy_list[4] -= 1
        
        if count == 5:
            cost =(cost) + (0.75 * (5 * 8))
        elif count == 4:
            cost =(cost) + (0.80 * (4 * 8))
        elif count == 3:
            cost =(cost) + (0.90 * (3 * 8))
        elif count == 2:
            cost =(cost) + (0.95 * (2 * 8))
        elif count == 1:
            cost =(cost) + (8)

print ('\n***\nYour total cost is:', cost, '\n***')