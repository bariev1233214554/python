number = int(input('Введите число: '))
if number % 2 == 0 and number > 0:
    print ("число положительное, четное")
if number % 2 == 0 and number < 0:
        print ("число отрицательное, четное")
if not number % 2 == 0 and number > 0:
    print ("число положительное, нечетное")
if not number % 2 == 0 and number < 0:
    print ("число отрицательное, нечетное")
if number == 0:
    print ("число равно нулю")
