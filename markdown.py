#Markdown

text = input('Enter a markdown sentence: ')

mark_list = ['*', '_', '>', '#', '-', '+']

for i in text:
    for j in mark_list:
        if i == j:
            n_text = text.replace(i, '')

print (n_text)