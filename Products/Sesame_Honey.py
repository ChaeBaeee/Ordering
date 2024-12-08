# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame16")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_sesame_honey_content(window):
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
        558.1047973632812,
        238.780517578125,
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
        y=713.177001953125,
        width=138.046875,
        height=39.21379852294922
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_cart(window),
        relief="flat"
    )
    button_2.place(
        x=352.87994384765625,
        y=22.0830078125,
        width=124.45072174072266,
        height=39.093994140625
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
        322.2070179723996,
        490.920166015625,
        322.750244140625,
        fill="#000000",
        outline="")

    canvas.create_text(
        42.4671630859375,
        343.134521484375,
        anchor="nw",
        text="Orange Glaze (4pcs)",
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
        492.619140625,
        anchor="nw",
        text="Wings glazed in a tangy and sweet orange sauce,\nproviding a light and citrusy flavor for every bite.",
        fill="#000000",
        font=("Abril Fatface", 20 * -1)
    )

    quantity_text = canvas.create_text(
        107.87994384765625,
        724.177001953125,
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
    button_3.image = button_image_3  # Keep a reference to the image
    button_3.place(
        x=137.59344482421875,
        y=725.339111328125,
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
    button_4.image = button_image_4  # Keep a reference to the image
    button_4.place(
        x=59.45404052734375,
        y=723.639892578125,
        width=27.178970336914062,
        height=27.178970336914062
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        252.19610595703125,
        190.765380859375,
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
        y=26.177001953125,
        width=33.0,
        height=29.0
    )

    # Keep a reference to the images to prevent garbage collection
    window.button_images = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, image_image_1]

    window.resizable(False, False)

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
        import sys
        sys.path.append(str(Path(__file__).parent.parent))
        from Cart import create_cart_content
        create_cart_content(window)
        print("Cart opened successfully.")
    except Exception as e:
        print(f"Failed to open Cart: {e}")
