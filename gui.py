from tkinter import *
from turtle import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askdirectory
from PIL import ImageGrab
import fractallogic
import random
from colors import Color

def choose():
    t = RawTurtle(screen)
    frac = fractallogic.Fractal()
    choice = fractal_var.get()
    if choice == "Snowflake":
        frac.koch(t, Color.get_color(Color), int(variable_2.get()) / 20, int(variable_1.get())*5, variable_3.get(), direction_var.get())
    if choice == "Tree":
        frac.tree(t, Color.get_color(Color), int(variable_1.get()), int(variable_2.get()), variable_3.get(), direction_var.get())
    if choice == "Polygon":
        frac.polygon(t, Color.get_color(Color), int(variable_1.get()) / 10, int(variable_2.get()) * 2, variable_3.get(), direction_var.get() )

def changecolor():
    frac_color = askcolor()
    Color.set_color(Color, frac_color)

def changespeed(speed):
    Color.set_speed(Color, speed_scale.get())

def saveimage():
    path=askdirectory()
    frac_number = random.randint(1, 1000)
    x0 = canvas.winfo_rootx()
    y0 = canvas.winfo_rooty()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("{}/fractal{}.png".format(path, str(frac_number)))

root = Tk()
root.title("Fancy Fractals")
root.configure(bg="black")
canvas = Canvas(root, width=1000, height=800)
canvas.pack()

#fancy_label = Label(text="Some fancy Options", bg="#000033", fg="white", font=(None, 20))
#fancy_label.pack(padx=50, pady=10, side=LEFT)

fractal_options = ["Tree", "Snowflake", "Polygon"]
fractal_var = StringVar(root)
fractal_var.set(fractal_options[0])
menu_fractals = OptionMenu(root, fractal_var, *fractal_options)
menu_fractals.config(bg="#000033", fg="white", font=(None, 15), width=10)
menu_fractals.pack(padx=50, pady=10, side= LEFT)

colorButton = Button(root, text="Color", padx=50, command=changecolor, bg="#000033", fg="white", font=(None, 15))
colorButton.pack(padx=50, pady=10, side=LEFT)

direction = ["Normal", "Mirror"]
direction_var = StringVar(root)
direction_var.set(direction[0])
menu_direction = OptionMenu(root, direction_var, *direction)
menu_direction.config(bg="#000033", fg="white", font=(None, 15), width=7)
menu_direction.pack(padx=50, pady=10, side=LEFT)

fancy_options_1 = [30, 40, 50, 60, 70]
variable_1 = StringVar(root)
variable_1.set(fancy_options_1[2])
fancy_1 = OptionMenu(root, variable_1, *fancy_options_1)
fancy_1.config(bg="#000033", fg="white", font=(None, 15))
fancy_1.pack(padx=50, pady=10, side= LEFT)

fancy_options_2 = [20, 30, 40, 50, 60]
variable_2 = StringVar(root)
variable_2.set(fancy_options_2[2])
fancy_2 = OptionMenu(root, variable_2, *fancy_options_2)
fancy_2.config(bg="#000033", fg="white", font=(None, 15))
fancy_2.pack(padx=50, pady=10, side= LEFT)

fancy_options_3 = [3, 4, 5, 6, 7]
variable_3 = IntVar(root)
variable_3.set(fancy_options_3[2])
fancy_3 = OptionMenu(root, variable_3, *fancy_options_3)
fancy_3.config(bg="#000033", fg="white", font=(None, 15))
fancy_3.pack(padx=50, pady=10, side= LEFT)

speed_var = IntVar(root)
speed_var.set(5)
speed_scale = Scale(root, from_=1, resolution=1, to=10, variable=speed_var, command=changespeed)
speed_scale.config(bg="#000033", fg="white", font=(None, 15))
speed_scale.pack(padx=50, pady=10, side= LEFT)

photo = PhotoImage(file="icon.png").subsample(4, 4)
imageButton = Button(root, image=photo, command=saveimage, bg="#000033", fg="white", font=(None, 15))
imageButton.pack(padx=0, pady=10, side=LEFT)

myButton = Button(root, text="Draw", padx=50, command=choose, bg="#000033", fg="white", font=(None, 20))
myButton.pack(padx=20, pady=60, side= LEFT)

screen = TurtleScreen(canvas)
screen.bgcolor("black")
#t = RawTurtle(screen)

root.mainloop()