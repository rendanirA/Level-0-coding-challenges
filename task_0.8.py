def convert_any_number_to_time(num):
    hour = num // 60
    minutes = num % 60

    print(
        f"{hour} hour{'s' if hour > 1 else '' } , {minutes} minute{'s' if minutes >1 else ''}  "
    )


convert_any_number_to_time(90)
