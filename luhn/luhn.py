class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        #Checks if input has anything not supposted to be in it. 
        new_card_num = self.card_num.replace(" ", '')
        if any(char.isalpha() for char in new_card_num):
            return False
        for digit in new_card_num:
            current_dig = digit.isnumeric()
            if current_dig == False:
                 return False
        if len(new_card_num.strip()) <= 1:
            return False

        #Start of algorithim
        list_of_numbers = [int(i) for i in new_card_num[:-1]]
        total = 0
        
        print("First set of numbers")
        print(list_of_numbers)
        lst = [i for i in range(len(list_of_numbers), 1, -2)]
        lst.append(1)
        for index in lst:
            print(index)
            n = list_of_numbers[-index] * 2
            if n > 9:
                n -= 9
            list_of_numbers[-index] = n
        print("Second set of numbers")
        print(list_of_numbers)
        for i in list_of_numbers:
            total += i
        total += int(new_card_num[-1])
        print("Total")
        print(total)
        if total % 10 == 0:
            return True
        else:
            return False




card = Luhn("055 444 285")

print(card.valid())

