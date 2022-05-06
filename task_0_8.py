def convert_any_number_to_time(num):
    hour = num // 60
    minutes = num % 60
    if hour == 0 or hour >= 1 and minutes == 0 or minutes > 1:
        print(f"{hour} hour{'s'} , {minutes} minute{'s'}  ")
    elif hour == 0 or hour > 1 and minutes == 0 or minutes > 1:
        print(f"{hour} hour{'s'} , {minutes} minute{'s'}  ")


convert_any_number_to_time(60)
