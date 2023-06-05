import pygame as pg 
import numpy as np 
import readWriteData as rw

pg.init()
width = 840
height = 840

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Doodles!')
clock = pg.time.Clock() 
running  = True

data = rw.readData('cat1000')
num = 28
mySize = int(width/10)
size  = int(mySize/num )    
gridNum = int(width/mySize)

def drawall(data , counter):
    eleNum = 784
    canvasCol = counter%gridNum
    canvasRow = int(counter/gridNum)
    for row in range(num) : 
        for col in range(num) : 
            x = (col * size) + (canvasCol*mySize)
            y = (row * size) + (canvasRow*mySize)
            index = row*num + col + (counter*eleNum)
            color = 255-data[index]
            pg.draw.rect(screen , (color,color,color) , (x,y,size,size))

while running : 
    screen.fill((255,255,255))
    for i in range(100) : 
        drawall(data , i)
    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
    pg.display.flip()
    clock.tick(60)
pg.quit()
