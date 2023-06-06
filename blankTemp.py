from os import name
import pygame as pg 
import random 
pg.init()
width = 500
height = 500

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Title of window')
clock = pg.time.Clock() 
running  = True

points = []

while running : 
    screen.fill((255,255,255))
    if pg.mouse.get_pressed()[0] : 
        mx,my = pg.mouse.get_pos()
        points.append((mx,my))
    if len(points) > 1 : 
        for i in range(len(points)-1) : 
            point1 = points[i]
            point2 = points[i+1]
            pg.draw.line(screen , (0,0,0) , point1 , point2 , 5)
            
    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
    pg.display.flip()
    clock.tick(60)
pg.quit()
