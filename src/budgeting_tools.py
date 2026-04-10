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

    def update():
        goal_name = name.get_text()
        end_val = end.get_text()
        months_val = months.get_text()

        try:
            end_num = float(end_val)
            months_num = float(months_val)
            monthly = end_num / months_num
            result = f"{goal_name}\n${monthly:.2f}/month\nfor {months_num:.1f} months\nto reach ${end_num:.2f}"
        except (ValueError, ZeroDivisionError):
            result = "Waiting for input..."

        text.text.configure(text=result)
        root.after(10, update)
    
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Savings Goals")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()


    name = styles.TextBox(foreground.foreground, "Name of Goal: ")
    name.show(700, 400)

    end = styles.TextBox(foreground.foreground, "End Goal: ")
    end.show(700, 700)

    months = styles.TextBox(foreground.foreground, "How many months: ")
    months.show(700, 1000)

    output = styles.OutputFrame(foreground.foreground, sizey=600)
    output.show(1800, 700)

    text = styles.OutputBox(output.frame, "", size=75)
    text.show()

    update()
    root.mainloop()

def budget_calc(mode):
    results = []
    num_categories = [0]

    def make_root():
        r = ctk.CTk()
        if mode == "1440p":
            r.geometry("2560x1440+0+0")
        elif mode == "1080p":
            r.geometry("1920x1080+0+0")
        elif mode == "fullscreen":
            r.attributes("-fullscreen", True)
        ctk.set_appearance_mode("dark")
        return r

    def each(num):
        for i in range(num):
            cat_root = make_root()

            foreground = styles.Foreground(cat_root)
            foreground.show()

            titleframe = styles.TitleBoxText(foreground.foreground)
            titleframe.show()

            title = styles.OutputBox(titleframe.title, "Budget Allocator")
            title.show()

            x = styles.RedX(foreground.foreground, cat_root)
            x.show()

            number = styles.TextBox(foreground.foreground, f"Enter Name of Category #{i + 1}: ")
            number.show(800, 600)

            amount = styles.TextBox(foreground.foreground, f"Enter Amount for Category #{i + 1}: ")
            amount.show(800, 800)

            def submit(n=number, a=amount, r=cat_root):
                results.append({"name": n.get_text(), "amount": a.get_text()})
                r.quit()
                r.destroy()

            submit_button = styles.SumbitButton(foreground.foreground, submit)
            submit_button.show(x=1500, y=700)

            cat_root.mainloop()

        print(results)

    def check():
        try:
            num_categories[0] = int(categories.get_text())
            root.quit()
            root.destroy()
            each(num_categories[0])
        except ValueError:
            pass

    root = make_root()

    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Budget Allocator")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()

    categories = styles.TextBox(foreground.foreground, "Number of Categories: ")
    categories.show(800, 600)

    submit_button = styles.SumbitButton(foreground.foreground, check)
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

    def update():
        starting_val = starting.get_text()
        rate_val = rate.get_text()
        years_val = years.get_text()
        size = 75

        try:
            starting_num = float(starting_val)
            rate_num = float(rate_val)
            years_num = float(years_val)
            result = f"${(years_num*rate_num*starting_num):.2f}"
            size = 150
        except (ValueError, ZeroDivisionError):
            result = "Waiting for input..."
            size = 75

        text.text.configure(text=result, font=("Dongle", size))
        root.after(10, update)
    
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Normal Interest Calculator")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()


    starting = styles.TextBox(foreground.foreground, "Starting Amount: ")
    starting.show(700,400)

    rate = styles.TextBox(foreground.foreground, "Interest Rate:")
    rate.show(700,700)
    
    years = styles.TextBox(foreground.foreground, "How Long in Years: ")
    years.show(700,1000)

    output = styles.OutputFrame(foreground.foreground, sizey=600)
    output.show(1800, 700)

    text = styles.OutputBox(output.frame, "", size=150)
    text.show()

    update()
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

    def update():
        starting_val = starting.get_text()
        rate_val = rate.get_text()
        years_val = years.get_text()
        per_val = per.get_text()
        size = 75

        try:
            starting_num = float(starting_val)
            rate_num = float(rate_val)
            years_num = float(years_val)
            per_num = float(per_val)
            result = f"${(starting_num*((1+(rate_num/per_num))**(per_num*years_num))):.2f}"
            size = 100
        except (ValueError, ZeroDivisionError):
            result = "Waiting for input..."
            size = 75

        text.text.configure(text=result, font=("Dongle", size))
        root.after(10, update)
    
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Compound Interest Calculator")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()


    starting = styles.TextBox(foreground.foreground, "Starting Amount: ")
    starting.show(700,400)

    rate = styles.TextBox(foreground.foreground, "Interest Rate: ")
    rate.show(700,600)
    
    years = styles.TextBox(foreground.foreground, "How Long in Years: ")
    years.show(700,800)

    per = styles.TextBox(foreground.foreground, "Times Compounded Each Year: ")
    per.show(700,1000)

    output = styles.OutputFrame(foreground.foreground, sizey=600)
    output.show(1800, 700)

    text = styles.OutputBox(output.frame, "", size=150)
    text.show()

    update()
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


    savings_goal = styles.BlueButton(foreground.foreground,"Savings Goal Calculator",command=lambda: savings_calc(mode),sizex=1000,sizey=250)
    savings_goal.show(600,600)

    budget_allocator = styles.BlueButton(foreground.foreground,"Budget Allocator",command=lambda: budget_calc(mode),sizex=1000,sizey=250)
    budget_allocator.show(600,1000)

    interest = styles.BlueButton(foreground.foreground,"Interest Calculator",command=lambda: interest_calc(mode),sizex=1000,sizey=250)
    interest.show(1800,600)

    compound = styles.BlueButton(foreground.foreground,"Compound Interest Calculator",command=lambda: compound_calc(mode),sizex=1000,sizey=250)
    compound.show(1800,1000)

    root.mainloop()
    #if the user clicks a button, load that function. Functions:
        #Savings Goals
        #Budget Allocator
        #Interest Calculator
        #Compound Interest Calculator
        #Leave Budgeting Tools - Leaves this function instead of calling a new one
