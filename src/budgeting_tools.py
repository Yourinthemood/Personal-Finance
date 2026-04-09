#CP2 Project 3 Personal Finance - Budgeting tools UI

import customtkinter as ctk
import styles

def savings_calc():
  root = ctk.CTk()
  root.geometry("2560x1440+0+0")
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Savings Goals")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()

  name = styles.TextBox(foreground.foreground, "Name of Goal: ")
  name.show(800,600)

  end = styles.TextBox(foreground.foreground, "End Goal: ")
  end.show(800,800)
  
  months = styles.TextBox(foreground.foreground, "How many months will this money be saved for: ")
  months.show(800,1000)

  root.mainloop()

def budget_calc():
  def each(num):
    for i in enumerate(num):
      root = ctk.CTk()
      root.geometry("2560x1440+0+0")
      ctk.set_appearance_mode("dark")

      foreground = styles.Foreground(root)
      foreground.show()

      titleframe = styles.TitleBoxText(foreground.foreground)
      titleframe.show()

      title = styles.OutputBox(titleframe.title, "Budget Allocator")
      title.show()

      x = styles.RedX(foreground.foreground, root)
      x.show()


      number = styles.TextBox(foreground.foreground, f"Enter Name of Category #{i}: ")
      number.show(800,600)

      amount = styles.TextBox(foreground.foreground, f"Enter Amount for Category #{i}: ")
      amount.show(800,800)

      submit_button = styles.SumbitButton(foreground.foreground, lambda: root.destroy())
      submit_button.show(x=1500, y=700)

  def check(num):
    try:
      num = int(num)
      each(num)
    except:
      pass

  root = ctk.CTk()
  root.geometry("2560x1440+0+0")
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Budget Allocator")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()


  categories = styles.TextBox(foreground.foreground, "Number of Categories: ")
  categories.show(800,600)

  submit_button = styles.SumbitButton(foreground.foreground, lambda: check(categories.get_text()))
  submit_button.show(x=1500, y=700)

  root.mainloop()

def interest_calc():
  root = ctk.CTk()
  root.geometry("2560x1440+0+0")
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Normal Interest Calculator")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()

  starting = styles.TextBox(foreground.foreground, "Starting Amount: ")
  starting.show(800,600)

  rate = styles.TextBox(foreground.foreground, "Interest Rate: ")
  rate.show(800,800)
  
  months = styles.TextBox(foreground.foreground, "How Long in Months: ")
  months.show(800,1000)

  root.mainloop()

def compound_calc():
  root = ctk.CTk()
  root.geometry("2560x1440+0+0")
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Compound Interest Calculator")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()


  starting = styles.TextBox(foreground.foreground, "Starting Amount: ")
  starting.show(800,600)

  rate = styles.TextBox(foreground.foreground, "Interest Rate: ")
  rate.show(800,800)
  
  months = styles.TextBox(foreground.foreground, "How Long in Months: ")
  months.show(800,1000)

  per = styles.TextBox(foreground.foreground, "Amount Added Per Month: ")
  per.show(800,1200)

  root.mainloop()

#Budgeting Tools UI Function:
def budgeting_tools():
  #Display All of the Budgeting tools on the window as buttons
  root = ctk.CTk()
  root.geometry("2560x1440+0+0")
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Budgeting Tools")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()


  savings_goal = styles.BlueButton(foreground.foreground,"Savings Goal Calculator",command=lambda: savings_calc(),sizex=600,sizey=100)
  savings_goal.show(400,400)

  budget_allocator = styles.BlueButton(foreground.foreground,"Budget Allocator",command=lambda: budget_calc(),sizex=600,sizey=100)
  budget_allocator.show(400,600)

  interest = styles.BlueButton(foreground.foreground,"Interest Calculator",command=lambda: interest_calc,sizex=600,sizey=100)
  interest.show(1200,400)

  compound = styles.BlueButton(foreground.foreground,"Compound Interest Calculator",command=lambda: compound_calc(),sizex=600,sizey=100)
  compound.show(1200,600)

  root.mainloop()
  #if the user clicks a button, load that function. Functions:
    #Savings Goals
    #Budget Allocator
    #Interest Calculator
    #Compound Interest Calculator
    #Leave Budgeting Tools - Leaves this function instead of calling a new one
