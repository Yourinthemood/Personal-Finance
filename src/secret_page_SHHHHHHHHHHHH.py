#You are not suppossed to be here, Go away
import styles
import customtkinter as ctk, pygame

def show_secret():
    def change_music():
        #Play matching song
        pygame.mixer.pause()
        match selected:
            case "Aria Math":
                print("AREA MATH")
            case "Buying Tacos":
                print("I CAN BUY MYSELF TACOS")
            case "Graze the roof":
                print("MARK ROBERING INTESIFIES")
            case "Gusty Garden Galaxy theme":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Gusty Garden Galaxy.mp3")
                except:
                    pygame.mixer.music.load("assets/Gusty Garden Galaxy.mp3")
                pygame.mixer.music.play(loops=-1)
            case "Kass's theme (default)":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Kass' Theme.mp3")
                except:
                    pygame.mixer.music.load("assets/Kass' Theme.mp3")
                pygame.mixer.music.play(loops=-1)
            case "Loonboon":
                print("DESTROY ZOMBIES")
            case "Mii Channel (plaza)":
                print("THAT'S NOT ME")
            case "Moog city 2":
                print("RELAX.YES")
            case "music":
                print("UHH IDK WHAT THIS DOES")
            case "Ultimate battle":
                print("NOT SO ULTIMATE NOW")
            case "Wii Shop Channel":
                print("GO SHOPING")
            case "Wii Sports Title Screen":
                print("DO DO DO DO DO DO DOOOOOOOOOOOOOOOOOOOOOOOOOO")

    root = ctk.CTk()
    fg = styles.Foreground(root)
    fg.show()
    titlebox = styles.TitleBoxText(fg.foreground)
    titlebox.show()
    title = styles.OutputBox(titlebox.title,text="Secret Page! SHHH don't tell anyone")
    title.show()
    exitb = styles.RedX(fg.foreground,root)
    exitb.show()
    jukebox = styles.SegmentedButton(fg.foreground,change_music,["Aria Math","Buying Tacos","Graze the roof","Gusty Garden Galaxy theme","Kass's theme (default)","Loonboon","Mii Channel (plaza)","Moog city 2","music","Ultimate battle","Wii Shop Channel","Wii Sports Title Screen"])
    jukebox.show()
    selected = jukebox.get_option()
    

    root.mainloop()