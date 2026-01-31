menu = {
    'Pizza': 100,
    'Coffee': 40,
    'Burger': 120,
    'pasta': 180,
}

print("Welcome to our Pytho Cafe!")
print("Here Is Our Hotel Menu:")
print("Pizza = Rs.100\nCoffee = Rs.40\nBurger = Rs.120\nPasta = Rs.180")

order_total = 0

# First order
item = input("Enter your 1st item: ")
if item in menu:
    order_total += menu[item]
    print(f"Your 1st item {item} is added to your order.")
else:
    print(f"Your Ordered item {item} is not available.")

# Loop for and More more orders
while True:
    another_order = input("Would you like to order more? Yes/No: ")

    if another_order == "Yes":
        item = input("Enter your Next item: ")
        if item in menu:
            order_total += menu[item]
            print(f"Your item {item} is added to your order.")

        else:
            print(f"Your Ordered item {item} is not available.")
    
    elif another_order == "No":
        break
    
    else:
        print("Please enter Yes or No only.")

        


print(f"\nThank You For Ordering! Your Total Bill is Rs.{order_total}")
