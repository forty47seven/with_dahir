#Run Length Encoding

text = input('Enter a text: ')

pos = 0
nxt_pos = 1
comp = ''

while pos < len(text):
    count = 1
    while text[pos] == text[nxt_pos] and pos != nxt_pos:
        count += 1
        pos += 1
        nxt_pos += 1

        if nxt_pos == len(text):
            nxt_pos = pos

    if count > 1:
        comp = comp + str(count) + text[pos]
    else:
        comp = comp + text[pos]
    pos = pos + 1
    nxt_pos = nxt_pos + 1
    
    if nxt_pos == len(text):
        nxt_pos = pos

print (comp)