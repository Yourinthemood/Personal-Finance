#CP2 Group Project 3
import styles, income_expenses, budgeting_tools, currencies, graphs
import customtkinter as ctk

def main_menu(source, username):
    #Once the User has Logged in or Created a Account:
    #(While Logged in):
    root = ctk.CTk()
    styles.apply_screen_resolution(root)
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

    if source == "login":
        warning = styles.Warning(foreground.foreground)
        warning_text = styles.OutputBox(warning.frame, "Succesfully logged in!", size=50)
        warning.show()
        warning_text.show()
    else:
        warning = styles.Warning(foreground.foreground)
        warning_text = styles.OutputBox(warning.frame, "New Account Created!", size=50)
        warning.show()
        warning_text.show()

    #if clicked Display Pie Chart:
        #trigger Pie Chart Function
    pie_chart = styles.BlueButton(foreground.foreground,"Pie Chart",command=lambda: graphs.pie_chart(username),sizex=650,sizey=250)
    pie_chart.show(400,600)

    #if clicked Display Line Graph
        #trigger Line Graph Function
    line_graph = styles.BlueButton(foreground.foreground,"Line Graph",command=lambda: graphs.line_graph(username),sizex=650,sizey=250)
    line_graph.show(400,1000)

    #if clicked Budgeting Tools:
        #trigger Budgeting Tools Menu Function
    budget = styles.BlueButton(foreground.foreground,"Budgeting tools",command=lambda: budgeting_tools.budgeting_tools(),sizex=650,sizey=250)
    budget.show(1200,600)

    #if clicked Convert to Different Currency:
        #trigger Convert to Dif. Currency Function
    currency_conv = styles.BlueButton(foreground.foreground,"Currency Conversion",command=lambda: currencies.convert(),sizex=650,sizey=250)
    currency_conv.show(1200,1000)

    #if clicked New Income:
        #trigger New Income Function
    income = styles.BlueButton(foreground.foreground,"New Income",command=lambda: income_expenses.income(username),sizex=650,sizey=250)
    income.show(2000,600)

    #if clicked New Expense:
        #trigger New Expense Function
    expense = styles.BlueButton(foreground.foreground,"New Expense",command=lambda: income_expenses.expenses(username),sizex=650,sizey=250)
    expense.show(2000,1000)


    #if clicked Quit Program 
        #Break Out of While Loop and display Leaving Message
    x = styles.RedX(foreground.foreground, root)
    x.show()
    
    root.mainloop()