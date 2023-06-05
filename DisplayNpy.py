import pygame as pg 
import numpy as np 


pg.init()
width = 560
height = 560

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Doodles!')
clock = pg.time.Clock() 
running  = True

data = np.load('ML/doodle/data/npy/cat.npy')

num = 28
mySize = 56
size  = int(mySize/num )    



def draw(drawing , xPos , yPos) :  
    for row in range(num) :   
            for col in range(num) : 
                x = (col*size) + (xPos*mySize) 
                y = (row*size) + (yPos*mySize)
                color  = 255 - drawing[row*(num) + col]
                pg.draw.rect(screen , (color,color,color) , (x,y,size,size))


while running : 
    screen.fill((255,255,255))
    counter = 0
    for canvasRow in range(10) :
        for canvasCol in range(10) :  
            draw(data[counter],canvasCol , canvasRow)
            x ,y = canvasCol*mySize , canvasRow*mySize
            # pg.draw.polygon(screen, (0,0,0), ((x,y),(x+mySize,y),(x+mySize,y+mySize),(x,y+mySize)), 1)
            counter+= 1


    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
    pg.display.flip()
    clock.tick(60)
pg.quit()
