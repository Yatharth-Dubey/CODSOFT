from tkinter import *
from PIL import Image, ImageTk

# Initialize window
a1 = Tk()

img = Image.open("calculator_background.jpg")
icon = ImageTk.PhotoImage(img)
a1.iconphoto(False, icon)

# Setting window title and size
a1.title("YATHARTH's CALCULATOR")
a1.geometry("350x300")

bg_image = Image.open("calculator_background.jpg")
bg_image = bg_image.resize((350, 300), Image.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(bg_image)

#background image
bg_label = Label(a1, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


t1 = Text(a1)
t1.pack()
t1.place(x=50, y=50, width=260, height=80)
t1.config(bg="yellow", fg="black", bd=5, relief="solid")

# Logic functions
def button_clicked(number):
    current = t1.get("1.0", "end-1c")
    t1.delete("1.0", "end")
    t1.insert("1.0", current + str(number))

def button_clear():
    t1.delete("1.0", "end")

def button_equal():
    try:
        result = str(eval(t1.get("1.0", "end-1c")))
        t1.delete("1.0", "end")
        t1.insert("1.0", result)
    except:
        t1.delete("1.0", "end")
        t1.insert("1.0", "ERROR")

# Buttons for the calculator
# 9
b9 = Button(a1, text="9", bg="tomato", command=lambda: button_clicked(9))
b9.pack()
b9.place(x=190, y=140, width=50, height=30)
# 8
b8 = Button(a1, text="8", bg="tomato", command=lambda: button_clicked(8))
b8.pack()
b8.place(x=120, y=140, width=50, height=30)
# 7
b7 = Button(a1, text="7", bg="tomato", command=lambda: button_clicked(7))
b7.pack()
b7.place(x=50, y=140, width=50, height=30)
# 6
b6 = Button(a1, text="6", bg="tomato", command=lambda: button_clicked(6))
b6.pack()
b6.place(x=190, y=180, width=50, height=30)
# 5
b5 = Button(a1, text="5", bg="tomato", command=lambda: button_clicked(5))
b5.pack()
b5.place(x=120, y=180, width=50, height=30)
# 4
b4 = Button(a1, text="4", bg="tomato", command=lambda: button_clicked(4))
b4.pack()
b4.place(x=50, y=180, width=50, height=30)
# 3
b3 = Button(a1, text="3", bg="tomato", command=lambda: button_clicked(3))
b3.pack()
b3.place(x=190, y=220, width=50, height=30)
# 2
b2 = Button(a1, text="2", bg="tomato", command=lambda: button_clicked(2))
b2.pack()
b2.place(x=120, y=220, width=50, height=30)
# 1
b1 = Button(a1, text="1", bg="tomato", command=lambda: button_clicked(1))
b1.pack()
b1.place(x=50, y=220, width=50, height=30)
# 0
b0 = Button(a1, text="0", bg="tomato", command=lambda: button_clicked(0))
b0.pack()
b0.place(x=50, y=260, width=50, height=30)
# =
b10 = Button(a1, text="=", bg="lightgreen", command=button_equal)
b10.pack()
b10.place(x=230, y=260, width=80, height=30)
# +
b11 = Button(a1, text="+", bg="lightgreen", command=lambda: button_clicked("+"))
b11.pack()
b11.place(x=260, y=180, width=50, height=30)
# -
b12 = Button(a1, text="-", bg="lightgreen", command=lambda: button_clicked("-"))
b12.pack()
b12.place(x=260, y=140, width=50, height=30)
# *
b13 = Button(a1, text="*", bg="lightgreen", command=lambda: button_clicked("*"))
b13.pack()
b13.place(x=260, y=220, width=50, height=30)
# /
b14 = Button(a1, text="/", bg="lightgreen", command=lambda: button_clicked("/"))
b14.pack()
b14.place(x=110, y=260, width=50, height=30)
# C
b15 = Button(a1, text="C", bg="lightgreen", command=button_clear)
b15.pack()
b15.place(x=170, y=260, width=50, height=30)


a1.mainloop()