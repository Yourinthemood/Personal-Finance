#CP2 Group Project 3 
#Import all other files in src except JSON_management
import styles, login, signup
import customtkinter as ctk, pygame, os

pygame.mixer.init()
try:
  pygame.mixer.music.load("Personal-Finance/music.mp3")
except:
  pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(loops=-1)
os.system("cls")
print("THIS PROJECT IS BUILT FOR A MONITOR WITH 2560x1440px, OTHERWISE IT LOOKS WEIRD!")

#main function
def main():
  #DISPLAY custom tkinter login screen GUI
  #Log in screen will have an option to log in to an existing account or an option to create a new account
  
  root = ctk.CTk()
  root.geometry("2560x1440+0+0")
  ctk.set_appearance_mode("dark")
  
  foreground = styles.Foreground(root)
  foreground.show()

  titleframe = styles.TitleBoxText(foreground.foreground)
  titleframe.show()

  title = styles.OutputBox(titleframe.title, "Personal Finance App")
  title.show()

  x = styles.RedX(foreground.foreground, root)
  x.show()
  
  #if the user clicks the New account button:
    #trigger create new account function
  login_btn = styles.BlueButton(foreground.foreground, "Log In", command=login.log_in, sizex=500, sizey=200)
  login_btn.show(1000,750)
 
  #if the user clicks the Log in button:
    #trigger the log in function
  signup_btn = styles.GreenButton(foreground.foreground, "New Account", command=signup.signup, sizex=500, sizey=200)
  signup_btn.show(1560,750)

  root.mainloop()

main()