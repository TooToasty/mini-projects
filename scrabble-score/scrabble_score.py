def score(word):
    total = 0
    word = word.lower().strip()
    for letter in word:
        if letter in 'aeioulnrst':
            total += 1
        elif letter in 'dg':
            total += 2
        elif letter in 'bcmp':
            total += 3
        elif letter in 'fhvwy':
            total += 4
        elif letter in 'jx':
            total += 8
        elif letter in 'qz':
            total += 10
        else:
            total += 5
    return total
