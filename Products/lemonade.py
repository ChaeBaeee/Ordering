from pathlib import Path
from drinks import create_drinks_content  # Import the function
from cart import create_cart_content, load_items, add_to_cart  # Import the functions

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets/frame22")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_lemonade_content(window):
    items = load_items()  # Refresh items from database
    if "Lemonade" not in items:
        print("Error: 'Lemonade' not found in items")
        return  # Exit the function if the key is not found
    lemonade_price = items["Lemonade"]["price"]  # Get the price of Lemonade
    lemonade_stock = items["Lemonade"]["stock"]  # Get the stock of Lemonade
    quantity = 1  # Initialize quantity variable
    print("Creating Lemonade content...")
    for widget in window.winfo_children():
        widget.destroy()  # Clear existing content

    window.geometry("507x782")
    window.configure(bg = "#FFD700")


    canvas = Canvas(
        window,
        bg = "#FFD700",
        height = 782,
        width = 507,
        bd = 0,
        highlightthickness=0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_to_cart("Lemonade", quantity),  # Remove popup message
        relief="flat",
        state="disabled" if lemonade_stock == 0 else "normal",  # Disable if stock is 0
        text="Unavailable" if lemonade_stock == 0 else ""  # Add "Unavailable" text if stock is 0
    )
    button_1.place(
        x=344.0,
        y=712.0,
        width=140.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_cart_content(window),  # Change this line
        relief="flat"
    )
    button_2.place(
        x=352.0,
        y=21.0,
        width=126.0,
        height=41.0
    )

    canvas.create_rectangle(
        -0.4979572594165802,
        697.3168375430512,
        507.94146728515625,
        697.9182739257812,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        18.142320811748505,
        322.2070179723996,
        490.920166015625,
        322.750244140625,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        42.467041015625,
        343.1343994140625,
        anchor="nw",
        text="Lemonade (22oz)",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        42.467041015625,
        417.8765869140625,
        anchor="nw",
        text=f"Php {lemonade_price}",  # Use the dynamic price
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        35.67236328125,
        492.6188049316406,
        anchor="nw",
        text="Freshly squeezed lemons, lightly sweetened and served over ice for a zesty, refreshing treat.",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    quantity_text = canvas.create_text(
        107.158203125,
        724.979736328125,
        anchor="nw",
        text=str(quantity),
        fill="#FFFFFF",
        font=("Abril Fatface", 18 * -1)
    )

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
        x=137.593505859375,
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
        x=59.4541015625,
        y=723.6400756835938,
        width=27.178970336914062,
        height=27.178970336914062
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        window,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_drinks_content(window),  # Go back to drinks window
        relief="flat"
    )
    button_5.place(
        x=21.158203125,
        y=21.979736328125,
        width=33.0,
        height=29.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        255.0,
        192.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
