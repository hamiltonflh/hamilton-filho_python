import pygame
pygame.init()

//O arquivo da musica precisa estar na pasta do projeto
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
pygane.event.wait()
