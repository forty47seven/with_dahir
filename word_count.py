#Word Count

text = 'Now this is going to Be the one TO be but IS it going tO keep up NOW or loose it\'s momentum'
l_text = text.split()
d_text = {}

for i in range(len(l_text)):
    count = 0
    for j in range(len(l_text) - 1):
        if l_text[i].lower() == l_text[j+1].lower():
            count += 1
    d_text.update({l_text[i].lower() : count})
    
for i, j in d_text.items():
    print (i + ': ' + str(j))

