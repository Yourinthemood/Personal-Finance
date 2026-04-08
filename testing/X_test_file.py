import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("X Shape with Border")
app.geometry("1300x1300")

canvas = ctk.CTkCanvas(app, width=1400, height=1400, bg="darkgrey", highlightthickness=0)
canvas.pack(pady=40)

border_width = 150
inner_width = 100
border_color = "black"
inner_color = "red"

line1_coords = (400, 400, 200, 200) 
line2_coords = (200, 400, 400, 200) 

canvas.create_line(*line1_coords, fill=border_color, width=border_width, capstyle="round")
canvas.create_line(*line2_coords, fill=border_color, width=border_width, capstyle="round")

canvas.create_line(*line1_coords, fill=inner_color, width=inner_width, capstyle="round")
canvas.create_line(*line2_coords, fill=inner_color, width=inner_width, capstyle="round")

app.mainloop()