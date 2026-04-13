#Classes for creating default stuff Goes here

# Imports
import customtkinter as ctk
from tkextrafont import Font
from PIL import Image
import os, random

# Load colors
values = {"grey": "#35393C", "linen": "#F2E9DC", "strawberry": "#E34850", "blue": "#727FC8", "green": "#709775"}
selected_mode = "fullscreen"
BASE_WIDTH = 2560
BASE_HEIGHT = 1440
if selected_mode == "1440p":
    scale_x = 1.0
    scale_y = 1.0
elif selected_mode == "1080p":
    scale_x = 1920 / BASE_WIDTH
    scale_y = 1080 / BASE_HEIGHT
elif selected_mode == "fullscreen":
    scale_x = 1.0
    scale_y = 1.0

def update_scales(root=None):
    global scale_x, scale_y
    if selected_mode == "1440p":
        scale_x = 1.0
        scale_y = 1.0
    elif selected_mode == "1080p":
        scale_x = 1920 / BASE_WIDTH
        scale_y = 1080 / BASE_HEIGHT
    elif selected_mode == "fullscreen":
        if root is not None:
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            scale_x = width / BASE_WIDTH
            scale_y = height / BASE_HEIGHT
        else:
            scale_x = 1.0
            scale_y = 1.0
    else:
        scale_x = 1.0
        scale_y = 1.0

def apply_screen_resolution(root):
    if selected_mode == "1440p":
        root.geometry("2560x1440+0+0")
        root.attributes("-fullscreen", False)
    elif selected_mode == "1080p":
        root.geometry("1920x1080+0+0")
        root.attributes("-fullscreen", False)
    elif selected_mode == "fullscreen":
        root.attributes("-fullscreen", True)
    else:
        root.geometry("2560x1440+0+0")
        root.attributes("-fullscreen", False)
    update_scales(root)


def scale_value(value):
    return max(int(value * min(scale_x, scale_y)), 1)


def scale_position(value):
    #Scale position coordinates based on current resolution.
    return int(value * min(scale_x, scale_y))


def scale_size(value):
    #Scale widget sizes more aggressively for 1080p.
    return max(int(value * min(scale_x, scale_y)), 1)


def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

# Load fonts
_font_loaded_roots = set()
def load_font(root):
    root_id = id(root)
    if root_id not in _font_loaded_roots:
        try:
            Font(file="docs/images/Dongle-Bold.ttf", family="Dongle", root=root)
            _font_loaded_roots.add(root_id)
        except:
            try:
                Font(file="Personal-Finance/docs/images/Dongle-Bold.ttf", family="Dongle", root=root)
                _font_loaded_roots.add(root_id)
            except:
                pass  # Font file not found, use default

class Foreground:
    def __init__(self, root):
        self.root = root
        load_font(root)
        self.foreground = ctk.CTkFrame(
            master=root,
            border_width=scale_value(10),
            corner_radius=scale_value(100),
            border_color=from_rgb((125,125,125)),
            fg_color=values["linen"]
        )
    
    def show(self):
        self.foreground.pack(pady=scale_position(50), padx=scale_position(50), fill="both", expand=True)


class TitleBoxText:
    def __init__(self, foreground, sizex=2000, sizey=150):
        # Use adaptive sizing: smaller for 1080p
        scaled_sizex = scale_size(sizex)
        scaled_sizey = scale_size(sizey)
        self.title = ctk.CTkFrame(
            master=foreground,
            width=scaled_sizex,
            height=scaled_sizey,
            border_width=scale_value(8),
            corner_radius=scale_value(25),
            fg_color=values["strawberry"],
            border_color=from_rgb((255,200,200)),
        )
        self.sizex = scaled_sizex
        self.sizey = scaled_sizey
        
    def show(self, x=1100, y=150):
        self.title.place(x=scale_position(x), y=scale_position(y), anchor="center")
        self.title.configure(width=self.sizex, height=self.sizey)
        self.title.propagate(False)


class TextBox:
    def __init__(self, foreground, text, sizex=1000, sizey=100):
        scaled_sizex = scale_size(sizex)
        scaled_sizey = scale_size(sizey)
        self.text_box = ctk.CTkEntry(
            master=foreground,
            width=scaled_sizex,
            height=scaled_sizey,
            border_width=scale_value(5),
            corner_radius=scale_value(10),
            fg_color=values["linen"],
            border_color=from_rgb((0,0,0)),
            placeholder_text=text,
            text_color=from_rgb((0,0,0)),
            font=("Arial", scale_value(64))
        )
        self.sizex=scaled_sizex
        self.sizey=scaled_sizey
    
    def show(self, x, y):
        self.text_box.place(x=scale_position(x), y=scale_position(y), anchor="center")
        self.text_box.configure(width=self.sizex, height=self.sizey)
        self.text_box.propagate(False)
    
    def get_text(self):
        return self.text_box.get()


class BlueButton:
    def __init__(self, foreground, text, command, sizex=1000, sizey=100):
        scaled_sizex = scale_size(sizex)
        scaled_sizey = scale_size(sizey)
        self.blue_button = ctk.CTkButton(
            master=foreground,
            width=scaled_sizex,
            height=scaled_sizey,
            border_width=scale_value(10),
            corner_radius=scale_value(25),
            border_color="#212121",
            fg_color=values["blue"],
            text=text,
            command=command,
            font=("Arial", scale_value(32))
        )
        self.sizex = scaled_sizex
        self.sizey = scaled_sizey
    
    def show(self, x, y):
        self.blue_button.place(x=scale_position(x), y=scale_position(y), anchor="center")
        self.blue_button.configure(width=self.sizex, height=self.sizey)
        self.blue_button.propagate(False)


class GreenButton:
    def __init__(self, foreground, text, command, sizex, sizey):
        scaled_sizex = scale_size(sizex)
        scaled_sizey = scale_size(sizey)
        self.green_button = ctk.CTkButton(
            master=foreground,
            width=scaled_sizex,
            height=scaled_sizey,
            border_width=scale_value(10),
            corner_radius=scale_value(25),
            border_color="#212121",
            fg_color=values["green"],
            text=text,
            command=command,
            font=("Arial", scale_value(32))
        )
        self.sizex = scaled_sizex
        self.sizey = scaled_sizey

    def show(self, x, y):
        self.green_button.place(x=scale_position(x), y=scale_position(y), anchor="center")  
        self.green_button.configure(width=self.sizex, height=self.sizey)
        self.green_button.propagate(False)


class RedX:
    def __init__(self, foreground, root):
        self.foreground = foreground
        self.root = root
    
    def show(self, x=2250, y=150):
        canvas = ctk.CTkCanvas(self.foreground, width=scale_value(150), height=scale_value(150), bg=values["linen"], highlightthickness=0)
        
        def on_click(event):
            self.root.destroy()
            os.system("cls")

        canvas.place(x=scale_position(x), y=scale_position(y), anchor="center")

        border_width = scale_value(50)
        inner_width = scale_value(30)
        
        border_color = from_rgb((255, 200, 200))
        inner_color = values["strawberry"]

        line1_coords = (scale_value(125), scale_value(125), scale_value(25), scale_value(25)) 
        line2_coords = (scale_value(25), scale_value(125), scale_value(125), scale_value(25)) 

        canvas.create_line(*line1_coords, fill=border_color, width=border_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=border_color, width=border_width, capstyle="round")

        canvas.create_line(*line1_coords, fill=inner_color, width=inner_width, capstyle="round")
        canvas.create_line(*line2_coords, fill=inner_color, width=inner_width, capstyle="round")
        
        canvas.bind("<Button-1>", on_click)


class SumbitButton:
    def __init__(self, foreground, command, sizex=200, sizey=100):
        scaled_sizex = scale_size(sizex)
        scaled_sizey = scale_size(sizey)
        self.submit = ctk.CTkButton(
            master=foreground,
            border_width=scale_value(5),
            corner_radius=scale_value(15),
            border_color=from_rgb((0,0,0)),
            text="Submit",
            fg_color=values["green"],
            command=command,
            font=("Arial", scale_value(32))
        )
        self.sizex=scaled_sizex
        self.sizey=scaled_sizey
    
    def show(self, x, y):
        self.submit.place(x=scale_position(x), y=scale_position(y), anchor="center")  
        self.submit.configure(width=self.sizex, height=self.sizey)
        self.submit.propagate(False)


class OutputBox:
    def __init__(self, titleframe, text, size=100):
        self.text = ctk.CTkLabel(
            master=titleframe,
            text=text,
            font=("Arial", scale_value(size)),
            text_color=values["linen"]
        )

    def show(self):
        self.text.pack(pady=scale_position(10))


class OutputFrame:
    def __init__(self, foreground, sizex, sizey):
        scaled_sizex = scale_size(sizex)
        scaled_sizey = scale_size(sizey)
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=scale_value(5),
            corner_radius=scale_value(15),
            border_color=from_rgb((200,255,200)),
            fg_color=values["green"]
        )
        self.sizex=scaled_sizex
        self.sizey=scaled_sizey

    def show(self, x, y):
        self.frame.place(x=scale_position(x), y=scale_position(y), anchor="center")  
        self.frame.configure(width=self.sizex, height=self.sizey)
        self.frame.propagate(False)


class Popup:
    def __init__(self, foreground, width=800, height=75):
        scaled_width = scale_size(width)
        scaled_height = scale_size(height)
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=scale_value(5),
            corner_radius=scale_value(15),
            width=scale_value(10),
            height=scaled_height,
            border_color=from_rgb((255,200,200)),
            fg_color=values["strawberry"]
        )
        self.sizex = scaled_width
        self.sizey = scaled_height

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
            self.frame.place(x=scale_position(1280), y=scale_position(current_y), anchor="center")
            self.frame.configure(width=scale_value(10), height=self.sizey)
            self.frame.propagate(False)

        elif self.step < 60:
            t = (self.step - 30) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * eased
            self.frame.configure(width=int(current_width))

        elif self.step < 160:
            pass

        elif self.step < 190:
            t = (self.step - 160) / 30
            eased = 1 - (1 - t) ** 3
            current_width = self.sizex * (1 - eased)
            self.frame.configure(width=int(max(current_width, scale_value(10))))

        elif self.step < 220:
            t = (self.step - 190) / 30
            eased = 1 - (1 - t) ** 3
            current_y = self.end_y + (self.start_y - self.end_y) * eased
            self.frame.place(x=scale_position(1280), y=scale_position(current_y), anchor="center")

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
        x = scale_position(random.randint(500, 2060))
        y = scale_position(random.randint(500, 940))
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
        scaled_width = scale_size(width)
        scaled_height = scale_size(height)
        self.frame = ctk.CTkFrame(
            master=foreground,
            border_width=scale_value(5),
            corner_radius=scale_value(15),
            width=scale_value(10),
            height=scaled_height,
            border_color=from_rgb((200,200,255)),
            fg_color=values["blue"]
        )
        self.sizex = scaled_width
        self.sizey = scaled_height

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
            self.frame.place(x=scale_position(1280), y=scale_position(current_y), anchor="center")
            self.frame.configure(width=scale_value(10), height=self.sizey)
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
    def __init__(self, foreground, command, options=[], height=28):
        self.segmented_button = ctk.CTkSegmentedButton(foreground, values=options, command=command, height=scale_value(height))
        self.segmented_button.set(options[0] if options else "Kass' theme")
    
    def get_option(self):
        return self.segmented_button.get()
    
    def show(self, pady=200):
        self.segmented_button.pack(pady=pady)