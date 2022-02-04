import pygame
from pygame.locals import *
import random
from maze import Maze

size = width, height = 800, 800

bgcolor = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()

running = True

MAZE_SIZE = (12,12)
CELL_SIZE = 40

m = Maze(MAZE_SIZE)


bx, by  = (100,100)

while running:
    screen.fill(bgcolor)
    
    
    for x in range(MAZE_SIZE[0]):
        for y in range(MAZE_SIZE[1]):
            if not (x-1, y, x, y) in m.doors and not (x+y==0):
                pygame.draw.line(screen, white, (bx+x*CELL_SIZE, by+y*CELL_SIZE),(bx+x*CELL_SIZE, by+(y+1)*CELL_SIZE))   

            if not (x,y,x+1,y) in m.doors:
                pygame.draw.line(screen, white, (bx+(x+1)*CELL_SIZE, by+y*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y+1)*CELL_SIZE))   
                
            if not (x,y-1,x,y) in m.doors:
                pygame.draw.line(screen, white, (bx+(x)*CELL_SIZE, by+y*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y)*CELL_SIZE))   
                
            
            if not (x,y,x,y+1) in m.doors and not (x+y==MAZE_SIZE[0]+MAZE_SIZE[1]-2):
                pygame.draw.line(screen, white, (bx+(x)*CELL_SIZE, by+(y+1)*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y+1)*CELL_SIZE))   
                

    pygame.display.update()
    clock.tick(60)