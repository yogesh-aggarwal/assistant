import pygame
import os
from gtts import gTTS
from io import BytesIO

my_variable = 'hello' # your real code gets this from the chatbot

# mp3_fp = BytesIO()
tts = gTTS(my_variable, 'en')
tts.save("welcome.mp3")

# os.startfile("welcome.mp3")

file = r'F:\Python\AI\assistant\welcome.mp3'
pygame.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
# pygame.event.wait()