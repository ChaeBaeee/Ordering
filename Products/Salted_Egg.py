
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\build\assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("507x782")
window.configure(bg = "#F2C94C")


canvas = Canvas(
    window,
    bg = "#F2C94C",
    height = 782,
    width = 507,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    558.1047973632812,
    238.7808380126953,
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
    x=344.83306884765625,
    y=712.979736328125,
    width=138.046875,
    height=39.41100311279297
)

canvas.create_rectangle(
    -0.4979572594165802,
    697.3168375430512,
    507.94146728515625,
    697.9182739257812,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    18.142320811748505,
    322.2069874548215,
    490.920166015625,
    322.7502136230469,
    fill="#000000",
    outline="")

canvas.create_text(
    42.4671630859375,
    343.1344299316406,
    anchor="nw",
    text="Salted Egg (4pcs)",
    fill="#000000",
    font=("Abril Fatface", 20 * -1)
)

canvas.create_text(
    42.4671630859375,
    417.8766174316406,
    anchor="nw",
    text="Php 999 ",
    fill="#000000",
    font=("Abril Fatface", 20 * -1)
)

canvas.create_text(
    35.67242431640625,
    492.6188049316406,
    anchor="nw",
    text="Crispy wings coated in a creamy salted egg sauce,\ndelivering a savory, rich flavor with a touch of\nsaltiness.",
    fill="#000000",
    font=("Abril Fatface", 20 * -1)
)

canvas.create_text(
    106.87994384765625,
    723.979736328125,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("Abril Fatface", 18 * -1)
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
    x=137.59344482421875,
    y=725.3387451171875,
    width=27.178970336914062,
    height=27.178970336914062
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
    x=59.45404052734375,
    y=723.6400756835938,
    width=27.178970336914062,
    height=27.178970336914062
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    252.19610595703125,
    192.19202423095703,
    image=image_image_1
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
    x=18.87994384765625,
    y=21.979736328125,
    width=33.0,
    height=29.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=351.87994384765625,
    y=20.979736328125,
    width=126.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
