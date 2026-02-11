inventory = {}
def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {}
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")
    return

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        new_stock = inventory[item]["stock"] + quantity
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")
    return

def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        current_stock = inventory[item]["stock"]
        return current_stock

def sales_report(sales):
    total = 0
    for item, quantity_sold in sales.items(): # Using .items() is cleaner
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        else:
            # Check if we have enough to sell
            if inventory[item]["stock"] >= quantity_sold:
                # FIX: Multiply price by quantity_sold, NOT total stock
                item_revenue = quantity_sold * inventory[item]["price"]
                total += item_revenue
                
                # Deduct the sold amount from stock
                inventory[item]["stock"] -= quantity_sold
            else:
                print(f"Error: Insufficient stock for '{item}'.")
    
    return f"Total revenue: ${total:.2f}"



#Test
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
