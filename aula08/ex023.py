"""
Tocando um mp3 com python3
"""

import pygame
pygame.init()
pygame.mixer.music.load('ex023.mp3')
pygame.mixer.music.play()
pygame.event.wait()
