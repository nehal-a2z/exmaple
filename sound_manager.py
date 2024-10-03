import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound("move.wav")

    def play_move_sound(self):
        self.move_sound.play()
