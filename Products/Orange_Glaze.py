from pathlib import Path
from other_flavors import create_other_flavors_content
from cart import create_cart_content, load_items, add_to_cart
import json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox  # Ensure all necessary imports are included

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets/frame16")

DATABASE_PATH = Path("database.json")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def save_cart(cart):
    with open(DATABASE_PATH, 'r+') as file:
        data = json.load(file)
        data["cart"] = cart
        file.seek (0)
        json.dump(data, file)
        file.truncate()

def load_cart():
    with open(DATABASE_PATH, 'r') as file:
        data = json.load(file)
        return data.get("cart", [])

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def create_orange_glaze_content(window):
    items = load_items()
    orange_glaze_price = items["Orange Glaze"]["price"]
    orange_glaze_stock = items["Orange Glaze"]["stock"]
    print("Creating Orange Glaze content...")
    for widget in window.winfo_children():
        widget.destroy()

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
        command=lambda: add_to_cart("Orange Glaze", quantity),
        relief="flat",
        state="disabled" if orange_glaze_stock == 0 else "normal",
        bg="grey" if orange_glaze_stock == 0 else "SystemButtonFace"
    )
    if orange_glaze_stock == 0:
        canvas.create_text(
            344.83306884765625,
            690.177001953125,  # Positioned above the button
            anchor="nw",
            text="Out of Stock",
            fill="red",
            font=("Abril Fatface", 16 * -1)
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
        command=lambda: create_cart_content(window),
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
        text=f"Php {orange_glaze_price}",
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

    quantity = 1

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
        724.177001953125,
        anchor="nw",
        text=str(quantity),
        fill="#000000",
        font=("Abril Fatface", 18 * -1)
    )

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
    button_3.image = button_image_3
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
    button_4.image = button_image_4
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
        command=lambda: create_other_flavors_content(window),
        relief="flat"
    )
    button_5.place(
        x=18.87994384765625,
        y=26.177001953125,
        width=33.0,
        height=29.0
    )

    window.button_images = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, image_image_1]

    window.resizable(False, False)
    print("Sesame Honey content created successfully.")
