sales = [
   {"item": "Laptop", "qty": 2, "price": 50000},
   {"item": "Mouse", "qty": 5, "price": 500},
   {"item": "Keyboard", "qty": 3, "price": 700},
]


# 1. Print total revenue
# Revenue = qty × price for each item.
total_revenue = 0
for s in sales:
    total_revenue += s["qty"] * s["price"]

print("Total Revenue:", total_revenue)


# 2. Print the item with highest qty

highest_qty_item = max(sales, key=lambda s: s["qty"])
print("Item with highest quantity:", highest_qty_item["item"])


# 3. Create a list of only item names

item_names = [s["item"] for s in sales]
print("Item names:", item_names)