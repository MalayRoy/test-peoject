# Write a Python program that takes a temperature input
# in Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to
# Kelvin if the temperature is below 0°C.


celsius = float(input("Enter the temperature in Celsius: "))

if celsius > 0:   
    fahrenheit = (celsius * 9/5) + 32
    print("The temperature in Fahrenheit is: " +str(fahrenheit)+ "°F")
elif celsius < 0:    
    kelvin = celsius + 273.15
    print("The temperature in Kelvin is: " +str(kelvin)+ "K")
else:
    print("The temperature is exactly 0°C.")