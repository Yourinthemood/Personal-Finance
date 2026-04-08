#CP2 Project 3 Financial Calculations, Login Function
import styles
import customtkinter as ctk
#Login Function:
def log_in():
  #loop until login complete:
    #Display a Log in screen that has two text box fields labeled Username and Password Respectively. After those have a Enter or submit buttont to send info here
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    ctk.set_appearance_mode("dark")

    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    root.mainloop()

    #Search JSON for the User and their Info

    #if the Username is not there:
      #Display User Does not Exist message and then restart loop

    #if Username is existant:
      #if the Password matches the User,
        #return
      #If password does not match User password
        #Display Incorrect Password Message

log_in()