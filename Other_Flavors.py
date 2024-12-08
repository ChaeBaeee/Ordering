# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from bestseller import create_bestseller_content  # Import the function
from cart import load_cart, load_items  # Add the missing imports

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_other_flavors_content(window):
    print("Creating Other Flavors content...")
    window.geometry("507x782")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 782,
        width = 507,
        bd = 0,
        highlightthickness=0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        149.5185546875,
        220.48944091796875,
        anchor="nw",
        text="Honey Sriracha",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
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
        3.397216796875,
        404.287109375,
        anchor="nw",
        text="Other Flavors",
        fill="#000000",
        font=("Abril Fatface", 16 * -1)
    )

    canvas.create_text(
        28.87744140625,
        603.0333862304688,
        anchor="nw",
        text="Drinks",
        fill="#000000",
        font=("Abril Fatface", 16 * -1)
    )

    canvas.create_text(
        147.785400390625,
        438.2608642578125,
        anchor="nw",
        text="Orange Glaze",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        341.435546875,
        439.9595642089844,
        anchor="nw",
        text="Sesame Honey",
        fill="#000000",
        font=("Abril Fatface", 14 * -1)
    )

    canvas.create_text(
        338.038330078125,
        220.82916259765625,
        anchor="nw",
        text="Lemon Pepper",
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

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_drinks(window),
        relief="flat"
    )
    button_1.image = button_image_1  # Keep a reference to the image
    button_1.place(
        x=23.81591796875,
        y=536.4450073242188,
        width=60.16745376586914,
        height=60.167457580566406
    )

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_best_sellers(window),
        relief="flat"
    )
    button_2.image = button_image_2  # Keep a reference to the image
    button_2.place(
        x=23.81591796875,
        y=110.0748291015625,
        width=60.16745376586914,
        height=60.167457580566406
    )

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.image = button_image_3  # Keep a reference to the image
    button_3.place(
        x=25.480224609375,
        y=327.84625244140625,
        width=60.16745376586914,
        height=60.167457580566406
    )

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_honey_siracha(window),
        relief="flat"
    )
    button_4.image = button_image_4  # Keep a reference to the image
    button_4.place(
        x=118.41552734375,
        y=65.65020751953125,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_lemon_pepper(window),
        relief="flat"
    )
    button_5.image = button_image_5  # Keep a reference to the image
    button_5.place(
        x=305.254638671875,
        y=65.730712890625,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_6 = PhotoImage(file=relative_to_assets("button_7.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_sesame_honey(window),
        relief="flat"
    )
    button_6.image = button_image_6  # Keep a reference to the image
    button_6.place(
        x=305.254638671875,
        y=284.09515380859375,
        width=148.88934326171875,
        height=148.88937377929688
    )

    button_image_7 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_orange_glaze(window),
        relief="flat"
    )
    button_7.image = button_image_7  # Keep a reference to the image
    button_7.place(
        x=116.024169921875,
        y=284.09515380859375,
        width=148.88934326171875,
        height=148.88937377929688
    )

    canvas.create_text(
        184.41552734375,
        16.9869384765625,
        anchor="nw",
        text="Other Flavors",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    button_8 = Button(
        window,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_order(window),
        relief="flat"
    )
    button_8.image = button_image_8  # Keep a reference to the image
    button_8.place(
        x=16.986572265625,
        y=721.94140625,
        width=99.83250427246094,
        height=38.94280242919922
    )

    button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_cart(window),  # Change command to open_cart
        relief="flat"
    )
    button_9.image = button_image_9  # Keep a reference to the image
    button_9.place(
        x=361.81982421875,
        y=721.94140625,
        width=124.00406646728516,
        height=38.58948516845703
    )

    # Keep a reference to the images to prevent garbage collection
    window.button_images = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6, button_image_7, button_image_8, button_image_9]

    window.resizable(False, False)
    print("Other Flavors content created successfully.")

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def open_drinks(window):
    try:
        print("Opening Drinks...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent))
        from drinks import create_drinks_content
        create_drinks_content(window)
        
        # Add a button to go back to the other flavors window
        button_image_back = PhotoImage(file=relative_to_assets("button_8.png"))  # Ensure the correct image is used
        button_back = Button(
            window,
            image=button_image_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: create_other_flavors_content(window),
            relief="flat"
        )
        button_back.place(
            x=17.394775390625,
            y=721.94140625,
            width=99.83250427246094,
            height=38.94280242919922
        )
        window.button_images.append(button_image_back)  # Keep a reference to the image
        
        print("Drinks opened successfully.")
    except Exception as e:
        print(f"Failed to open Drinks: {e}")

def open_honey_siracha(window):
    try:
        print("Opening Honey Siracha...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "products"))
        from Honey_Siracha import create_honey_siracha_content
        create_honey_siracha_content(window)
        print("Honey Siracha opened successfully.")
    except Exception as e:
        print(f"Failed to open Honey Siracha: {e}")

def open_lemon_pepper(window):
    try:
        print("Opening Lemon Pepper...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "products"))
        from Lemon_Pepper import create_lemon_pepper_content
        create_lemon_pepper_content(window)
        print("Lemon Pepper opened successfully.")
    except Exception as e:
        print(f"Failed to open Lemon Pepper: {e}")

def open_sesame_honey(window):
    try:
        print("Opening Sesame Honey...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "products"))
        from Sesame_Honey import create_sesame_honey_content
        import sys
        sys.path.append(str(Path(__file__).parent / "products"))
        from Sesame_Honey import create_sesame_honey_content
        create_sesame_honey_content(window)
        print("Sesame Honey opened successfully.")
    except Exception as e:
        print(f"Failed to open Sesame Honey: {e}")

def open_orange_glaze(window):
    try:
        print("Opening Orange Glaze...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent / "products"))
        from Orange_Glaze import create_orange_glaze_content
        create_orange_glaze_content(window)
        print("Orange Glaze opened successfully.")
    except Exception as e:
        print(f"Failed to open Orange Glaze: {e}")

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
