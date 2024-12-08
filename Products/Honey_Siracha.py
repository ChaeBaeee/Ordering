from pathlib import Path
from other_flavors import create_other_flavors_content  # Import the function
from cart import create_cart_content, load_items, add_to_cart  # Import the functions

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json  # Import json module

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame10")

DATABASE_PATH = Path(r"C:\Users\pilim\Desktop\Ordering\database.json")  # Ensure this path is correct

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def save_cart(cart):
    with open(DATABASE_PATH, 'r+') as file:
        data = json.load(file)
        data["cart"] = cart
        file.seek(0)
        json.dump(data, file)
        file.truncate()

def load_cart():
    with open(DATABASE_PATH, 'r') as file:
        data = json.load(file)
        return data.get("cart", [])

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def create_honey_siracha_content(window):
    items = load_items()  # Refresh items from database
    honey_sriracha_price = items["Honey Sriracha"]["price"]  # Ensure the key matches the database
    honey_sriracha_stock = items["Honey Sriracha"]["stock"]  # Ensure the key matches the database
    print("Creating Honey Sriracha content...")
    for widget in window.winfo_children():
        widget.destroy()  # Clear existing content

    window.geometry("507x782")
    window.configure(bg = "#F9A825")

    canvas = Canvas(
        window,
        bg = "#F9A825",
        height = 782,
        width = 507,
        bd = 0,
        highlightthickness=0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        558.1047973632812,
        238.781005859375,
        anchor="nw",
        text="Burger",
        fill="#000000",
        font=("Abril Fatface", 12 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_to_cart("Honey Sriracha", quantity) or print(f"Added {quantity} Honey Sriracha to cart"),  # Add Honey Sriracha to cart with quantity and print confirmation
        relief="flat"
    )
    button_1.place(
        x=344.83306884765625,
        y=713.2791748046875,
        width=138.046875,
        height=39.11162567138672
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_cart_content(window),  # Change this line
        relief="flat"
    )
    button_2.place(
        x=351.87994384765625,
        y=21.2791748046875,
        width=126.0,
        height=41.0
    )

    canvas.create_rectangle(
        -0.4979572594165802,
        697.3170206485199,
        507.94146728515625,
        697.91845703125,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        18.142320811748505,
        322.2070179723996,
        490.920166015625,
        322.750244140625,
        fill="#000000",
        outline="")

    canvas.create_text(
        42.4671630859375,
        343.134521484375,
        anchor="nw",
        text="Honey Sriracha (4pcs)",
        fill="#000000",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        42.4671630859375,
        417.876708984375,
        anchor="nw",
        text=f"Php {honey_sriracha_price}",  # Use the dynamic price
        fill="#000000",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        35.67242431640625,
        492.618896484375,
        anchor="nw",
        text="Sweet honey combined with spicy Sriracha,\ncreating a perfect blend of heat and sweetness on\neach wing.",
        fill="#000000",
        font=("Abril Fatface", 20 * -1)
    )

    quantity = 1  # Initialize quantity

    def update_quantity_display():
        canvas.itemconfig(quantity_text, text=str(quantity))

    def increment_quantity():
        nonlocal quantity
        quantity += 1
        update_quantity_display()

    def decrement_quantity():
        nonlocal quantity
        if quantity > 1:
            quantity -= 1
            update_quantity_display()

    quantity_text = canvas.create_text(
        107.87994384765625,
        723.2791748046875,
        anchor="nw",
        text=str(quantity),
        fill="#000000",
        font=("Abril Fatface", 18 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=increment_quantity,
        relief="flat"
    )
    button_3.place(
        x=137.59344482421875,
        y=725.3387451171875,
        width=27.178970336914062,
        height=27.178970336914062
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=decrement_quantity,
        relief="flat"
    )
    button_4.place(
        x=59.45404052734375,
        y=723.64013671875,
        width=27.178970336914062,
        height=27.178970336914062
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        252.19610595703125,
        194.31475830078125,
        image=image_image_1
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        window,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_other_flavors_content(window),  # Go back to other flavors window
        relief="flat"
    )
    button_5.place(
        x=18.87994384765625,
        y=23.2791748046875,
        width=33.0,
        height=29.0
    )

    # Keep a reference to the images to prevent garbage collection
    window.button_images = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, image_image_1]

    window.resizable(False, False)
    print("Honey Sriracha content created successfully.")
