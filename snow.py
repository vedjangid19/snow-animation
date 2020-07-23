import pygame, random

pygame.init()

blue = (135,206,250)
white = (255,255,255)
black = (0,0,0)

gravity = 5
fps = 60
width = 800
height = 500
snowsize = 3
snownumber = 300

varheight = height
snowcolor = white
bgcolor = blue

gameover = False

display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snow")

snowflake = []

for q in range(snownumber):
    x = random.randint(-300,width) 
    y = random.randint(0,varheight)
    snowflake.append([x,y])

clock = pygame.time.Clock()
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
    display.fill(bgcolor)
    for i in snowflake:
        i[0] += 2
        i[1] += gravity

        pygame.draw.circle(display,snowcolor,i,snowsize)

        if i[1] > varheight:
            i[1] = random.randrange(-150,-5) 
            i[0] = random.randrange(-200,width) 

    pygame.display.flip()

    clock.tick(fps)





















