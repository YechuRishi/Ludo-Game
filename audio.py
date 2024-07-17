import tkinter as tk
import pygame

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load('./assets/dice.mp3')  # Replace with the path to your MP3 audio file
    pygame.mixer.music.play()

app = tk.Tk()
app.title("MP3 Audio Player")

play_button = tk.Button(app, text="Play Audio", command=play_audio)
play_button.pack(pady=20)

app.mainloop()
