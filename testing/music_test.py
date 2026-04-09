import pygame, time

pygame.mixer.init()
pygame.mixer.music.load("The Price is Right theme song 4.mp3")
pygame.mixer.music.play(loops=-1)

while pygame.mixer.music.get_busy():
    time.sleep(0.1)