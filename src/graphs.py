import customtkinter as ctk
import styles
import csv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
 
def line_graph(username):
    root = ctk.CTk()
    root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")
 
    foreground = styles.Foreground(root)
    foreground.show()
 
    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()
 
    title = styles.OutputBox(titleframe.title, "Line Graph")
    title.show()
 
    x = styles.RedX(foreground.foreground, root)
    x.show()
 
    # read incomes.csv and save rows that match the username
    income_dates = []
    income_amounts = []
    try:
        with open("files/incomes.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    income_dates.append(row["date"])
                    income_amounts.append(float(row["amount"]))
    except:
        with open("Personal-Finance/files/incomes.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    income_dates.append(row["date"])
                    income_amounts.append(float(row["amount"]))
 
    # read expenses.csv and save rows that match the username
    expense_dates = []
    expense_amounts = []
    try:
        with open("files/expenses.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    expense_dates.append(row["date"])
                    expense_amounts.append(float(row["amount"]))
    except:
        with open("Personal-Finance/files/expenses.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    expense_dates.append(row["date"])
                    expense_amounts.append(float(row["amount"]))
 
    # make the chart
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#1e1e2e")
    ax.set_facecolor("#1e1e2e")
 
    ax.plot(income_dates, income_amounts, marker="o", color="#4ade80", label="Income")
    ax.plot(expense_dates, expense_amounts, marker="o", color="#f87171", label="Expenses")
 
    ax.set_title("Income vs Expenses", color="white")
    ax.tick_params(colors="white", labelrotation=30)
    ax.legend(facecolor="#2a2a3e", labelcolor="white")
    fig.tight_layout()
 
    # put the chart in the window
    canvas = FigureCanvasTkAgg(fig, master=foreground.foreground)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5, rely=0.55, anchor="center")
 
    root.mainloop()
 
 
def pie_chart(username):
    root = ctk.CTk()
    root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")
 
    foreground = styles.Foreground(root)
    foreground.show()
 
    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()
 
    title = styles.OutputBox(titleframe.title, "Pie Charts")
    title.show()
 
    x = styles.RedX(foreground.foreground, root)
    x.show()
 
    # read incomes.csv and add up amounts per category
    income_categories = {}
    try:
        with open("files/incomes.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    cat = row["category"]
                    if cat in income_categories:
                        income_categories[cat] += float(row["amount"])
                    else:
                        income_categories[cat] = float(row["amount"])
    except:
        with open("Personal-Finance/files/incomes.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    cat = row["category"]
                    if cat in income_categories:
                        income_categories[cat] += float(row["amount"])
                    else:
                        income_categories[cat] = float(row["amount"])
 
    # read expenses.csv and add up amounts per category
    expense_categories = {}
    try:
        with open("files/expenses.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    cat = row["category"]
                    if cat in expense_categories:
                        expense_categories[cat] += float(row["amount"])
                    else:
                        expense_categories[cat] = float(row["amount"])
    except:
        with open("Personal-Finance/files/expenses.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    cat = row["category"]
                    if cat in expense_categories:
                        expense_categories[cat] += float(row["amount"])
                    else:
                        expense_categories[cat] = float(row["amount"])
 
    # make two pie charts side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor("#1e1e2e")
 
    ax1.set_facecolor("#1e1e2e")
    ax1.pie(income_categories.values(), labels=income_categories.keys(), autopct="%1.1f%%")
    ax1.set_title("Income by Category", color="white")
 
    ax2.set_facecolor("#1e1e2e")
    ax2.pie(expense_categories.values(), labels=expense_categories.keys(), autopct="%1.1f%%")
    ax2.set_title("Expenses by Category", color="white")
 
    fig.tight_layout()
 
    # put the chart in the window
    canvas = FigureCanvasTkAgg(fig, master=foreground.foreground)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5, rely=0.55, anchor="center")
 
    root.mainloop()