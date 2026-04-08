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
    def __init__(self, foreground):
        self.title = ctk.CTkFrame(
            master=foreground,
            border_width=8,
            corner_radius=25,
            fg_color=values["strawberry"],
            border_color=from_rgb((255, 200, 200))
        )
        
    def show(self):
        self.title.pack(pady=75, padx=100, fill="x", expand=False)

class TextBox:
    def __init__(self, text):
        self.text = text
    
    def show(self):
        pass


class BlueButton:
    def __init__(self, foreground, text, command):
        self.blue_button = ctk.CTkButton(
            master=foreground,
            width=1000,
            height=100,
            border_width=10,
            corner_radius=25,
            border_color="#212121",
            fg_color=values["blue"],
            text=text,
            command=command
        )
    
    def show(self):
        self.blue_button.pack(pady=25)


class GreenButton:
    def __init__(self, foreground, text, command):
        self.green_button = ctk.CTkButton(
            master=foreground,
            width=1000,
            height=100,
            border_width=10,
            corner_radius=25,
            border_color="#212121",
            fg_color=values["green"],
            text=text,
            command=command
        )

    def show(self):
        self.green_button.pack(pady=25)    


class RedX:
    def __init__(self, foreground, command):
        self.exit_button = ctk.CTkButton(
            master=foreground,
            border_width=2,
            border_color=from_rgb((25,0,0)),
            fg_color=values["strawberry"],
            command=command
        )
        self.foreground = foreground
    
    
    def show(self):
        canvas = ctk.CTkCanvas(self.foreground, width=150, height=150, bg=values["linen"], highlightthickness=0)
        
        def on_click(event):
            print("X clicked!")

        def on_enter(event):
            event.widget.configure(bg="#555555")

        def on_leave(event):
            event.widget.configure(bg="darkgrey")

        canvas.pack()

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
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)

        self.exit_button.pack(pady=10)


class SumbitButton:
    def __init__(self, foreground, command):
        self.submit = ctk.CTkButton(
            master=foreground,
            border_width=2,
            border_color=from_rgb((0,0,0)),
            fg_color=values["linen"],
            text="Submit",
            command=command
        )
    
    def show(self):
        self.submit.pack(pady=20)


class OutputBox:
    def __init__(self, titleframe):
        text = Font(file="docs/images/Dongle-Bold.ttf", family="Dongle")
        self.text = ctk.CTkLabel(
            master=titleframe,
            text="Personal Finance App",
            font=("Dongle", 100),
            text_color="#212121"
        )

    def show(self):
        self.text.pack(pady=10)