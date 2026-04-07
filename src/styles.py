#Classes for creating default stuff Goes here

#Imports
import customtkinter as ctk
values = {"grey": "#35393C", "linen": "#F2E9DC", "strawberry": "#E34850", "blue": "#727FC8", "green": "#709775"}
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

class Foreground:
    def __init__(self, root):
        self.foreground = ctk.CTkFrame(
            master=root,
            border_width=15,
            corner_radius=100,
            border_color=from_rgb((125,125,125)),
            fg_color=values["linen"]
        )
    
    def show(self):
        self.foreground.pack(pady=50, padx=50, fill="both", expand=True)


class TitleBoxText(Foreground):
    def __init__(self):
        self.title = ctk.CTkFrame(
            master=self.foreground,
            width=10,
            height=50,
            border_width=2,
            corner_radius=10,
            fg_color=values["strawberry"],
        )
        
    
    def show(self):
        self.title.pack(pady=25, padx=100, fill="both", expand=False)


class TextBox:
    def __init__(self,text):
        self.text = text
    
    def show(self):
        pass


class BlueButton(Foreground):
    def __init__(self, text):
        self.blue_button = ctk.CTkButton(
            master=self.foreground,
            border_width=2,
            border_color=from_rgb((0,0,0)),
            fg_color=values["blue"],
            text=text,
            #command=login.login()
        )
    
    def show(self):
        self.blue_button.pack(pady=20)


class GreenButton(Foreground):
    def __init__(self, text):
        self.green_button = ctk.CTkButton(
            master=self.foreground,
            border_width=2,
            border_color=from_rgb((0,0,0)),
            fg_color=values["green"],
            text=text,
            #command=signup.signup()
        )

    def show(self):
        self.green_button.place(relx=0.5, rely=0.5, anchor="center") 
        self.green_button.pack(pady=20)    


class RedX:
    def __init__(self):
        pass
    
    def show(self):
        pass


class SumbitButton(Foreground):
    def __init__(self):
        self.submit = ctk.CTkButton(
            master=self.foreground,
            border_width=2,
            border_color=from_rgb((0,0,0)),
            fg_color=values["linen"],
            text="Submit",
            #command=signup.signup()
        )
    
    def show(self):
        self.sumit.place(relx=0.5, rely=0.5, anchor="center") 
        self.submit.pack(pady=20)


class OutputBox:
    def __init__(self,color):
        self.color = color

    def show(self):
        pass