import pygame, sys, json, src.constants
from pygame.locals import *
from src.constants import *
from src.objects import *
pygame.init()

# -- Collect data --
def load_timers():
    with open("assets/data/timers.json") as f:
        data = json.load(f)

    output = []
    for element in data:
        output.append(Timer(element["duration"], element["name"], element["song"], screen))

    return output

def save_timers(data):
    to_save = []
    for element in data:
        to_save.append({"duration":element.duration, "name":element.name, "song":element.song})
    with open("assets/data/timers.json", "w") as f:
        json.dump(to_save, f, indent=4)

# -- Screen elements --
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timers = load_timers()

# -- Main loop --
running = True
while running:
    # -- Event handling --
    MOUSE_POS = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if src.constants.selected_timer==None:
                    for element in timers:
                        if element.expand_rect.collidepoint(MOUSE_POS):
                            src.constants.selected_timer = element
                            break
                elif src.constants.selected_timer!=None:
                    if src.constants.selected_timer.reduce_rect.collidepoint(MOUSE_POS):
                        src.constants.selected_timer = None
                        pygame.mixer.music.stop()
                        break
                    if src.constants.selected_timer.start_rect.collidepoint(MOUSE_POS) and not src.constants.selected_timer.active:
                        src.constants.selected_timer.start_timer()
                        break
                    if src.constants.selected_timer.stop_rect.collidepoint(MOUSE_POS) and src.constants.selected_timer.active:
                        src.constants.selected_timer.active = False
                        pygame.mixer.music.stop()
                        break

    # -- Draw elemnts --
    screen.fill(WHITE)
    x=1
    y=1
    for element in timers:
        element.update(x, y)
        x+=1
        if(x%5==0):
            y+=1
            x=1
    screen.blit(add_timer, add_timer_rect)

    # -- Info texts --
    if src.constants.selected_timer==None:
        for element in timers:
            if element.expand_rect.collidepoint(MOUSE_POS):
                screen.blit(info_expand, info_rect)
    elif src.constants.selected_timer!=None:
        if src.constants.selected_timer.reduce_rect.collidepoint(MOUSE_POS):
            screen.blit(info_reduce, info_rect)
        if src.constants.start_timer_rect.collidepoint(MOUSE_POS) and not src.constants.selected_timer.active:
            screen.blit(info_start, info_rect)
        elif src.constants.stop_timer_rect.collidepoint(MOUSE_POS) and src.constants.selected_timer.active:
            screen.blit(info_stop, info_rect)
    if add_timer_rect.collidepoint(MOUSE_POS):
        screen.blit(info_add_timer, info_rect)

    pygame.display.flip()