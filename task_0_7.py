def convert_celsius_to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32


fahrenheit = convert_celsius_to_fahrenheit(120)
print(fahrenheit)


def covert_fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius = covert_fahrenheit_to_celcius(32)
print(celsius)
