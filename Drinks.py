
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pilim\Desktop\build\assets\frame3")


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
    x=23.816162109375,
    y=536.4450073242188,
    width=60.16745376586914,
    height=60.167457580566406
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
    x=23.816162109375,
    y=110.0748291015625,
    width=60.16745376586914,
    height=60.167457580566406
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
    x=23.78173828125,
    y=327.84625244140625,
    width=60.16745376586914,
    height=60.167457580566406
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
    x=116.024169921875,
    y=65.73040771484375,
    width=148.88934326171875,
    height=148.88937377929688
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
    x=305.254638671875,
    y=65.730712890625,
    width=148.88934326171875,
    height=148.88937377929688
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
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
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
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
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
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
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
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
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
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

canvas.create_text(
    204.25,
    737.2295532226562,
    anchor="nw",
    text="P 999",
    fill="#FBFBFB",
    font=("Abril Fatface", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
