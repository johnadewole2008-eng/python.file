Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #a simple calculator to calculate the compound interest 
... principal=0
... rate=0
... time=0
... 
... while principal<=0:
...     principal=float(input("enter principal amount: "))
...     if principal<=0:
...         print("you must input a value")
... 
... while rate<=0:
...     rate=float(input("enter interest rate: "))
...     if rate<=0:
...         print("you must input a value")
... 
... while time<=0:
...     time=int(input("enter time in years: "))
...     if time<=0:
...         print("you must input a value")
... 
... print(f"principal= {principal}")
... print(f"rate= {rate}")
... print(f"time= {time}")
... compound_interest= principal*pow((1+rate/100),time)
