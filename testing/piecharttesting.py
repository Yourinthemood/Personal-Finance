import piecharts
import customtkinter

root = customtkinter.CTk()
root.geometry("400x400")

pie_chart = piecharts.CTkPieChart(root, line_width=50) 
pie_chart.pack(pady=20)

pie_chart.add("A", 10)
pie_chart.add("B", 60, color="cyan", text_color="black")
pie_chart.add("C", 40)

root.mainloop()