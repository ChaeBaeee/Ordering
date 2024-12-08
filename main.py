from tkinter import Tk
from bestseller import create_bestseller_content

def main():
    window = Tk()
    create_bestseller_content(window)
    window.mainloop()

if __name__ == "__main__":
    main()