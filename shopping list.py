#a program to crate a shopping list
foods=[]
prices=[]
total=0

while True:
    food=input("Enter the foodstuffs you need to get(enter q to quit):")
    if food=="q":
        break
    else:
        price=float(input("Enter the price:"))
        foods.append(food)
        prices.append(price)
print("----YOUR ITEMS----")
for food in foods:
    print(food, end=" ")
for price in prices:
    total+=price

print()
print(f"your total is {total} naira")