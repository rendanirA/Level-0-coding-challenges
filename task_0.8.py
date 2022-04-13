def convert_any_number_to_time(num):
    hour = num // 60
    minutes = num % 60

    if num == 60:
        print(hour, "Hour ,", minutes, "minute")
    elif num <= 119:
        print(hour, "hour ,", minutes, "minutes")
    else:
        print(hour, "Hours ,", minutes, "minutes")


convert_any_number_to_time(133)
