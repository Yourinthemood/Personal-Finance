import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Fullscreen App")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))

        label = customtkinter.CTkLabel(master=self, text="Welcome to Fullscreen App! Press Esc to exit.")
        label.pack(fill="both", expand=True)
    
    def button(self, name):
        self.btn = customtkinter.CTkButton(
            master=self,
            text=name,
            command=lambda: print("Button clicked"),
            width=100,
            height=50,
            border_width=20,
            corner_radius=2,
            hover=True
        )
        self.btn.pack(pady=20)
        
app = App()
app.button(name="Test")
app.mainloop()