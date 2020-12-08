def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Please enter DNA with the same length!")
    for letter in range(len(strand_a)):
        if strand_a[letter] != strand_b[letter]:
            distance += 1
    return distance

print(distance("GGACGGATTCTG", "AGGACGGATTCT"))
