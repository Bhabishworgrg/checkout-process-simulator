stock = {"apple": 35, "banana": 18, "orange": 26}

stockList = [f"{key} ({value}p)" for key, value in stock.items()]
stockString = " - ".join(stockList)

print(f"Welcome to the Shop!\n\nCurrently in stock: {stockString}\nPick an item, or Enter to Checkout.")

basket = []
price = 0

while True:
    choice = input("Choice --> ")

    if choice == "":
        break

    for item in stock:
        if choice == item:
            break
    else:
        print("No such item. Try again.")
        continue
    
    print("Item added.")
    
    basket.append(choice)
    price += stock[choice]

basketString = " - ".join(basket)

print(f"Thank you. You have purchased {basketString} at a cost of {price}p")
