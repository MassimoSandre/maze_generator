import pygame
from pygame.locals import *
import random
from maze import Maze
from maze_solver import Maze_Solver

size = width, height = 800, 800

bgcolor = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()

font = pygame.font.SysFont('arial', 20)

running = True

MAZE_SIZE = (10,10)
CELL_SIZE = 40

m = Maze(MAZE_SIZE)
solver = Maze_Solver(m)
sol = solver.get_solution()

bx, by  = (100,100)

print(sol)

while running:
    screen.fill(bgcolor)
    
    
    for x in range(MAZE_SIZE[0]):
        for y in range(MAZE_SIZE[1]):
            if not (x-1, y, x, y) in m.doors and not (x+y==0):
                pygame.draw.line(screen, white, (bx+x*CELL_SIZE, by+y*CELL_SIZE),(bx+x*CELL_SIZE, by+(y+1)*CELL_SIZE))   
            else:
                if (x-1, y) in sol and (x,y) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE - CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2),(bx+x*CELL_SIZE + CELL_SIZE//2,by+y*CELL_SIZE + CELL_SIZE//2))   

            if not (x,y,x+1,y) in m.doors:
                pygame.draw.line(screen, white, (bx+(x+1)*CELL_SIZE, by+y*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y+1)*CELL_SIZE))   
            else:
                if (x, y) in sol and (x+1,y) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2),(bx+x*CELL_SIZE + 3*(CELL_SIZE//2),by+y*CELL_SIZE + CELL_SIZE//2))   
                
            if not (x,y-1,x,y) in m.doors:
                pygame.draw.line(screen, white, (bx+(x)*CELL_SIZE, by+y*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y)*CELL_SIZE))   
            else:
                if (x, y-1) in sol and (x,y) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE - CELL_SIZE//2),(bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2))   
                
            if not (x,y,x,y+1) in m.doors and not (x+y==MAZE_SIZE[0]+MAZE_SIZE[1]-2):
                pygame.draw.line(screen, white, (bx+(x)*CELL_SIZE, by+(y+1)*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y+1)*CELL_SIZE))   
            else:
                if (x, y) in sol and (x,y+1) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2),(bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + 3*(CELL_SIZE//2)))   

            


    pygame.display.update()
    clock.tick(60)