def total(basket):
    def list_of_sets(basket):
        mylist = []
        while basket:
            this_set = set(basket)
            for elem in this_set:
                basket.remove(elem)
            mylist.append(len(this_set))
        return mylist
    
    list_num = list_of_sets(basket)
    print(list_num)

    set_price = {0: 0, 1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

    # we need to make an adjustment because you can save 40 cents by buying two sets of 4 books rather than sets of 5 and 3
    adjustment = 0
    if list_num.count(5) and list_num.count(3):
        adjustment += min(list_num.count(5), list_num.count(3)) * 40

    return sum(set_price[cnt] for cnt in list_num) - adjustment

basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]

print(total(basket))