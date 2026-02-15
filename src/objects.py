import pygame
from src.constants import *

class Timer:
    def __init__(self, duration: int, name: str, song: str, screen):
        self.duration = duration
        self.name = name
        self.song = song
        self.remaining = duration
        self.active = False
        self.choosen = False
        self.screen = screen
        self.text = self.remaining

    def start_timer(self):
        pygame.mixer.music.load(f"assets/sounds/{self.song}")
        pygame.mixer.music.play(-1)
        self.remaining = self.duration
        self.text = self.remaining
        self.active = True

    def update(self, x, y):
        if self.choosen:
            if self.active:
                self.text = FONT_MEDIUM.render(str(self.remaining), True, WHITE)
                self.text_rect = self.text.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(self.text, self.text_rect)
        elif not self.choosen:
            self.text = FONT_SMALL.render(str(self.remaining), True, WHITE)
            self.text_Rect = self.text.get_rect(center=(x*40, y*20))
            self.screen.blit(self.text, self.text_rect)