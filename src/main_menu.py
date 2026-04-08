#CP2 Group Project 3
import styles
import customtkinter as ctk


def main_menu():

    #Once the User has Logged in or Created a Account:
    #(While Logged in):
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    ctk.set_appearance_mode("dark")
  
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title)
    title.show()

    pie_chart = styles.BlueButton(foreground.foreground,"Pie Chart",command=lambda: print("Pie Chart Clicked"),sizex=300,sizey=100)
    pie_chart.show(400,400)

    line_graph = styles.BlueButton(foreground.foreground,"Line Graph",command=lambda: print("Line Graph Clicked"),sizex=300,sizey=100)
    line_graph.show(400,600)

    budget = styles.BlueButton(foreground.foreground,"Budgeting tools",command=lambda: print("Budgeting tools Clicked"),sizex=300,sizey=100)
    budget.show(800,400)

    currency_conv = styles.BlueButton(foreground.foreground,"Currency Conversion",command=lambda: print("Currency Conversion Clicked"),sizex=300,sizey=100)
    currency_conv.show(800,600)

    income = styles.BlueButton(foreground.foreground,"New Income",command=lambda: print("New Income Clicked"),sizex=300,sizey=100)
    income.show(1200,400)

    expense = styles.BlueButton(foreground.foreground,"New Expense",command=lambda: print("New Expense Clicked"),sizex=300,sizey=100)
    expense.show(1200,600)


    x = styles.RedX(foreground.foreground, root)
    x.show()
    

    root.mainloop()
        #Welcome User to main program and DISPLAY buttons for the following:
        #Budgeting tools and viewing money
        #Display Pie Chart
        #New Income Entry
        #New Expense Entry
        #Convert to Different Currency
        #Display Line Graph
        #Quit Program 

        #Match the user's click with the following:
        #if clicked Budgeting Tools:
            #trigger Budgeting Tools Menu Function
        #if clicked Display Pie Chart:
            #trigger Pie Chart Function
        #if clicked New Income:
            #trigger New Income Function
        #if cicked New Expense:
            #trligger New Expense Function
        #if clicked Convert to Different Currency:
            #trigger Convert to Dif. Currency Function
        #if clicked Display Line Graph
            #trigger Line Graph Function
        #if clicked Quit Program 
            #Break Out of While Loop and display Leaving Message
