#CP2 Group Project 3
import styles, income_expenses, budgeting_tools
import customtkinter as ctk

def main_menu(mode):
    #Once the User has Logged in or Created a Account:
    #(While Logged in):
    root = ctk.CTk()
    if mode == "1440p":
      root.geometry("2560x1440+0+0")
    elif mode == "1080p":
      root.geometry("1920x1080+0+0")
    elif mode == "fullscreen":
      root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")

    #Welcome User to main program and DISPLAY buttons for the following:
        #Budgeting tools and viewing money
        #Display Pie Chart
        #New Income Entry
        #New Expense Entry
        #Convert to Different Currency
        #Display Line Graph
        #Quit Program 

    #Match the user's click with the following:
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Personal Finance App")
    title.show()

    #if clicked Display Pie Chart:
        #trigger Pie Chart Function
    pie_chart = styles.BlueButton(foreground.foreground,"Pie Chart",command=lambda: print("Pie Chart Clicked"),sizex=300,sizey=100)
    pie_chart.show(400,400)

    #if clicked Display Line Graph
        #trigger Line Graph Function
    line_graph = styles.BlueButton(foreground.foreground,"Line Graph",command=lambda: print("Line Graph Clicked"),sizex=300,sizey=100)
    line_graph.show(400,600)

    #if clicked Budgeting Tools:
        #trigger Budgeting Tools Menu Function
    budget = styles.BlueButton(foreground.foreground,"Budgeting tools",command=lambda: budgeting_tools.budgeting_tools(mode),sizex=350,sizey=100)
    budget.show(800,400)

    #if clicked Convert to Different Currency:
        #trigger Convert to Dif. Currency Function
    currency_conv = styles.BlueButton(foreground.foreground,"Currency Conversion",command=lambda: print("Currency Conversion Clicked"),sizex=300,sizey=100)
    currency_conv.show(800,600)

    #if clicked New Income:
        #trigger New Income Function
    income = styles.BlueButton(foreground.foreground,"New Income",command=lambda: income_expenses.income(mode),sizex=300,sizey=100)
    income.show(1200,400)

    #if cicked New Expense:
        #trigger New Expense Function
    expense = styles.BlueButton(foreground.foreground,"New Expense",command=lambda: income_expenses.expenses(mode),sizex=300,sizey=100)
    expense.show(1200,600)


    #if clicked Quit Program 
        #Break Out of While Loop and display Leaving Message
    x = styles.RedX(foreground.foreground, root)
    x.show()
    
    root.mainloop()