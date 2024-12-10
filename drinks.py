# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame3")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def calculate_order_total():
    from cart import load_cart, load_items
    cart = load_cart()
    items = load_items()
    total = sum(item["quantity"] * items[item["item"]]["price"] for item in cart)
    return total

def update_order_total(canvas):
    total = calculate_order_total()
    canvas.itemconfig(order_total_text, text=f"P {total}")

def create_drinks_content(window):
    # Reuse the existing code to create the drinks content
    window.geometry("507x782")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=782,
        width=507,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        144.796142578125,
        220.82916259765625,
        anchor="nw",
        text="Classic Iced Tea",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        217.968994140625,
        21.4119873046875,
        anchor="nw",
        text="Drinks",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    canvas.create_text(
        8.52783203125,
        184.81707763671875,
        anchor="nw",
        text="Best Sellers",
        fill="#000000",
        font=("Abril Fatface", 16 * -1)
    )

    canvas.create_text(
        3.397705078125,
        404.287109375,
        anchor="nw",
        text="Other Flavors",
        fill="#000000",
        font=("Abril Fatface", 16 * -1)
    )

    canvas.create_text(
        25.887939453125,
        601.334716796875,
        anchor="nw",
        text="Drinks",
        fill="#000000",
        font=("Abril Fatface", 16 * -1)
    )

    canvas.create_text(
        160.084228515625,
        439.9595642089844,
        anchor="nw",
        text="Coca-Cola",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        243.31982421875,
        657.3912963867188,
        anchor="nw",
        text="Root Beer Float",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        363.926513671875,
        439.9595642089844,
        anchor="nw",
        text="Pepsi",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        350.3369140625,
        220.82916259765625,
        anchor="nw",
        text="Lemonade",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        558.104736328125,
        238.7806396484375,
        anchor="nw",
        text="Burger",
        fill="#000000",
        font=("Abril Fatface", 12 * -1)
    )

    canvas.create_rectangle(
        -0.4979572594165802,
        697.3169596133637,
        507.94146728515625,
        697.9183959960938,
        fill="#000000",
        outline="")

    # Keep a reference to the images to prevent garbage collection
    if not hasattr(window, 'button_images'):
        window.button_images = []

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    window.button_images.append(button_image_1)
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_order(window),  # Changed command here
        relief="flat"
    )
    button_1.place(
        x=23.816162109375,
        y=536.4450073242188,
        width=60.16745376586914,
        height=60.167457580566406
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    window.button_images.append(button_image_2)
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_best_sellers(window),
        relief="flat"
    )
    button_2.place(
        x=23.816162109375,
        y=110.0748291015625,
        width=60.16745376586914,
        height=60.167457580566406
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    window.button_images.append(button_image_3)
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_other_flavors(window),
        relief="flat"
    )
    button_3.place(
        x=23.78173828125,
        y=327.84625244140625,
        width=60.16745376586914,
        height=60.167457580566406
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    window.button_images.append(button_image_4)
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_ice_tea(window),  # Open ice_tea.py
        relief="flat"
    )
    button_4.place(
        x=116.024169921875,
        y=65.73040771484375,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    window.button_images.append(button_image_5)
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_lemonade(window),  # Open lemonade.py
        relief="flat"
    )
    button_5.place(
        x=305.254638671875,
        y=65.730712890625,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))  # Fixed missing file argument
    window.button_images.append(button_image_6)
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_coca_cola(window),  # Open coca_cola.py
        relief="flat"
    )
    button_6.place(
        x=116.024658203125,
        y=280.2830810546875,
        width=148.88934326171875,
        height=152.70135498046875
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    window.button_images.append(button_image_7)
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_pepsi(window),  # Open pepsi.py
        relief="flat"
    )
    button_7.place(
        x=305.254638671875,
        y=284.09515380859375,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    window.button_images.append(button_image_8)
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_root_beer(window),  # Open root_beer.py
        relief="flat"
    )
    button_8.place(
        x=214.4423828125,
        y=499.4135437011719,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    window.button_images.append(button_image_9)
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),  # Changed command here
        relief="flat"
    )
    button_9.place(
        x=17.394775390625,
        y=721.94140625,
        width=99.83250427246094,
        height=38.94280242919922
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    window.button_images.append(button_image_10)
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_cart(window),  # Change command to open_cart
        relief="flat"
    )
    button_10.place(
        x=362.227783203125,
        y=721.94140625,
        width=124.00406646728516,
        height=38.58948516845703
    )

    canvas.create_rectangle(
        188.9619140625,
        708.3519287109375,
        319.7607116699219,
        772.901985168457,
        fill="#1A4524",
        outline="")

    canvas.create_text(
        204.25,
        716.8453369140625,
        anchor="nw",
        text="Order Total",
        fill="#FBFBFB",
        font=("Abril Fatface", 18 * -1)
    )

    global order_total_text
    order_total_text = canvas.create_text(
        204.25,
        737.2295532226562,
        anchor="nw",
        text=f"P {calculate_order_total()}",
        fill="#FBFBFB",
        font=("Abril Fatface", 18 * -1)
    )

    # Call update_order_total whenever the order changes
    update_order_total(canvas)

    window.resizable(False, False)

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def open_best_sellers(window):
    try:
        print("Opening Best Sellers...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent))
        from bestseller import create_bestseller_content
        create_bestseller_content(window)
        print("Best Sellers opened successfully.")
    except Exception as e:
        print(f"Failed to open Best Sellers: {e}")

def open_other_flavors(window):
    try:
        print("Opening Other Flavors...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent))
        from other_flavors import create_other_flavors_content
        create_other_flavors_content(window)
        print("Other Flavors opened successfully.")
    except Exception as e:
        print(f"Failed to open Other Flavors: {e}")

def back_to_order(window):
    try:
        print("Going back to Order...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent))
        from order import create_main_window_content
        create_main_window_content(window)
        print("Order window opened successfully.")
    except Exception as e:
        print(f"Failed to open Order window: {e}")

def open_ice_tea(window):
    try:
        print("Opening Classic Iced Tea...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "Products"))
        from ice_tea import create_ice_tea_content
        print("Calling create_ice_tea_content...")
        create_ice_tea_content(window)
        print("Classic Iced Tea opened successfully.")
    except Exception as e:
        print(f"Failed to open Classic Iced Tea: {e}")

def open_coca_cola(window):
    try:
        print("Opening Coca-Cola...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "Products"))
        from coca_cola import create_coca_cola_content
        create_coca_cola_content(window)
        print("Coca-Cola opened successfully.")
    except Exception as e:
        print(f"Failed to open Coca-Cola: {e}")

def open_pepsi(window):
    try:
        print("Opening Pepsi...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "Products"))
        from pepsi import create_pepsi_content
        create_pepsi_content(window)
        print("Pepsi opened successfully.")
    except Exception as e:
        print(f"Failed to open Pepsi: {e}")

def open_root_beer(window):
    try:
        print("Opening Root Beer Float...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "Products"))
        from root_beer import create_root_beer_content
        create_root_beer_content(window)
        print("Root Beer Float opened successfully.")
    except Exception as e:
        print(f"Failed to open Root Beer Float: {e}")

def open_lemonade(window):
    try:
        print("Opening Lemonade...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "Products"))
        from lemonade import create_lemonade_content
        create_lemonade_content(window)
        print("Lemonade opened successfully.")
    except KeyError:
        print("Failed to open Lemonade: 'Lemonade' not found in items")
    except Exception as e:
        print(f"Failed to open Lemonade: {e}")

def open_cart(window):
    try:
        print("Opening Cart...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent))
        from cart import create_cart_content
        create_cart_content(window)
        print("Cart opened successfully.")
    except Exception as e:
        print(f"Failed to open Cart: {e}")