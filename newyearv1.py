import pygame
import random

class Fireworks():
    def __init__(self,bounds,pygame,screen):
        self.fireworks=[]
        self.speed=3
        self.size=1
        self.nr=200
        for i in range(self.nr+10):
            self.fireworks.append([0,0,(0,0,0)])
        # for i in range(500):
        #     x = random.randrange(bounds[0]*-1, bounds[0]*2, 1)
        #     y = random.randrange(bounds[1]-50, bounds[1], 1)
        #     self.fireworks.append([x, y,(random.randint(0,255),random.randint(0,255),random.randint(0,255))])

        self.screen = screen
        self.pygame = pygame
        self.bounds = bounds
        self.count = 0
    
    def tick(self):
        self.count+=1
        x = random.randrange(self.bounds[0]*-1, self.bounds[0]*2, 1)
        y = random.randrange(self.bounds[1]-50, self.bounds[1], 1)
        self.fireworks[self.count]=([x, y,(random.randint(0,255),random.randint(0,255),random.randint(0,255))])

        for i in range(len(self.fireworks)):
            self.pygame.draw.line( 
                self.screen, 
                color=self.fireworks[i][2], 
                start_pos=[self.fireworks[i][0],self.fireworks[i][1]], 
                end_pos=[self.fireworks[i][0],self.fireworks[i][1]+10], 
                width=2)
            
            if self.count % self.speed == 0:
                self.fireworks[i][1] -= 10

            if ( self.fireworks[i][1] > self.bounds[1]*2 or 
                    self.fireworks[i][0] < self.bounds[0]*-1 or 
                    self.fireworks[i][0] > self.bounds[0]*2 ):
                y = random.randrange(self.bounds[1]*-1, 0)
                self.fireworks[i][1] = y
                
                x = random.randrange(self.bounds[0]*-1, self.bounds[0]*2)
                self.fireworks[i][1] = y

            if self.count > self.nr:
                self.count -= self.nr
            
        
def main():
    #colors
    BLUE=[0,0,33]

    #init
    pygame.init()
    #screen size
    SIZE=[800,600]
    screen=pygame.display.set_mode(size=SIZE)
    pygame.display.set_caption("Happy New Year")

    #make firework
    fw1=Fireworks(SIZE,pygame,screen)

    clock=pygame.time.Clock()
    


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
        text = fontObj.render('Happy New Year', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), None)
        screen.blit(text, [70, int(SIZE[1]/2)-100])

        #Let's fireworks go up
        fw1.tick()
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

if __name__=="__main__":
    main()
