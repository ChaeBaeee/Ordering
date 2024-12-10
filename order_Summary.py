# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
import json

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame7")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def save_addons_to_database(addons):
    with open('database.json', 'r+') as f:
        data = json.load(f)
        data['addons'] = addons
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def create_order_summary_content(window, page=0):
    for widget in window.winfo_children():
        widget.destroy()  # Clear existing content

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

    canvas.create_rectangle(
        -0.4979572594165802,
        697.3170206485199,
        507.94146728515625,
        697.91845703125,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        18.5360144674778,
        538.5360166603944,
        459.9996032714844,
        539.08984375,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        18.5362586081028,
        614.5360166603945,
        459.9998474121094,
        615.08984375,
        fill="#000000",
        outline=""
    )

    canvas.create_rectangle(
        18.5360144674778,
        621.4461729103945,
        459.9996032714844,
        622.0,
        fill="#000000",
        outline=""
    )

    canvas.create_text(
        171.0,
        46.0,
        anchor="nw",
        text="Order Summary",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    canvas.create_text(
        44.0,
        115.0,
        anchor="nw",
        text="Item name",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    canvas.create_text(
        223.0,
        115.0,
        anchor="nw",
        text="Quantity",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    canvas.create_text(
        386.0,
        115.0,
        anchor="nw",
        text="Price",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    with open('database.json', 'r') as f:
        data = json.load(f)
    
    cart = data['cart']
    items = data['items']
    addons = data.get('addons', [])  # Load add-ons from database.json

    total = 0

    # Calculate total for all cart items
    for item in cart:
        item_name = item['item']
        quantity = item['quantity']
        price = items[item_name]['price'] * quantity
        total += price

    # Calculate total for all add-ons
    for addon in addons:
        total += addon['price'] * addon['quantity']

    y_position = 150  # Starting y position for items
    font_size = 18  # Fixed font size
    spacing = 40  # Fixed spacing
    items_per_page = 10  # Number of items per page

    start_index = page * items_per_page
    end_index = start_index + items_per_page

    # Calculate the total number of pages for cart items
    total_cart_pages = (len(cart) + items_per_page - 1) // items_per_page

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png")
    )
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png")
    )

    if page < total_cart_pages:
        for item in cart[start_index:end_index]:
            item_name = item['item']
            quantity = item['quantity']
            price = items[item_name]['price'] * quantity

            canvas.create_text(
                44.0,
                y_position,
                anchor="nw",
                text=item_name,
                fill="#000000",
                font=("Abril Fatface", font_size * -1)
            )

            canvas.create_text(
                223.0,
                y_position,
                anchor="nw",
                text=str(quantity),
                fill="#000000",
                font=("Abril Fatface", font_size * -1)
            )

            canvas.create_text(
                386.0,
                y_position,
                anchor="nw",
                text=f"₱{price}",
                fill="#000000",
                font=("Abril Fatface", font_size * -1)
            )

            y_position += spacing  # Increment y position for next item

    elif page >= total_cart_pages:
        y_position += 20  # Add some space before the add-ons section

        # Display "Add-Ons :" text
        canvas.create_text(
            29.0,
            y_position,
            anchor="nw",
            text="Add-Ons :",
            fill="#000000",
            font=("Abril Fatface", 21 * -1)
        )
        y_position += spacing  # Adjust y position for add-ons

        addons_per_page = 6  # Number of add-ons per page
        start_addon_index = (page - total_cart_pages) * addons_per_page
        end_addon_index = start_addon_index + addons_per_page

        for addon in addons[start_addon_index:end_addon_index]:
            addon_name = addon['addon']
            quantity = addon['quantity']
            price = addon['price'] * quantity

            canvas.create_text(
                44.0,
                y_position,
                anchor="nw",
                text=addon_name,
                fill="#000000",
                font=("Abril Fatface", font_size * -1)
            )

            quantity_text = canvas.create_text(
                223.0,
                y_position,
                anchor="nw",
                text=str(quantity),
                fill="#000000",
                font=("Abril Fatface", font_size * -1)
            )

            canvas.create_text(
                386.0,
                y_position,
                anchor="nw",
                text=f"₱{price}",
                fill="#000000",
                font=("Abril Fatface", font_size * -1)
            )

            def update_quantity_display(q_text=quantity_text, q=quantity):
                canvas.itemconfig(q_text, text=str(q))

            def increment_quantity(a_name=addon_name, q_text=quantity_text):
                for addon in addons:
                    if addon['addon'] == a_name:
                        if addon['quantity'] < addon['stock']:  # Check if stock is available
                            addon['quantity'] += 1
                            update_quantity_display(q_text, addon['quantity'])
                        break
                save_addons_to_database(addons)
                create_order_summary_content(window)

            def decrement_quantity(a_name=addon_name, q_text=quantity_text):
                for addon in addons:
                    if addon['addon'] == a_name and addon['quantity'] > 0:
                        addon['quantity'] -= 1
                        update_quantity_display(q_text, addon['quantity'])
                        break
                save_addons_to_database(addons)
                create_order_summary_content(window)

            button_increment = Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda a_name=addon_name, q_text=quantity_text: increment_quantity(a_name, q_text),
                relief="flat"
            )
            button_increment.place(
                x=300.0,
                y=y_position,
                width=20,
                height=20
            )

            button_decrement = Button(
                image=button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=lambda a_name=addon_name, q_text=quantity_text: decrement_quantity(a_name, q_text),
                relief="flat"
            )
            button_decrement.place(
                x=330.0,
                y=y_position,
                width=20,
                height=20
            )

            y_position += spacing  # Increment y position for next add-on

    # Display total amount
    canvas.create_text(
        29.0,
        562.0,
        anchor="nw",
        text=f"Total: {'':>65}₱{total:.2f}",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    payment_method = getattr(window, 'payment_method', 'Not Selected')

    canvas.create_text(
        29.000244140625,
        645.0,
        anchor="nw",
        text=f"Payment Method: {payment_method}",
        fill="#000000",
        font=("Abril Fatface", 21 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_2.png")
    )
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_1.png")
    )

    def go_back_to_payment_method():
        from payment_Method import create_payment_method_content  # Move import here to avoid circular import
        print("Back button pressed - Going back to payment method")
        clear_window(window)
        create_payment_method_content(window)

    def go_to_order_number():
        from order_number import create_order_number_content  # Import the function to create order number content
        with open('database.json', 'r+') as f:
            data = json.load(f)
            
            # Decrease stock based on items in the cart
            for item in data['cart']:
                item_name = item['item']
                quantity = item['quantity']
                if item_name in data['items']:
                    data['items'][item_name]['stock'] -= quantity
            
            # Reset the cart
            data['cart'] = []
            
            order_number = data.get('order_number', 0) + 1
            data['order_number'] = order_number
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
        
        clear_window(window)
        create_order_number_content(window, order_number)

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=go_back_to_payment_method,
        relief="flat"
    )
    button_1.place(
        x=19.0,
        y=721.0,
        width=83.83250427246094,
        height=38.94280242919922
    )

    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=go_to_order_number,  # Ensure this command is set correctly
        relief="flat"
    )
    button_2.place(
        x=400.0,
        y=721.0,
        width=83.83250427246094,
        height=38.94280242919922
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_7.png")
    )
    button_7 = Button(
        window,
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_order_summary_content(window, page - 1) if page > 0 else None,
        relief="flat"
    )
    button_7.place(
        x=180.620849609375,
        y=717.3338356018066,
        width=56.0,
        height=53.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_8.png")
    )
    button_8 = Button(
        window,
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: create_order_summary_content(window, page + 1),
        relief="flat"
    )
    button_8.place(
        x=240.620849609375,
        y=717.3338356018066,
        width=56.0,
        height=53.0
    )

    window.button_images = [button_image_1, button_image_2, button_image_4, button_image_5, button_image_9, button_image_10]  # Keep a reference to the images

if __name__ == "__main__":
    window = Tk()
    create_order_summary_content(window)
    window.mainloop()