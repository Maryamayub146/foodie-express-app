import os
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from rich.table import Table

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

console = Console()


products = [
    {"id": 1, "title": "Cheese Burger",        "price": 350},
    {"id": 2, "title": "Chicken Pizza",         "price": 600},
    {"id": 3, "title": "Zinger Burger",         "price": 400},
    {"id": 4, "title": "French Fries",          "price": 200},
    {"id": 5, "title": "Grilled Sandwich",      "price": 250},
    {"id": 6, "title": "Chicken Wings",         "price": 450},
    {"id": 7, "title": "Chicken Shawarma",      "price": 220},
    {"id": 8, "title": "Club Sandwich",         "price": 280},
    {"id": 9, "title": "Loaded Nachos",         "price": 350},
    {"id": 10, "title": "Hot Dog",              "price": 260},
    {"id": 11, "title": "Crispy Broast",        "price": 390},
    {"id": 12, "title": "Beef Burger",          "price": 380},
    {"id": 13, "title": "Garlic Mayo Fries",    "price": 240},
    {"id": 14, "title": "Stuffed Crust Pizza",  "price": 700},
    {"id": 15, "title": "Hotdog Deluxe",        "price": 270},
    {"id": 16, "title": "Mozzarella Sticks",    "price": 320},
    {"id": 17, "title": "Fried Chicken Bucket", "price": 850},
    {"id": 18, "title": "Chicken Tikka Pizza",  "price": 620},
    {"id": 19, "title": "Veggie Sandwich",      "price": 230},
    {"id": 20, "title": "Spicy Chicken Soap",   "price": 290},
]

def list_products():
    table = Table(title="🛒 Your Products")
    table.add_column("ID", justify="center")
    table.add_column("Title", justify="left")
    table.add_column("Price", justify="center")

    for p in products:
        table.add_row(str(p['id']), p['title'], f"Rs{p['price']}")

    console.print(table)

def search_product(keyword):
    matched = [p for p in products if keyword.lower() in p['title'].lower()]

    if matched:
        print(f"[bold green]Found {len(matched)} items matching '{keyword}':[/]")
        for p in matched:
            print(f"- {p['title']} - Rs{p['price']}")
    else:
        print(f"[red]No products found for '{keyword}'[/]")

def place_order(product_name):
    print(f"[bold cyan]✅ Order placed for '{product_name}'![/]")

def main():
    print("[bold magenta]🛍️ Welcome to Smart Shopping CLI Assistant![/]")
    while True:
        user_input = input("\n🤖 Enter command (list/search/order/exit): ").strip().lower()

        if user_input == "list":
            list_products()
        elif user_input == "search":
            keyword = input("🔍 Enter product keyword: ")
            search_product(keyword)
        elif user_input == "order":
            product_name = input("🛒 Enter product name to order: ")
            place_order(product_name)
        elif user_input == "exit":
            print("👋 Goodbye!")
            break
        else:
            print("[red]Invalid command. Try again.[/]")

if __name__ == "__main__":
    main()
