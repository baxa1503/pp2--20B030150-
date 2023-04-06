import keyboard
import pygame.mixer

# initialize pygame mixer
pygame.mixer.init()

# load music files
music_files = ['song1.mp3', 'song2.mp3', 'song3.mp3']
current_song = 0
pygame.mixer.music.load(music_files[current_song])

# define keyboard callbacks
def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_song])
    pygame.mixer.music.play()

def previous_song():
    global current_song
    current_song = (current_song - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_song])
    pygame.mixer.music.play()

# register keyboard callbacks
keyboard.add_hotkey('space', play_music)
keyboard.add_hotkey('s', stop_music)
keyboard.add_hotkey('n', next_song)
keyboard.add_hotkey('p', previous_song)

# start the keyboard listener
keyboard.wait()
