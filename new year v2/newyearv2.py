import pygame,math
from random import*
from fireworks import Firework
from data import *
from clas import *



def update(screen:pygame.Surface,fireworks,trails)->None:
    if True:
        for t in trails:
            t.show(screen)
            if t.decay():
                trails.remove(t)

    for fw in fireworks:
        fw.update(screen)
        if fw.remove():
            fireworks.remove(fw)
    pygame.display.update()


def main():
    #colors
    BLUE=[0,0,33]

    #init
    pygame.init()
    #screen size
    SIZE=[screen_size_x,screen_size_y]
    screen=pygame.display.set_mode(size=SIZE)
    pygame.display.set_caption("Happy New Year")

    clock=pygame.time.Clock()
    fireworks=[Firework() for i in range(1)] #first firework
    


    #work until close
    done=False
    while not done:
        

        for event in pygame.event.get():   # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True   # Flag that we are done so we exit this loop


        # Clear screen every tick
        screen.fill(BLUE)
        # Floor is beneath tree's but above background snow.
        pygame.draw.rect(screen, (240, 240, 240), [0, SIZE[1]-60, SIZE[0], 60])

        fontObj = pygame.font.SysFont(pygame.font.get_default_font(), 100, True, True)
        text = fontObj.render('Happy New Year', True, (randint(0,255),randint(0,255),randint(0,255)), None)
        screen.blit(text, [70, int(SIZE[1]/2)-100])


        # Go ahead and update the screen with what we've drawn.
        # pygame.display.update()

        if randint(0, 40) == 1:  # create new firework
            fireworks.append(Firework())
        clock.tick(80)
        update(screen,fireworks,trails)
        

    pygame.quit()
    quit()

if __name__=="__main__":
    main()