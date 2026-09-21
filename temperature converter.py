#temperature converter machine
temp_val= float(input("enter the temperature value only:"))
temp_unit= input("enter C for celsius to convert to fahrenheit and F for faraheint to convert to celsius:")
if temp_unit=="C":
    converter=(9*temp_val)/5+32
    print(f"temperature in Faraheint is {converter}F")
elif temp_unit=="F":
    converter=(temp_val-32)*5/9
    print(f"temperature in Celsius is {converter}C")
else:
    print(f"{temp_unit} is invalid")
    