# Shopping Cart program-

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"The total is {total}")
print("Thankyou for coming:)")
