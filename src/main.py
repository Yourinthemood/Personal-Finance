#CP2 Group Project 3 
#Import all other files in src except JSON_management
import piecharts
import customtkinter
import signup

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

app = customtkinter.CTk()
app.configure(fg_color=from_rgb((100,0,0)))

#main function
def main():
  #DISPLAY custom tkinter login screen GUI
  #Log in screen will have an option to log in to an existing account or an option to create a new account
  
  root = customtkinter.CTk()
  root.geometry("720x1080")
  customtkinter.set_appearance_mode("dark")

  values = {"grey": "#35393C", "linen": "#F2E9DC", "strawberry": "#E34850", "blue": "#727FC8", "green": "#709775"}

  frame = customtkinter.CTkFrame(root)
  frame.pack(pady=20, padx=20, fill="both", expand=True)

  title = customtkinter.CTkFrame(
    master=frame,
    width=10,
    height=50,
    border_width=2,
    corner_radius=10,
    fg_color=values["strawberry"],
)
  title.pack(pady=25, padx=100, fill="both", expand=False)

  signup_btn = customtkinter.CTkButton(
    master=frame,
    border_width=2,
    border_color=from_rgb((0,0,0)),
    fg_color=values["green"],
    text="Sign Up",
    #command=signup.signup()
)
  signup_btn.pack(pady=20)

  login_btn = customtkinter.CTkButton(
    master=frame,
    text="Login",
    #command=login.login()
)
  login_btn.pack(pady=20)

  root.mainloop()




  #if the user clicks the New account button:
    #trigger create new account function
 
  #if the user clicks the Log in button:
    #trigger the log in function

  #Once the User has Logged in or Created a Account:
  #(While Logged in):
    #Welcome User to main program and DISPLAY buttons for the folowing:
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
      #if clicked New Expense:
        #trigger New Expense Function
      #if clicked Convert to Different Currency:
        #trigger Convert to Dif. Currency Function
      #if clicked Display Line Graph
        #trigger Line Graph Function
      #if Quit Program clicked
        #Break Out of While Loop and display Leaving Message
if __name__ == "__main__": 
    main()