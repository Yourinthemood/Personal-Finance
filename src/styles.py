#Classes for creating default stuff Goes here

#Imports
import customtkinter as ctk
from tkextrafont import Font
values = {"grey": "#35393C", "linen": "#F2E9DC", "strawberry": "#E34850", "blue": "#727FC8", "green": "#709775"}
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


class Foreground:
    def __init__(self, root):
        self.root = root
        self.foreground = ctk.CTkFrame(
            master=root,
            border_width=10,
            corner_radius=100,
            border_color=from_rgb((125,125,125)),
            fg_color=values["linen"]
        )
    
    def show(self):
        self.foreground.pack(pady=50, padx=50, fill="both", expand=True)


class TitleBoxText:
    def __init__(self, foreground, sizex=2100, sizey=125):
        self.title = ctk.CTkFrame(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=8,
            corner_radius=25,
            fg_color=values["strawberry"],
            border_color=from_rgb((255, 200, 200))
        )
        self.sizex = sizex
        self.sizey = sizey
        
    def show(self, x=1150, y=100):
        self.title.place(x=x, y=y, anchor="center")
        self.title.configure(width=self.sizex, height=self.sizey)
        self.title.propagate(False)


class TextBox:
    def __init__(self, foreground, text, sizex=1000, sizey=100):
        self.text_box = ctk.CTkEntry(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=5,
            corner_radius=10,
            fg_color=values["linen"],
            border_color=from_rgb((0,0,0)),
            placeholder_text=text,
            text_color=from_rgb((0,0,0))
        )
        self.sizex=sizex
        self.sizey=sizey
    
    def show(self, x, y):
        self.text_box.place(x=x, y=y, anchor="center")
        self.text_box.configure(width=self.sizex, height=self.sizey)
        self.text_box.propagate(False)
    
    def get_text(self):
        return self.text_box.get()


class BlueButton:
    def __init__(self, foreground, text, command, sizex=1000, sizey=100):
        self.blue_button = ctk.CTkButton(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=10,
            corner_radius=25,
            border_color="#212121",
            fg_color=values["blue"],
            text=text,
            command=command
        )
        self.sizex = sizex
        self.sizey = sizey
    
    def show(self, x, y):
        self.blue_button.place(x=x, y=y, anchor="center")
        self.blue_button.configure(width=self.sizex, height=self.sizey)
        self.blue_button.propagate(False)


class GreenButton:
    def __init__(self, foreground, text, command, sizex, sizey):
        self.green_button = ctk.CTkButton(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=10,
            corner_radius=25,
            border_color="#212121",
            fg_color=values["green"],
            text=text,
            command=command
        )
        self.sizex = sizex
        self.sizey = sizey

    def show(self, x, y):
        self.green_button.place(x=x, y=y, anchor="center")  
        self.green_button.configure(width=self.sizex, height=self.sizey)
        self.green_button.propagate(False)


class RedX:
    def __init__(self, foreground, root):
        self.foreground = foreground
        self.root = root
    
    def show(self, x=2300, y=150):
        canvas = ctk.CTkCanvas(self.foreground, width=150, height=150, bg=values["linen"], highlightthickness=0)
        
        def on_click(event):
            self.root.destroy()

        canvas.place(x=x, y=y, anchor="center")

        border_width = 50
        inner_width = 30
        
        border_color = from_rgb((255, 200, 200))
        inner_color = values["strawberry"]

        line1_coords = (125, 125, 25, 25) 
        line2_coords = (25, 125, 125, 25) 

        canvas.create_line(*line1_coords, fill=border_color, width=border_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=border_color, width=border_width, capstyle="round")

        canvas.create_line(*line1_coords, fill=inner_color, width=inner_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=inner_color, width=inner_width, capstyle="round")
        
        canvas.bind("<Button-1>", on_click)


class SumbitButton:
    def __init__(self, foreground, command, sizex, sizey, color):
        self.submit = ctk.CTkButton(
            master=foreground,
            border_width=2,
            border_color=from_rgb((0,0,0)),
            text="Submit",
            fg_color=from_rgb(color),
            command=command
        )
        self.sizex=sizex
        self.sizey=sizey
    
    def show(self, x, y):
        self.submit.place(x=x, y=y, anchor="center")  
        self.submit.configure(width=self.sizex, height=self.sizey)
        self.submit.propagate(False)


class OutputBox:
    def __init__(self, titleframe):
        self.text = ctk.CTkLabel(
            master=titleframe,
            text="Personal Finance App",
            font=("Arial", 100),
            text_color="#212121"
        )

    def show(self):
        self.text.pack(pady=10)