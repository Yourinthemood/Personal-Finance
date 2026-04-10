import customtkinter as ctk, csv
import styles

def income(mode):
  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
  ctk.set_appearance_mode("dark")

  def check():
    amt = amount.get_text()
    nme = name.get_text()
    try:
        float(amt)
    except ValueError:
        return

    with open("files/incomes.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([nme, amt])
    root.destroy()
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "New Income")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()
  

  amount = styles.TextBox(foreground.foreground, "Amount: ")
  amount.show(700,600)

  name = styles.TextBox(foreground.foreground, "Income Name: ")
  name.show(700,800)

  submit_button = styles.SumbitButton(foreground.foreground, lambda: check(), sizex=500, sizey=300)
  submit_button.show(1800, 700)

  root.mainloop()

def expenses(mode):
  root = ctk.CTk()
  if mode == "1440p":
    root.geometry("2560x1440+0+0")
  elif mode == "1080p":
    root.geometry("1920x1080+0+0")
  elif mode == "fullscreen":
    root.attributes("-fullscreen", True)
  ctk.set_appearance_mode("dark")

  def check():
    amt = amount.get_text()
    nme = name.get_text()
    try:
        float(amt)
    except ValueError:
        return

    with open("files/expenses.csv", "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([nme, amt])
    root.destroy()
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "New Expense")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()
  
  
  amount = styles.TextBox(foreground.foreground, "Amount: ")
  amount.show(700,600)

  name = styles.TextBox(foreground.foreground, "Expense Name: ")
  name.show(700,800)

  submit_button = styles.SumbitButton(foreground.foreground, lambda: check(), sizex=500, sizey=300)
  submit_button.show(1800, 700)

  root.mainloop()