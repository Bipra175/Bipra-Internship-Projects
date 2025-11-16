# Program for Temperature Converter 
# Convert Celsius to Fahrenheit and Kelvin

# Asking the user to enter temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Converting Celsius to Kelvin
kelvin = celsius + 273.15

# Printing all the results
print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)
