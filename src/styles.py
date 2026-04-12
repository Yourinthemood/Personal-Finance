#Classes for creating default stuff Goes here

# Imports
import customtkinter as ctk
from tkextrafont import Font
from PIL import Image
import os, random

# Load colors
values = {"grey": "#35393C", "linen": "#F2E9DC", "strawberry": "#E34850", "blue": "#727FC8", "green": "#709775"}
selected_mode = "fullscreen"
if selected_mode == "1440p":
    scale_x = 1.0
    scale_y = 1.0
elif selected_mode == "1080p":
    scale_x = 1920 / 2560  # 0.75
    scale_y = 1080 / 1440  # 0.75
elif selected_mode == "fullscreen":
    scale_x = 1.0
    scale_y = 1.0

def update_scales():
    global scale_x, scale_y
    if selected_mode == "1440p":
        scale_x = 1.0
        scale_y = 1.0
    elif selected_mode == "1080p":
        scale_x = 1920 / 2560
        scale_y = 1080 / 1440
    elif selected_mode == "fullscreen":
        scale_x = 1.0
        scale_y = 1.0

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

# Load fonts
_font_loaded_roots = set()
def load_font(root):
    root_id = id(root)
    if root_id not in _font_loaded_roots:
        Font(file="docs/images/Dongle-Bold.ttf", family="Dongle", root=root)
        _font_loaded_roots.add(root_id)

class Foreground:
    def __init__(self, root):
        self.root = root
        load_font(root)
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
    def __init__(self, foreground, sizex=2000, sizey=150):
        self.title = ctk.CTkFrame(
            master=foreground,
            width=sizex,
            height=sizey,
            border_width=8,
            corner_radius=25,
            fg_color=values["strawberry"],
            border_color=from_rgb((255,200,200)),
        )
        self.sizex = sizex
        self.sizey = sizey
        
    def show(self, x=1100, y=150):
        self.title.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")
        self.title.configure(width=int(self.sizex * scale_x), height=int(self.sizey * scale_y))
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
            text_color=from_rgb((0,0,0)),
            font=("Dongle", 64)
        )
        self.sizex=sizex
        self.sizey=sizey
    
    def show(self, x, y):
        self.text_box.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")
        self.text_box.configure(width=int(self.sizex * scale_x), height=int(self.sizey * scale_y))
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
            command=command,
            font=("Dongle", 32)
        )
        self.sizex = sizex
        self.sizey = sizey
    
    def show(self, x, y):
        self.blue_button.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")
        self.blue_button.configure(width=int(self.sizex * scale_x), height=int(self.sizey * scale_y))
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
            command=command,
            font=("Dongle", 32)
        )
        self.sizex = sizex
        self.sizey = sizey

    def show(self, x, y):
        self.green_button.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")  
        self.green_button.configure(width=int(self.sizex * scale_x), height=int(self.sizey * scale_y))
        self.green_button.propagate(False)


class RedX:
    def __init__(self, foreground, root):
        self.foreground = foreground
        self.root = root
    
    def show(self, x=2250, y=150):
        canvas = ctk.CTkCanvas(self.foreground, width=int(150 * scale_x), height=int(150 * scale_y), bg=values["linen"], highlightthickness=0)
        
        def on_click(event):
            self.root.destroy()
            os.system("cls")

        canvas.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")

        border_width = int(50 * scale_x)
        inner_width = int(30 * scale_x)
        
        border_color = from_rgb((255, 200, 200))
        inner_color = values["strawberry"]

        line1_coords = (int(125 * scale_x), int(125 * scale_y), int(25 * scale_x), int(25 * scale_y)) 
        line2_coords = (int(25 * scale_x), int(125 * scale_y), int(125 * scale_x), int(25 * scale_y)) 

        canvas.create_line(*line1_coords, fill=border_color, width=border_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=border_color, width=border_width, capstyle="round")

        canvas.create_line(*line1_coords, fill=inner_color, width=inner_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=inner_color, width=inner_width, capstyle="round")
        
        canvas.bind("<Button-1>", on_click)


class SumbitButton:
    def __init__(self, foreground, command, sizex=200, sizey=100):
        self.submit = ctk.CTkButton(
            master=foreground,
            border_width=5,
            corner_radius=15,
            border_color=from_rgb((0,0,0)),
            text="Submit",
            fg_color=values["green"],
            command=command,
            font=("Dongle", 32)
        )
        self.sizex=sizex
        self.sizey=sizey
    
    def show(self, x, y):
        self.submit.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")  
        self.submit.configure(width=int(self.sizex * scale_x), height=int(self.sizey * scale_y))
        self.submit.propagate(False)


class OutputBox:
    def __init__(self, titleframe, text, size=100):
        self.text = ctk.CTkLabel(
            master=titleframe,
            text=text,
            font=("Dongle", size),
            text_color=values["linen"]
        )

    def show(self):
        self.text.pack(pady=10)


class OutputFrame:
    def __init__(self, foreground, sizex, sizey):
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=5,
            corner_radius=15,
            border_color=from_rgb((200,255,200)),
            fg_color=values["green"]
        )
        self.sizex=sizex
        self.sizey=sizey

    def show(self, x, y):
        self.frame.place(x=int(x * scale_x), y=int(y * scale_y), anchor="center")  
        self.frame.configure(width=int(self.sizex * scale_x), height=int(self.sizey * scale_y))
        self.frame.propagate(False)


class Popup:
    def __init__(self, foreground, width=800, height=75):
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=5,
            corner_radius=15,
            width=10,
            height=height,
            border_color=from_rgb((255,200,200)),
            fg_color=values["strawberry"]
        )
        self.sizex = width
        self.sizey = height

    def show(self):
        self.start_y = 1500
        self.end_y = 1200
        self.step = 0
        self._animate()

    def _animate(self):
        if self.step < 30:
            t = self.step / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.start_y + (self.end_y - self.start_y) * eased
            self.frame.place(x=int(1280 * scale_x), y=int(current_y * scale_y), anchor="center")
            self.frame.configure(width=int(10 * scale_x), height=int(self.sizey * scale_y))
            self.frame.propagate(False)

        elif self.step < 60:
            t = (self.step - 30) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * eased
            self.frame.configure(width=int(current_width * scale_x))

        elif self.step < 160:
            pass

        elif self.step < 190:
            t = (self.step - 160) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * (1 - eased)
            self.frame.configure(width=int(max(current_width, 10) * scale_x))

        elif self.step < 220:
            t = (self.step - 190) / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.end_y + (self.start_y - self.end_y) * eased
            self.frame.place(x=int(1280 * scale_x), y=int(current_y * scale_y), anchor="center")

        else:
            self.frame.place_forget()
            return

        self.step += 1
        self.frame.after(16, self._animate)


class Ads:
    def __init__(self):
        def keep_on_top(root):
            root.lift()
            root.attributes("-topmost", True)
            root.after(50, keep_on_top, root)
        root = ctk.CTkToplevel()
        x = int(random.randint(500, 2060) * scale_x)
        y = int(random.randint(500, 940) * scale_y)
        root.geometry(f"500x500+{x}+{y}")
        root.resizable(False, False)

        root.attributes("-topmost", True)
        root.lift()
        root.focus_force()
        root.overrideredirect(True)

        pil_image = Image.open("assets/1.png")
        ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500, 500))

        image_label = ctk.CTkLabel(root, image=ctk_image, text="")
        image_label.pack(expand=True, fill="both")
        image_label.bind("<Button-1>", lambda e: root.destroy())

        keep_on_top(root)


class Warning:
    def __init__(self, foreground, width=800, height=75):
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=5,
            corner_radius=15,
            width=10,
            height=height,
            border_color=from_rgb((200,200,255)),
            fg_color=values["blue"]
        )
        self.sizex = width
        self.sizey = height

    def show(self):
        self.start_y = 1500
        self.end_y = 1200
        self.step = 0
        self._animate()

    def _animate(self):
        if self.step < 30:
            t = self.step / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.start_y + (self.end_y - self.start_y) * eased
            self.frame.place(x=int(1280 * scale_x), y=int(current_y * scale_y), anchor="center")
            self.frame.configure(width=int(10 * scale_x), height=int(self.sizey * scale_y))
            self.frame.propagate(False)

        elif self.step < 60:
            t = (self.step - 30) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * eased
            self.frame.configure(width=int(current_width * scale_x))

        elif self.step < 160:
            pass

        elif self.step < 190:
            t = (self.step - 160) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * (1 - eased)
            self.frame.configure(width=int(max(current_width, 10) * scale_x))

        elif self.step < 220:
            t = (self.step - 190) / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.end_y + (self.start_y - self.end_y) * eased
            self.frame.place(x=int(1280 * scale_x), y=int(current_y * scale_y), anchor="center")

        else:
            self.frame.place_forget()
            return

        self.step += 1
        self.frame.after(16, self._animate)


class SegmentedButton:
    def __init__(self, foreground, command, options=[]):
        self.segmented_button = ctk.CTkSegmentedButton(foreground, values=options, command=command)
        self.segmented_button.set(options[0] if options else "Kass' theme")
    
    def get_option(self):
        return self.segmented_button.get()
    
    def show(self):
        self.segmented_button.pack(pady=200)