
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\Ordering\assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("507x782")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 782,
    width = 507,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    117.209228515625,
    66.24874114990234,
    anchor="nw",
    text="How would you like to pay?",
    fill="#000000",
    font=("Abril Fatface", 21 * -1)
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
    x=39.06982421875,
    y=720.2427101135254,
    width=83.83250427246094,
    height=38.94280242919922
)

canvas.create_rectangle(
    -0.4979572594165802,
    697.3169939456391,
    507.94146728515625,
    697.9184303283691,
    fill="#000000",
    outline="")

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
    x=96.491455078125,
    y=192.33383560180664,
    width=312.55816650390625,
    height=110.4145736694336
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
    x=97.157958984375,
    y=336.2359046936035,
    width=312.55816650390625,
    height=110.4145736694336
)

canvas.create_rectangle(
    363.518798828125,
    708.3519630432129,
    494.3175964355469,
    772.9020195007324,
    fill="#1A4524",
    outline="")

canvas.create_text(
    378.806884765625,
    716.8453712463379,
    anchor="nw",
    text="Order Total",
    fill="#FBFBFB",
    font=("Abril Fatface", 18 * -1)
)

canvas.create_text(
    378.806884765625,
    737.2295875549316,
    anchor="nw",
    text="P 999",
    fill="#FBFBFB",
    font=("Abril Fatface", 18 * -1)
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
    x=97.157958984375,
    y=480.2359046936035,
    width=312.55816650390625,
    height=110.4145736694336
)
window.resizable(False, False)
window.mainloop()
