from random import randint 
def lot6(kuchi):
    for i in range (kuchi):
        number = list()
        while True:
            roll = randint(1,34)
            if not roll in number:
                number.append(roll)
            if len (number) == 6:
                break
        number.sort()
        print(number)


while True:
    kuchi = int(input("何口買いますか？"))
    if not kuchi == 0:
        lot6(kuchi)
    else:
        break



 