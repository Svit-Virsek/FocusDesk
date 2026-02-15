import pygame, sys, json
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.display.flip()