_list = [45, 76, 123, 1234, 38, 5, 25, 890, 457, 220, 47, 29]

def highscore():
    score = 0
    for i in _list:
        if i > score:
            score = i
    return score 

print ('The Highest Score is', highscore())