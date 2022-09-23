# This program validates credit card numbers.

num = int(input())

def checkCardNumber():
    counter = 0
    number = '0'
    
    cardNum = str(input())
    
    if cardNum[0] not in ('4', '5', '6'):
        return print('Invalid')
    elif len(cardNum) == 16 and cardNum.isnumeric():
        for n in cardNum:
            if n == number:
                counter += 1
            else:
                counter = 0
                number = n
            
            if counter == 3:
                return print('Invalid')
            
        return print('Valid')
    elif len(cardNum) == 19:
        for n in cardNum:
            if n != '-' and not n.isnumeric():
                return print('Invalid')
            elif (cardNum[4].isnumeric()) or (cardNum[9].isnumeric()) or (cardNum[14].isnumeric()):
                return print('Invalid')
            elif n == '-':
                continue
            
            if n == number:
                counter += 1
            else:
                counter = 0
                number = n
                continue
            
            if counter == 3:
                return print('Invalid')
            
        return print('Valid')
    else:
        return print('Invalid')

            
for x in range(num):
    checkCardNumber()
