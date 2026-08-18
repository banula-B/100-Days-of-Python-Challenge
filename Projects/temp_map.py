# this is a tempreature converter

celsius = [0, 10, 20, 30, 40]

def temp_converter(celsius):
    return (celsius * 9 / 5) + 32

fahrenhite = list(map(temp_converter, celsius))

print(f"Temperature in Celsius: {celsius}")

print(f"Temperature in Fahrenheit: {fahrenhite}")
