#CP2 Group Project 3 
#Import all other files in src except JSON_management
import styles, login, signup
import customtkinter as ctk, pygame, os

pygame.mixer.init()
try:
    pygame.mixer.music.load("Personal-Finance/assets/Kass' Theme.mp3")
except:
    pygame.mixer.music.load("assets/Kass' Theme.mp3")
pygame.mixer.music.play(loops=-1)
os.system("cls")

#main function
def login_screen():
    def send(login_signup):
        root.destroy()
        if login_signup == "login":
            login.log_in()
        else:
            signup.signup()

    #DISPLAY custom tkinter login screen GUI
    #Log in screen will have an option to log in to an existing account or an option to create a new account
  
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
    
    foreground = styles.Foreground(root)
    foreground.show()

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Personal Finance App")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()


    # Ad Warning & Ad
    warning = styles.Warning(foreground.foreground)
    warning_text = styles.OutputBox(warning.frame, "Click on ads to close them.", size=50)
    warning.show()
    warning_text.show()
    styles.Ads()
    
    #if the user clicks the New account button:
        #trigger create new account function
    login_btn = styles.BlueButton(foreground.foreground, "Log In", command=lambda: send("login"), sizex=1000, sizey=250)
    login_btn.show(600,750)
    
    #if the user clicks the Log in button:
        #trigger the log in function
    signup_btn = styles.GreenButton(foreground.foreground, "New Account", command=lambda: send("signup"), sizex=1000, sizey=250)
    signup_btn.show(1800,750)

    root.mainloop()

def main():
    root = ctk.CTk()
    root.geometry("300x250")
    ctk.set_appearance_mode("dark")

    label = ctk.CTkLabel(root, text="Select Resolution Mode")
    label.pack(pady=20)
    
    def set_1440p():
        styles.selected_mode = "1440p"
        styles.update_scales()
        root.destroy()
        login_screen()
    
    def set_1080p():
        styles.selected_mode = "1080p"
        styles.update_scales()
        root.destroy()
        login_screen()
    
    def set_fullscreen():
        styles.selected_mode = "fullscreen"
        styles.update_scales()
        root.destroy()
        login_screen()
    
    btn1440 = ctk.CTkButton(root, text="1440p (2560x1440)", command=set_1440p)
    btn1440.pack(pady=10)
    
    btn1080 = ctk.CTkButton(root, text="1080p (1920x1080)", command=set_1080p)
    btn1080.pack(pady=10)
    
    btn_full = ctk.CTkButton(root, text="Fullscreen", command=set_fullscreen)
    btn_full.pack(pady=10)
    
    root.mainloop()
main()