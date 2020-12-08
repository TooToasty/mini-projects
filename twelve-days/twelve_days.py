#This function returns the verse put in
def single_verse(verse):
    verses = [
    "and a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,"
    ]

    pre_day = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
    ]
#Because first verse is different than all the oters
    if verse == 1:
        return "On the {} day of Christmas my true love gave to me: {}".format(pre_day[0], verses[0][4:])
    else:
        after_colon = []
        for i in verses[:verse]:
            after_colon.append(i)
        after_string = " ".join(after_colon[::-1])
        return "On the {} day of Christmas my true love gave to me: {}".format(pre_day[verse - 1], after_string)

#This is the main function which handles the loop for multiple verses and error handling.
def recite(start_verse, end_verse):
    start = int(start_verse)
    end = int(end_verse)

    #Invalid Input output
    if (start <= 0 or end > 12):
        raise Exception("Please enter numbers between 1-12.")
    elif start > end:
        raise Exception("Please enter a valid first and last verse.")
#Case for a single verse
    if start == end:
        return [single_verse(end)]
    else:
        final_string = ''
        count = (end - start) + 1
        while count >= 1:
            final_string = single_verse(end) + "" + final_string
            end -= 1
            count -= 1

        return [final_string]






print(recite(1, 3))
