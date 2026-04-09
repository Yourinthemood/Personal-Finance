#CP2 Project 3 Personal Finance - Budgeting tools UI

import customtkinter as ctk
import styles

def savings_calc(mode):
  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Savings Goals")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()


  name = styles.TextBox(foreground.foreground, "Name of Goal: ", sizex=1500)
  name.show(900,400)

  end = styles.TextBox(foreground.foreground, "End Goal: ", sizex=1500)
  end.show(900,700)
  
  months = styles.TextBox(foreground.foreground, "How many months: ", sizex=1500)
  months.show(900,1000)


  output = styles.OutputFrame(foreground.foreground, sizex=500, sizey=500)
  output.show(2100, 700)

  #text = styles.OutputBox()

  root.mainloop()

def budget_calc(mode):
  def each(num, mode):
    for i in enumerate(num):
      root = ctk.CTk()
      if mode == "1440p":
        root.geometry("2560x1440+0+0")
      elif mode == "1080p":
        root.geometry("1920x1080+0+0")
      elif mode == "fullscreen":
        root.attributes("-fullscreen", True)
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

  def check(num, mode):
    try:
      num = int(num)
      each(num, mode)
    except:
      pass

  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
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

  submit_button = styles.SumbitButton(foreground.foreground, lambda: check(categories.get_text(), mode))
  submit_button.show(x=1500, y=700)

  root.mainloop()

def interest_calc(mode):
  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
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

def compound_calc(mode):
  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Compound Interest Calculator")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()


  starting = styles.TextBox(foreground.foreground, "Starting Amount: ", sizex=1500)
  starting.show(1000,400)

  rate = styles.TextBox(foreground.foreground, "Interest Rate: ", sizex=1500)
  rate.show(1000,600)
  
  months = styles.TextBox(foreground.foreground, "How Long in Months: ", sizex=1500)
  months.show(1000,800)

  per = styles.TextBox(foreground.foreground, "Amount Added Per Month: ", sizex=1500)
  per.show(1000,1000)

  root.mainloop()

#Budgeting Tools UI Function:
def budgeting_tools(mode):
  #Display All of the Budgeting tools on the window as buttons
  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Budgeting Tools")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()


  savings_goal = styles.BlueButton(foreground.foreground,"Savings Goal Calculator",command=lambda: savings_calc(mode),sizex=600,sizey=100)
  savings_goal.show(400,400)

  budget_allocator = styles.BlueButton(foreground.foreground,"Budget Allocator",command=lambda: budget_calc(mode),sizex=600,sizey=100)
  budget_allocator.show(400,600)

  interest = styles.BlueButton(foreground.foreground,"Interest Calculator",command=lambda: interest_calc(mode),sizex=600,sizey=100)
  interest.show(1200,400)

  compound = styles.BlueButton(foreground.foreground,"Compound Interest Calculator",command=lambda: compound_calc(mode),sizex=600,sizey=100)
  compound.show(1200,600)

  root.mainloop()
  #if the user clicks a button, load that function. Functions:
    #Savings Goals
    #Budget Allocator
    #Interest Calculator
    #Compound Interest Calculator
    #Leave Budgeting Tools - Leaves this function instead of calling a new one
