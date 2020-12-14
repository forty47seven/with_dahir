#Allergies

score = int(input('Enter allergy score: '))

l_allergy = ['Cats', 'Pollen', 'Chocolate', 'Tomatoes', 'Strawberries', 'Shellfish', 'Peanuts', 'Eggs']

if score >= 256:
    score = score % 256

count = 0

allergies = []
if score > 0:
    for i in range(8):
        if score >= (2**(7 - i)):
            allergies.append(l_allergy[i])
            score = score - (2**(7 - i))

    print ('Dude is allergic to the following:')
    print (*allergies)
else:
    print ('Dude is not allergic to the shit we have')