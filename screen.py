import tkinter as tk
from tkinter import Canvas
from picture_base import map_synthesis
import config

mark = 0
canvas = None

def click(e):
    global canvas, mark
    mx = e.x
    my = e.y
    if mark == 0: mark = 1 ,screen_main()

def screen_main():
    global canvas, mark
    if mark == 0:
        canvas.create_text(config.width / 2, config.height / 2, text="START", fill="gold", font=config.F_L)
    elif mark == 1:
        canvas.delete("all")
        map_area(canvas)
        info_area(canvas)

def map_area(canvas):
    canvas.delete("main_area")
    canvas.create_rectangle(0, 0, config.width - 304, config.height, fill="white", width=2, tags="main_area")
    image = map_synthesis(config.base_ground)
    canvas.create_image(0, 0, image=image, anchor=tk.NW)

def info_area(canvas):
    canvas.delete("info_area")
    info_text = "Player Status:\nHealth: 100\nMana: 50\nLevel: 5"
    canvas.create_text(config.width - 150, 50, anchor="nw", text=info_text, fill="white", font=("Arial", 12), tags="info_area")

def start():
    global canvas
    root = tk.Tk()
    root.title("RPG GAME")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=config.width, height=config.height, bg="black")
    canvas.pack()
    root.bind("<Button>", click)
    root.after(100, screen_main)
    root.mainloop()
    
start()
