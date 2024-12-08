# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def open_other_flavors(window):
    try:
        print("Opening Other Flavors...")
        clear_window(window)
        import sys
        sys.path.append(str(Path(__file__).parent.parent))
        from other_flavors import create_other_flavors_content
        create_other_flavors_content(window)
        print("Other Flavors opened successfully.")
    except Exception as e:
        print(f"Failed to open Other Flavors: {e}")

def open_cart(window):
    try:
        print("Opening Cart...")
        clear_window(window)
        from cart import create_cart_content
        create_cart_content(window)
        print("Cart opened successfully.")
    except Exception as e:
        print(f"Failed to open Cart: {e}")

def create_honey_siracha_content(window):
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
        command=lambda: print("button_1 clicked"),
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
        command=lambda: open_cart(window),  # Update this line
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
        text="Php 999 ",
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

    quantity_text = canvas.create_text(
        107.87994384765625,
        723.2791748046875,
        anchor="nw",
        text="1",
        fill="#000000",
        font=("Abril Fatface", 18 * -1)
    )

    def increment_quantity():
        current_quantity = int(canvas.itemcget(quantity_text, "text"))
        canvas.itemconfig(quantity_text, text=str(current_quantity + 1))

    def decrement_quantity():
        current_quantity = int(canvas.itemcget(quantity_text, "text"))
        if current_quantity > 1:
            canvas.itemconfig(quantity_text, text=str(current_quantity - 1))

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        window,
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
        window,
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
        command=lambda: open_other_flavors(window),
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
