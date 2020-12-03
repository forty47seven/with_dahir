intro = ['On the' , ' day of christmas my true love gave to me: ']
days = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
gifts = ['a Partridge in a Pear Tree.', 'two Turtle Doves, and', 'three French Hens,', 'four Calling Birds,', 'five Gold Rings,', 'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,', 'nine Ladies Dancing,', 'ten Lords-a-Leaping,', 'eleven Pipers Piping,', 'twelve Drummers Drumming,']

song = [intro[0], days[0], intro[1], gifts[0]]
print (*song)
for i in range(11):
    song.remove(song[1])
    song.insert(1, days[i + 1])
    song.insert(3, gifts[i + 1])
    print (*song)