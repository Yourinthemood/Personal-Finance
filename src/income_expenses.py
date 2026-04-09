import customtkinter as ctk
import styles

def income():
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    ctk.set_appearance_mode("dark")
    
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "New Income")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()
    
    username_box = styles.TextBox(foreground.foreground, "How Long in Months: ")
    username_box.show(800,600)

    password_box = styles.TextBox(foreground.foreground, "Income Name: ")
    password_box.show(800,800)

    submit_button = styles.SumbitButton(foreground.foreground, lambda: root.destroy())
    submit_button.show(x=1500, y=700)

    root.mainloop()

def expenses():
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    ctk.set_appearance_mode("dark")
    
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "New Expense")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()
    
    username_box = styles.TextBox(foreground.foreground, "Amount Expended: ")
    username_box.show(800,600)

    password_box = styles.TextBox(foreground.foreground, "Expense Name: ")
    password_box.show(800,800)

    submit_button = styles.SumbitButton(foreground.foreground, lambda: root.destroy())
    submit_button.show(x=1500, y=700)

    root.mainloop()