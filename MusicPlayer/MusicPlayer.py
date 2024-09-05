import os
import tkinter as tk
from tkinter import filedialog
import pygame  # For audio-playback

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk() # Creating the main window for the GUI
        self.root.title("Music Player")

        self.current_song = "" # Storing the path of the currently selected song
        self.paused = False # Not Paused Automatically

        # GUI elements
        self.label = tk.Label(self.root, text="Choose a song")
        self.label.pack() # Packs the widget into the GUI window

        # Methods: Select_Song and Play_Pause
        self.btn_select_song = tk.Button(self.root, text="Select Track", command=self.select_song)
        self.btn_select_song.pack()

        # Pause Button
        self.btn_play_pause = tk.Button(self.root, text="Play", command=self.play_pause)
        self.btn_play_pause.pack()

        self.volume_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack()

        # Starting the main event loop of the GUI (Keeps the GUI window active)
        # During Loop, Ensures the program stays running and responds to user interactions until the window is closed
        self.root.mainloop()

    # Opening a file-dialog to select a song, Storing seleted path file in song_path
    def select_song(self):
        song_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Song",
                                                   filetypes=(("MP3 Files", "*.mp3"),))
        if song_path:
            self.current_song = song_path
            self.label.config(text="Now playing: " + os.path.basename(song_path))


    #1. if self.current_song = Is song selected?
    #2. If that song is not paused, then we pause it
    #3. Updates the button text to "Play" and change its state to true
    #4. Otherwise, It Plays the music, Updates the button text to "Pause" and change the state to False meaning its playing
    def play_pause(self):
        if self.current_song:
            if not self.paused:
                pygame.mixer.music.load(self.current_song)
                pygame.mixer.music.play()
                self.paused = True
                self.btn_play_pause.config(text="Pause")
            else:
                pygame.mixer.music.pause()
                self.paused = False
                self.btn_play_pause.config(text="Play")

    # Dividing over 100 since the set_volume expects the value between 0.0-1.0
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

if __name__ == "__main__":
    pygame.mixer.init()
    music_player = MusicPlayer()