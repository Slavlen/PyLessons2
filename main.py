import pygame
import sys
import playtable

pygame.init()

while True:
    playtable.check_event()
    playtable.draw_table()
    pygame.display.update()
