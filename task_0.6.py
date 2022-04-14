def max_number(number1, number2, number3):

    if number1 > number2 and number1 > number3:
        print(number1, " is a maximum value")
    elif number2 > number1 and number2 > number3:
        print(number2, " is a maximum value")
    elif number3 > number1 and number3 > number2:
        print(number3, " is a maximum value")


print(max_number(9, 81, 10))
