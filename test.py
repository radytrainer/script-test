import os
import pyttsx3

second = 30

os.system(f'shutdown /s /t {second}')
pyttsx3.speak(f'Okay Brother I am shutting down your computer in next {second} seconds')

