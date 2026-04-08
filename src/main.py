#CP2 Group Project 3 
#Import all other files in src except JSON_management
import piecharts, styles
import customtkinter as ctk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Flowers Parody _ David Lopez 4.mp3")
pygame.mixer.music.play(loops=-1)

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

  title = styles.OutputBox(titleframe.title)
  title.show()

  x = styles.RedX(foreground.foreground, command=lambda: print("Quit clicked"))
  x.show()
  
  #if the user clicks the New account button:
    #trigger create new account function
  login_btn = styles.BlueButton(foreground.foreground, "Log In", command=lambda: print("Log in clicked"))
  login_btn.show()
 
  #if the user clicks the Log in button:
    #trigger the log in function
  signup_btn = styles.GreenButton(foreground.foreground, "New Account", command=lambda: print("Sign up clicked"))
  signup_btn.show()

  root.mainloop()

  #Once the User has Logged in or Created a Account:
  #(While Logged in):
    #Welcome User to main program and DISPLAY buttons for the following:
      #Budgeting tools and viewing money
      #Display Pie Chart
      #New Income Entry
      #New Expense Entry
      #Convert to Different Currency
      #Display Line Graph
      #Quit Program 

    #Match the user's click with the following:
      #if clicked Budgeting Tools:
        #trigger Budgeting Tools Menu Function
      #if clicked Display Pie Chart:
        #trigger Pie Chart Function
      #if clicked New Income:
        #trigger New Income Function
      #if cicked New Expense:
        #trligger New Expense Function
      #if clicked Convert to Different Currency:
        #trigger Convert to Dif. Currency Function
      #if clicked Display Line Graph
        #trigger Line Graph Function
      #if clicked Quit Program 
        #Break Out of While Loop and display Leaving Message
      
if __name__ == "__main__": 
    main()