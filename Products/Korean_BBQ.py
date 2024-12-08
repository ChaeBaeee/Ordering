# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from bestseller import create_bestseller_content  # Import the function
from cart import create_cart_content  # Import the function


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame15")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_korean_bbq_content(window):
    print("Creating Korean BBQ content...")
    window.geometry("507x782")
    window.configure(bg = "#2E2E2E")

    canvas = Canvas(
        window,
        bg = "#2E2E2E",
        height = 782,
        width = 507,
        bd = 0,
        highlightthickness=0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        558.1048583984375,
        238.781005859375,
        anchor="nw",
        text="Burger",
        fill="#000000",
        font=("Abril Fatface", 12 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=344.1580810546875,
        y=712.87744140625,
        width=139.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_cart_content(window),  # Navigate to cart content
        relief="flat"
    )
    button_2.place(
        x=352.1580810546875,
        y=20.87744140625,
        width=126.0,
        height=41.0
    )

    canvas.create_rectangle(
        -0.4979572594165802,
        697.3170206485202,
        507.94146728515625,
        697.91845703125,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        18.142320811748505,
        322.2072621130246,
        490.920166015625,
        322.75048828125,
        fill="#000000",
        outline="")

    canvas.create_text(
        42.4671630859375,
        343.134765625,
        anchor="nw",
        text="Korean BBQ (4pcs)",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        42.4671630859375,
        417.87646484375,
        anchor="nw",
        text="Php 999 ",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        35.6724853515625,
        492.618896484375,
        anchor="nw",
        text="Crispy wings glazed with a sweet, smoky Korean\nBBQ sauce, bringing a tangy and spicy kick.",
        fill="#FFFFFF",
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
        108.1580810546875,
        723.87744140625,
        anchor="nw",
        text=str(quantity),
        fill="#FFFFFF",
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
        x=137.593505859375,
        y=725.3388671875,
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
        x=59.4539794921875,
        y=723.64013671875,
        width=27.178970336914062,
        height=27.178970336914062
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        252.1961669921875,
        192.659423828125,
        image=image_image_1
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        window,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_bestseller_content(window),  # Go back to bestseller window
        relief="flat"
    )
    button_5.place(
        x=19.1580810546875,
        y=21.87744140625,
        width=33.0,
        height=29.0
    )

    # Keep a reference to the images to prevent garbage collection
    window.button_images = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, image_image_1]

    window.resizable(False, False)
    print("BBQ content created successfully.")
