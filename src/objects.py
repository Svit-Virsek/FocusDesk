import pygame, src.constants
from src.constants import *

class Timer:
    def __init__(self, duration: int, name: str, song: str, screen):
        self.duration = duration
        self.name = name
        self.song = song
        self.remaining = duration
        self.active = False
        self.screen = screen
        self.text = self.remaining
        self.text_rect = pygame.Rect(20, 20, 20, 20)
        self.border = border
        self.border_rect = pygame.Rect(20, 20, 20, 20)
        self.expand = expand_timer
        self.expand_rect = pygame.Rect(20, 20, 20, 20)
        self.reduce = reduce_timer
        self.reduce_rect = pygame.Rect(20, 20, 20, 20)
        self.start = start_timer
        self.start_rect = start_timer_rect
        self.stop = stop_timer
        self.stop_rect = stop_timer_rect
        self.remaining_min = 0
        self.remaining_sec = 0
        self.select_empty = select_empty
        self.select_tick = select_tick
        self.select_rect = pygame.Rect(20, 20, 20, 20)
        self.selected = False
        self.effect = False

    def initialize_timer(self):
        self.remaining = self.duration

    def stop_timer(self):
        self.active = False
        self.remaining = 0
        pygame.mixer.music.stop()

    def pause_timer(self):
        self.active = False
        pygame.mixer.music.stop()

    def unpause_timer(self):
        pygame.mixer.music.load(f"assets/sounds/{self.song}")
        pygame.mixer.music.play(-1)
        self.text = int(self.remaining)
        self.active = True

    def update(self, x, y):
        if src.constants.selected_timer == self:
            if self.active:
                if self.remaining!=0:
                    self.remaining_min = int(self.remaining//60)
                    self.remaining_sec = int(self.remaining%60)
                    self.text = FONT_MEDIUM.render(f"{self.remaining_min}:{self.remaining_sec}", True, BLACK)
                else:
                    self.text = FONT_MEDIUM.render("00:00", True, BLACK)
                self.text_rect = self.text.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(self.text, self.text_rect)
                self.border_rect = self.border.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(self.border, self.border_rect)
                self.reduce_rect = self.reduce.get_rect(center=(WIDTH//2+60, HEIGHT//2-60))
                self.screen.blit(self.reduce, self.reduce_rect)
                self.screen.blit(self.stop, self.stop_rect)
            elif not self.active:
                if self.remaining!=0:
                    self.remaining_min = int(self.remaining//60)
                    self.remaining_sec = int(self.remaining%60)
                    self.text = FONT_MEDIUM.render(f"{self.remaining_min}:{self.remaining_sec}", True, BLACK)
                else:
                    self.text = FONT_MEDIUM.render("00:00", True, BLACK)
                self.text_rect = self.text.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(self.text, self.text_rect)
                self.border_rect = self.border.get_rect(center=(WIDTH//2, HEIGHT//2))
                self.screen.blit(self.border, self.border_rect)
                self.reduce_rect = self.reduce.get_rect(center=(WIDTH//2+60, HEIGHT//2-60))
                self.screen.blit(self.reduce, self.reduce_rect)
                self.screen.blit(self.start, self.start_rect)
        elif src.constants.selected_timer==None:
            if self.remaining!=0:
                    self.remaining_min = int(self.remaining//60)
                    self.remaining_sec = int(self.remaining%60)
                    self.text = FONT_MEDIUM.render(f"{self.remaining_min}:{self.remaining_sec}", True, BLACK)
            else:
                self.text = FONT_MEDIUM.render("00:00", True, BLACK)
            self.text_rect = self.text.get_rect(center=(x*200+5, y*200))
            self.screen.blit(self.text, self.text_rect)
            self.border_rect = self.border.get_rect(center=(x*200+5, y*200))
            self.screen.blit(self.border, self.border_rect)
            self.expand_rect = self.expand.get_rect(center=(x*200+65, y*200-60))
            self.screen.blit(self.expand, self.expand_rect)
            self.select_rect = select_empty.get_rect(center=(x*200-60, y*200-60))
            if not self.effect:
                if not self.selected:
                    self.screen.blit(self.select_empty, self.select_rect)
                else:
                    self.screen.blit(self.select_tick, self.select_rect)
            if self.effect:
                self.screen.blit(self.select_tick, self.select_rect)