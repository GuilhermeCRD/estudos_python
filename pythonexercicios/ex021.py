import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer_music.load(
    r'C:\Users\guigu\ Documents\ Arquivos vscode\estudos_python\pythonexercicios\ex021.mp3'
    )
pygame.mixer_music.play()
input('----- Aperte enter para para a musica -----')