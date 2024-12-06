# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from bestseller import create_bestseller_content  # Import the function

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame13")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_garlic_parmesan_content(window):
    print("Creating Garlic Parmesan content...")
    window.geometry("507x782")
    window.configure(bg = "#88D498")

    canvas = Canvas(
        window,
        bg = "#88D498",
        height = 782,
        width = 507,
        bd = 0,
        highlightthickness=0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        558.1048583984375,
        238.7808837890625,
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
        x=344.8331298828125,
        y=713.4481201171875,
        width=138.324951171875,
        height=39.13037109375
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=352.1580810546875,
        y=20.5784912109375,
        width=126.0,
        height=42.0
    )

    canvas.create_rectangle(
        -0.4979572594165802,
        697.3168985782077,
        507.94146728515625,
        697.9183349609375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        18.142320811748505,
        322.2071400427121,
        490.920166015625,
        322.7503662109375,
        fill="#000000",
        outline="")

    canvas.create_text(
        42.4671630859375,
        343.1346435546875,
        anchor="nw",
        text="Garlic Parmesan (4pcs)",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        42.4671630859375,
        417.8768310546875,
        anchor="nw",
        text="Php 999 ",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        35.6724853515625,
        492.6190185546875,
        anchor="nw",
        text="Tender wings drenched in a buttery garlic sauce,\ntopped with Parmesan for a creamy and savory\ntaste.",
        fill="#FFFFFF",
        font=("Abril Fatface", 20 * -1)
    )

    canvas.create_text(
        108.1580810546875,
        723.5784912109375,
        anchor="nw",
        text="1",
        fill="#FFFFFF",
        font=("Abril Fatface", 18 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=137.593505859375,
        y=725.3389892578125,
        width=27.178970336914062,
        height=27.178970336914062
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=59.4539794921875,
        y=723.6402587890625,
        width=27.178970336914062,
        height=27.178970336914062
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        252.1961669921875,
        192.646240234375,
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
        y=21.5784912109375,
        width=33.0,
        height=29.0
    )

    # Keep a reference to the images to prevent garbage collection
    window.button_images = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, image_image_1]

    window.resizable(False, False)
    print("Garlic Parmesan content created successfully.")
