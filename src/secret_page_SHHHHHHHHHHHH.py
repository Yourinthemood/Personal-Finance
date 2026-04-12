#You are not suppossed to be here, Go away
import styles
import customtkinter as ctk, pygame

def show_secret():
    def change_music(selected):
        #Play matching song
        pygame.mixer.pause()
        match selected:
            case "Aria Math":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Aria Math.mp3")
                except:
                    pygame.mixer.music.load("assets/Aria Math.mp3")
            case "Buying Tacos":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Flowers Parody.mp3")
                except:
                    pygame.mixer.music.load("assets/Flowers Parody.mp3")
            case "Graze the roof":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Graze the Roof.mp3")
                except:
                    pygame.mixer.music.load("assets/Graze the Roof.mp3")
            case "Gusty Garden Galaxy theme":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Gusty Garden Galaxy.mp3")
                except:
                    pygame.mixer.music.load("assets/Gusty Garden Galaxy.mp3")
            case "Kass's theme":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Kass' Theme.mp3")
                except:
                    pygame.mixer.music.load("assets/Kass' Theme.mp3")
            case "Loonboon":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Loonboon.mp3")
                except:
                    pygame.mixer.music.load("assets/Loonboon.mp3")
            case "Mii Channel (plaza)":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Mii Channel (Plaza).mp3")
                except:
                    pygame.mixer.music.load("assets/Mii Channel (Plaza).mp3")
            case "Moog city 2":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Moog City 2.mp3")
                except:
                    pygame.mixer.music.load("assets/Moog City 2.mp3")
            case "Ultimate battle":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Ultimate Battle.mp3")
                except:
                    pygame.mixer.music.load("assets/Ultimate Battle.mp3")
            case "Wii Shop Channel":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Wii Shop Channel.mp3")
                except:
                    pygame.mixer.music.load("assets/Wii Shop Channel.mp3")
            case "Wii Sports Title Screen":
                try:
                    pygame.mixer.music.load("Personal-Finance/assets/Wii Sports Title Screen.mp3")
                except:
                    pygame.mixer.music.load("assets/Wii Sports Title Screen.mp3")
        pygame.mixer.music.play(loops=-1)

    root = ctk.CTk()
    root.geometry("2560x1440+0+0")
    root.attributes("-fullscreen", True)
    if styles.selected_mode == "1440p":
        root.geometry("2560x1440+0+0")
    elif styles.selected_mode == "1080p":
        root.geometry("1920x1080+0+0")
    elif styles.selected_mode == "fullscreen":
        root.attributes("-fullscreen", True)
    fg = styles.Foreground(root)
    fg.show()
    titlebox = styles.TitleBoxText(fg.foreground)
    titlebox.show()
    title = styles.OutputBox(titlebox.title,text="Secret Page! SHHH don't tell anyone")
    title.show()
    exitb = styles.RedX(fg.foreground,root)
    exitb.show()
    jukebox = styles.SegmentedButton(fg.foreground,change_music,["Aria Math","Buying Tacos","Graze the roof","Gusty Garden Galaxy theme","Kass's theme","Loonboon","Mii Channel (plaza)","Moog city 2","Ultimate battle","Wii Shop Channel","Wii Sports Title Screen"])
    jukebox.show()

    root.mainloop()