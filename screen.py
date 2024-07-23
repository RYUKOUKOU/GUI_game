import tkinter as tk
from tkinter import Canvas
from picture_base import map_synthesis
import config
import time

def click(e):
    pass

def main_area_base(canvas):
    global image
    canvas.delete("main_area")
    canvas.create_rectangle(0, 0, config.width - 304, config.height, fill="white", width=2, tags="main_area")
    image = map_synthesis(config.base_ground)
    canvas.create_image(0, 0, image=image, anchor=tk.NW)


def info_area(canvas):
    canvas.delete("info_area")
    info_text = "Player Status:\nHealth: 100\nMana: 50\nLevel: 5"
    canvas.create_text(config.width - 150, 50, anchor="nw", text=info_text, fill="white", font=("Arial", 12), tags="info_area")

def start():
    root = tk.Tk()
    root.title("RPG GAME")
    root.resizable(False, False)
    root.bind("<Button>", click)
    
    canvas = tk.Canvas(root, width=config.width, height=config.height, bg="black")
    canvas.pack()
    main_area_base(canvas)
    root.mainloop()


#start()
