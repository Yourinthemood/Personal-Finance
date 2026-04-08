#CP2 Project 3 Financial Calculations, Login Function
import styles, JSON_management, main_menu
import customtkinter as ctk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(loops=-1)

#Login Function:
def log_in():
  #loop until login complete:
    #Display a Log in screen that has two text box fields labeled Username and Password Respectively. After those have a Enter or submit buttont to send info here
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    ctk.set_appearance_mode("dark")

    foreground = styles.Foreground(root)
    foreground.show()

    x = styles.RedX(foreground.foreground, root)
    x.show(1650,150)

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    username_box = styles.TextBox(foreground.foreground,"Username: ")
    username_box.show(700,500)

    password_box = styles.TextBox(foreground.foreground, "Password: ")
    password_box.show(700,500)

    submit_button = styles.SumbitButton(foreground.foreground,lambda: print(f"{username_box.get_text()}:{password_box.get_text()}"), sizex=100, sizey=50)
    submit_button.show(x=1000,y=100)

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
