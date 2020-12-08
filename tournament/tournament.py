def tally(rows):
    temp = [row.split(';') for row in rows]
    keys = ['MP', 'W', 'D', 'L', 'P']
    table = {el: {key: 0 for key in keys} for row in temp for el in row[:2]}

    print(temp)
    for row in temp:
        table[row[0]]['MP'] += 1
        table[row[1]]['MP'] += 1
        if row[2] == 'win':
            table[row[0]]['W'] += 1
            table[row[0]]['P'] += 3
            table[row[1]]['L'] += 1
        elif row[2] == 'loss':
            table[row[1]]['W'] += 1
            table[row[1]]['P'] += 3
            table[row[0]]['L'] += 1
        elif row[2] == 'draw':
            table[row[1]]['D'] += 1
            table[row[1]]['P'] += 1
            table[row[0]]['D'] += 1
            table[row[0]]['P'] += 1

    ordered = sorted(table.keys(),
                     key=lambda x: (-table[x]['P'], x.lower()))

    result = ["Team                           | MP |  W |  D |  L |  P"]

    fmt = '{:30} |{:3} |{:3} |{:3} |{:3} |{:3}'

    for team in ordered:
        result.append(fmt.format(team, table[team]['MP'], table[team]['W'],
                      table[team]['D'], table[team]['L'], table[team]['P']))

    

print(tally(["Allegoric Alaskans;Blithering Badgers;win", "Blithering Badgers;Courageous Californians;win", "Courageous Californians;Allegoric Alaskans;loss"]))