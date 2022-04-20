def convert_any_number_to_time(num):
    hour = num // 60
    minutes = num % 60

    if num // 60 == 1 and num % 60 == 0:
        print(hour, "Hour ,", minutes, "minute")
    elif num // 60 == 1 and num % 60 == 1:
        print(hour, "hour ,", minutes, "minute")
    elif num // 60 == 1 and num % 60 > 1:
        print(hour, "Hour ,", minutes, "minutes")
    elif num // 60 > 1 and num % 60 == 0:
        print(hour, "Hours ,", minutes, "minute")
    elif num // 60 > 1 and num % 60 == 1:
        print(hour, "Hours ,", minutes, "minute")
    elif num // 60 > 1 and num % 60 > 1:
        print(hour, "Hours ,", minutes, "minutes")
    else:
        print(hour, "Hours ,", minutes, "minutes")


convert_any_number_to_time(242)
