import pandas as pd
import json

CSV_FILE = "products.csv"
JSON_FILE = "products.json"

# Ensure CSV exists with proper schema
def initialize_csv():
    try:
        pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Product ID", "Product Name", "Category", "Price", "Stock"])
        df.to_csv(CSV_FILE, index=False)

def add_product():
    pid = input("Enter Product ID: ")
    pname = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = input("Enter Price: ")
    stock = input("Enter Stock: ")

    df = pd.read_csv(CSV_FILE)
    new_row = {"Product ID": pid, "Product Name": pname, "Category": category, "Price": price, "Stock": stock}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    print("Product added successfully!")

def display_products():
    df = pd.read_csv(CSV_FILE)
    print("\n--- Product List ---")
    print(df)

def update_product():
    pid = input("Enter Product ID to update: ")
    df = pd.read_csv(CSV_FILE)

    if pid in df["Product ID"].astype(str).values:
        new_price = input("Enter new Price: ")
        new_stock = input("Enter new Stock: ")
        df.loc[df["Product ID"].astype(str) == pid, ["Price", "Stock"]] = [new_price, new_stock]
        df.to_csv(CSV_FILE, index=False)
        print("Product updated successfully!")
    else:
        print("Error: Product ID not found.")

def delete_product():
    pid = input("Enter Product ID to delete: ")
    df = pd.read_csv(CSV_FILE)

    if pid in df["Product ID"].astype(str).values:
        df = df[df["Product ID"].astype(str) != pid]
        df.to_csv(CSV_FILE, index=False)
        print("Product deleted successfully!")
    else:
        print("Error: Product ID not found.")

def export_to_json():
    df = pd.read_csv(CSV_FILE)
    df.to_json(JSON_FILE, orient="records", indent=4)
    print("Exported to products.json")

def display_json():
    try:
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
            print("\n--- JSON Data ---")
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("JSON file not found. Please export first.")

def menu():
    initialize_csv()
    while True:
        print("\n--- PRODUCT INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Export to JSON")
        print("6. Display JSON")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            export_to_json()
        elif choice == "6":
            display_json()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
