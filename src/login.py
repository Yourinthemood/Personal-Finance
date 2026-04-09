#CP2 Project 3 Financial Calculations, Login Function
import styles, JSON_management, main_menu
import customtkinter as ctk

#Login Function:
def log_in(mode):
  #loop until login complete:
    #Display a Log in screen that has two text box fields labeled Username and Password Respectively. After those have a Enter or submit buttont to send info here
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

    x = styles.RedX(foreground.foreground, root)
    x.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Log In")
    title.show()

    username_box = styles.TextBox(foreground.foreground,"Username: ")
    username_box.show(800,600)

    password_box = styles.TextBox(foreground.foreground, "Password: ")
    password_box.show(800,800)

    submit_button = styles.SumbitButton(foreground.foreground,lambda: main_menu.main_menu(mode))
    submit_button.show(x=1500, y=700)

    root.mainloop()

    #Search JSON for the User and their Info
    user_info = JSON_management.JSON_reader()

    #if the Username is not there:
      #Display User Does not Exist message and then restart loop

    #if Username is existant:
      #if the Password matches the User,
        #return
      #If password does not match User password
        #Display Incorrect Password Message
