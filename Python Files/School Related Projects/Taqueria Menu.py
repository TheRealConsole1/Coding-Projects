menu =  {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cart = []
total = 0
print("----------------Menu---------------")
for key, value in menu.items():
    print(f"{key} ${value:.2f}")
print("-----------------------------------")

ordering = True
while ordering:
    try:
        order = input("Item: ").title()
        if order not in menu:
            pass
        else:
            total += menu.get(order)
            print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        break
    else:
        ...
