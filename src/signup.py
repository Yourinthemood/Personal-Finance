#CP2 Project 3
import styles, JSON_management, main_menu
import customtkinter as ctk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(loops=-1)

#Sign up function:
def signup():
    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    ctk.set_appearance_mode("dark")

    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    x = styles.RedX(foreground.foreground, root)
    x.show(1650,150)

    username_box = styles.TextBox(foreground,"Username: ")
    username_box.show(700,500)

    password_box = styles.TextBox(foreground, "Password: ")
    password_box.show(900,500)

    submit_button = styles.SumbitButton(foreground, lambda: print(f"{username_box.get_text()}:{password_box.get_text()}"), sizex=200, sizey=100)
    submit_button.show(x=100, y=100)

    root.mainloop()
  #Loop until User Gets Unique Password
    #Display a Field for the User to type in which has a caption above it titled: Username. Below that, Have an Enter Button to submit what they have in the field

    #if Username is Unique:
      #Break Out of loop
    #if Username is Not Unique:
      #Display Message to User that their Username is not unique and then go through the loop again

  #Loop Until the Password Is Stong
    #Display a Field for the User to type in which has the caption above it titled: Password. Below that Have a Enter Button to submit what they have in the field

    #Run password Strength Checking Function
    #if Password Strength is strong enough
      #leave loop
    #if Password Strength is Weak:
      #Display to User what they did wrong and then go through the loop again

  #Save the User To the JSON
