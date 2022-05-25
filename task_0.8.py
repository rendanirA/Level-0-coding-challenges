def convert_numbers_to_time(num):
    hours = num // 60
    minutes = num % 60
    hours_string = "hour"
    minutes_string = "minute"

    if hours != 1:
        hours_string = "hours"
    if minutes != 1:
        minutes_string = "minutes"
    results = f"{hours} {hours_string}, {minutes} {minutes_string}"
    return results


print(convert_numbers_to_time(60))
