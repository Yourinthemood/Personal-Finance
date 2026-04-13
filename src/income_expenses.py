import customtkinter as ctk, csv, datetime
import styles, secret_page_SHHHHHHHHHHHH

def income(username):
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    root.attributes("-fullscreen", True)
    if styles.selected_mode == "1440p":
        root.geometry("2560x1440+0+0")
    elif styles.selected_mode == "1080p":
        root.geometry("1920x1080+0+0")
    elif styles.selected_mode == "fullscreen":
        root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")

    def check():
        amt = amount.get_text()
        cate = cat.get_text()
        try:
            float(amt)
        except ValueError:
            popup = styles.Popup(foreground.foreground)
            popup_text = styles.OutputBox(popup.frame, "That wasn't a valid amount...", size=50)
            popup.show()
            popup_text.show()
            return

        with open("files/incomes.csv", "a", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amt, cate])
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

    cat = styles.TextBox(foreground.foreground, "Income Category: ")
    cat.show(700,800)

    submit_button = styles.SumbitButton(foreground.foreground, lambda: check(), sizex=500, sizey=300)
    submit_button.show(1800, 700)

    root.mainloop()

def expenses(username):
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    root.attributes("-fullscreen", True)
    if styles.selected_mode == "1440p":
        root.geometry("2560x1440+0+0")
    elif styles.selected_mode == "1080p":
        root.geometry("1920x1080+0+0")
    elif styles.selected_mode == "fullscreen":
        root.attributes("-fullscreen", True)
    ctk.set_appearance_mode("dark")

    def check():
        amt = amount.get_text()
        nme = name.get_text()
        try:
            float(amt)
        except ValueError:
            popup = styles.Popup(foreground.foreground)
            popup_text = styles.OutputBox(popup.frame, "That wasn't a valid amount...", size=50)
            popup.show()
            popup_text.show()
            return

        with open("files/expenses.csv", "a", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amt, nme])
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

    name = styles.TextBox(foreground.foreground, "Expense Category: ")
    name.show(700,800)

    submit_button = styles.SumbitButton(foreground.foreground, lambda: check(), sizex=500, sizey=300)
    submit_button.show(1800, 700)

    if styles.selected_mode == "1440p":
        scale_x = 1.0
        scale_y = 1.0
    elif styles.selected_mode == "1080p":
        scale_x = 1920 / 2560
        scale_y = 1080 / 1440
    elif styles.selected_mode == "fullscreen":
        scale_x = 1.0
        scale_y = 1.0

    secret_button_totally = ctk.CTkButton(
            master=root,
            width=100,
            height=100,
            fg_color="#242424",
            command=secret_page_SHHHHHHHHHHHH.show_secret,
            text="",
        )
    secret_button_totally.place(x=int(2560 * scale_x) - 50, y=int(1440 * scale_y) - 50, anchor="center")
    secret_button_totally.configure(width=int(100 * scale_x), height=int(100 * scale_y))

    root.mainloop()