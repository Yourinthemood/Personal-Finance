import piecharts
import customtkinter

root = customtkinter.CTk()
root.geometry("1000x1000")
customtkinter.set_appearance_mode("dark")

values = {"A": 10, "B": 10, "C": 10}

frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

pie_chart = piecharts.CTkPieChart(frame, line_width=50)
pie_chart.pack(pady=20)

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def update_chart():
    global pie_chart

    pie_chart.destroy()

    pie_chart = piecharts.CTkPieChart(frame, line_width=50)
    pie_chart.pack(pady=20)

    pie_chart.add("A", values["A"], color=from_rgb((230, 150, 218)), text_color="black")
    pie_chart.add("B", values["B"], color=from_rgb((200, 100, 10)), text_color="black")
    pie_chart.add("C", values["C"], color="#709775", text_color="black")

update_chart()

def increase_A():
    values["A"] += 5
    update_chart()

btn = customtkinter.CTkButton(
    master=frame,
    text="Increase A",
    command=increase_A
)
btn.pack(pady=20)

root.mainloop()