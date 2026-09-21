#weight unit converter
weight= float(input("enter your weight:"))
convert= input("what do you want to convert to(K for kilogram or L for pounds)")
if convert=="K":
    output= weight/2.20462
    unit="lbs."
    print(f"your weight in kg is {round(output, 2)} {unit}")
elif convert=="L":
    output=weight*2.20462
    unit="lbs."
    print(f"your weight in pounds is {round(output, 2)} {unit}")
else:
    print(f"{convert} is invalid")