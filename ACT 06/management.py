class Item:
    item_id = ""
    name = ""
    description = ""
    price = 0.0

items = []

while True:
    print("\nMenu:")
    print("1. Show All Items")
    print("2. Add Item")
    print("3. Edit Item")
    print("4. Delete Item")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        for item in items:
            print("ID:", item.item_id, "Name:", item.name, "Description:", item.description, "Price:", item.price)
    
    if choice == '2':
        try:
            new_item = Item()
            new_item.item_id = input("Enter Item ID: ")
            new_item.name = input("Enter Item Name: ")
            new_item.description = input("Enter Item Description: ")
            new_item.price = float(input("Enter Item Price: "))
            if new_item.price < 0:
                print("Price cannot be negative.")
            else:
                items.append(new_item)
                print("Item added successfully.")
        except ValueError:
            print("Invalid input. Price must be a number.")
    
    if choice == '3':
        item_id = input("Enter Item ID to edit: ")
        found = False
        for i in range(len(items)):
            if items[i].item_id == item_id:
                try:
                    items[i].name = input("Enter New Item Name: ")
                    items[i].description = input("Enter New Item Description: ")
                    new_price = float(input("Enter New Item Price: "))
                    if new_price < 0:
                        print("Price cannot be negative.")
                    else:
                        items[i].price = new_price
                        print("Item updated successfully.")
                        found = True
                except ValueError:
                    print("Invalid input. Price must be a number.")
        if not found:
            print("Item not found.")
    
    if choice == '4':
        item_id = input("Enter Item ID to delete: ")
        found = False
        for item in items:
            if item.item_id == item_id:
                items.remove(item)
                print("Item deleted successfully.")
                found = True
                break
        if not found:
            print("Item not found.")
    
    if choice == '5':
        print("Exiting...")
        break
    
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice, please try again.")
