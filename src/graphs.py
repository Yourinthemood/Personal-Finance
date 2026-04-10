import customtkinter as ctk
import styles

def line_graph(mode):
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

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Line Graph")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()

def pie_chart(mode):
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

    titleframe = styles.TitleBoxText(foreground.foreground)
    titleframe.show()

    title = styles.OutputBox(titleframe.title, "Pie Charts")
    title.show()

    x = styles.RedX(foreground.foreground, root)
    x.show()