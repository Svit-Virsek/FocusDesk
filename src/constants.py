import pygame
pygame.init()

# -- Constants --
RED = "#FF0000"
BLUE = "#0015FF"
GREEN = "#00FF08"
YELLOW = "#FFF700"
LIGHT_BLUE = "#00A6FF"
BLACK = "#000000"
WHITE = "#FFFFFF"
GREY = "#7F7F7F"
WIDTH = 1000
HEIGHT = 650
FONT_SMALL = pygame.font.SysFont(None, 25)
FONT_MEDIUM = pygame.font.SysFont(None, 40)

# -- Variables --
selected_timer = None

# -- Screen elements --
border = pygame.image.load("assets/images/border.png")
border = pygame.transform.scale(border, (200, 200))
add_timer = pygame.image.load("assets/images/add_timer.png")
add_timer = pygame.transform.scale(add_timer, (45, 45))
add_timer_rect = add_timer.get_rect(bottomright=(WIDTH-20, HEIGHT-20))
expand_timer = pygame.image.load("assets/images/expand_timer.png")
expand_timer = pygame.transform.scale(expand_timer, (35, 35))
reduce_timer = pygame.image.load("assets/images/reduce_timer.png")
reduce_timer = pygame.transform.scale(reduce_timer, (35, 35))
start_timer = pygame.image.load("assets/images/start.png")
start_timer = pygame.transform.scale(start_timer, (30, 30))
start_timer_rect = start_timer.get_rect(center=(WIDTH//2, HEIGHT//2+50))
stop_timer = pygame.image.load("assets/images/stop.png")
stop_timer = pygame.transform.scale(stop_timer, (30, 30))
stop_timer_rect = stop_timer.get_rect(center=(WIDTH//2, HEIGHT//2+50))

# -- Info texts --
info_rect = pygame.Rect(20, 605, 980, 25)
info_add_timer = FONT_SMALL.render("Add new timer.", True, GREY)
info_del = FONT_SMALL.render("Delete selected timers.", True, GREY)
info_select = FONT_SMALL.render("Select this timer.", True, GREY)
info_expand = FONT_SMALL.render("Expand this element.", True, GREY)
info_reduce = FONT_SMALL.render("Reduce this timer.", True, GREY)
info_start = FONT_SMALL.render("Start timer.", True, GREY)
info_stop = FONT_SMALL.render("Stop timer.", True, GREY)