import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def generate_frames(text):
    frames = []
    for i in range(1, len(text) + 1):
        frames.append(text[:i])
    return frames

def animated_print(frames, repetitions):
    for _ in range(repetitions):
        for frame in frames:
            print("\r" + frame, end="")
            time.sleep(0.25)
            clear_screen()

text = "Hola, mundo!"
frames = generate_frames(text)
repetitions = 3
animated_print(frames, repetitions)
