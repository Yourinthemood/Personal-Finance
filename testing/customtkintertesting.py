import piecharts
import customtkinter

app = customtkinter.CTk

root = customtkinter.CTk()
root.geometry("400x400")
customtkinter.set_appearance_mode("dark")

frame = customtkinter.CTkFrame(
    master=root,
    width=300,
    height=300,
    border_width=2,
    corner_radius=10,
    fg_color="dark gray"
)
frame.pack(pady=20, padx=20, fill="both", expand=True)

pie_chart = piecharts.CTkPieChart(frame, line_width=50) 
pie_chart.pack(pady=20)

pie_chart.add("A", 10)
pie_chart.add("B", 10, color="cyan", text_color="black")
pie_chart.add("C", 10)

btn = customtkinter.CTkButton(
    master=frame,
    text="Click!",
    command=lambda: print("Hi"),
    width=100,
    height=50,
    border_width=2,
    corner_radius=8,
    hover=True
)
btn.pack(pady=20)



entry = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Type something...",
    width=200,
    height=30,
    border_width=2,
    corner_radius=10
)
entry.pack(pady=10)

# To get the text from the entry:
def get_text():
    text = entry.get()
    print(f"Entry contains: {text}")

get_button = customtkinter.CTkButton(master=app, text="Get Text", command=get_text)
get_button.pack(pady=5)



root.mainloop()
