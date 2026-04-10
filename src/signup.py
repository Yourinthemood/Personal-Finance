#CP2 Project 3
import styles, JSON_management, main_menu
import customtkinter as ctk, hashlib

#Sign up function:
def signup(mode):
    def send(username,password):
        pasw = password.encode("utf-8")
        pasw = hashlib.blake2b(pasw).hexdigest()
        data = {
            "Username":username,
            "Password":pasw
        }
        JSON_management.JSON_add(data)
        root.destroy()
        main_menu.main_menu(mode, source="signup")

        
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

    titleframe = styles.TitleBoxText(foreground.foreground)#You need some tacos to feel better!!!
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Sign Up")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()


    username_box = styles.TextBox(foreground.foreground,"Username: ")
    username_box.show(700,600)

    password_box = styles.TextBox(foreground.foreground, "Password: ")
    password_box.show(700,800)

    submit_button = styles.SumbitButton(foreground.foreground,lambda: send(username_box.get_text(),password_box.get_text()), sizex=500, sizey=300)
    submit_button.show(1800, 700)

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
