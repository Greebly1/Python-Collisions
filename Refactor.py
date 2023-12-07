import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000
FPSCAP = 120
BACKGROUNDCOLOR = "burlywood1"

window = pygame.display.set_mode((WIDTH, HEIGHT))

playing = True
clock = pygame.time.Clock()

class circleSprite:
    circles = []

    def __init__(self, initColor, initLoc : pygame.math.Vector2, initRad):
        circleSprite.circles.append(self)
        self.color = initColor
        self.location = initLoc
        self.radius = initRad
        self.ID = len(circleSprite.circles)
        self.name = "circle{}".format(self.ID)
        print("Created", self)

    def __del__(self):
        if(circleSprite.isInList(self)):
            circleSprite.circles.remove(self)
        print("Deleted", self)

    def __str__(self):
        return self.name
    
    def destroy(self):
        if(circleSprite.isInList(self)):
            circleSprite.circles.remove(self)
        del self

    def drawCircles():
        for object in circleSprite.circles:
            pygame.draw.circle(window, object.color, object.location, object.radius)

    def isInList(object):
        if object in circleSprite.circles:
            return True
        return False

#returns true if object1 and object2 are colliding
def isColliding(object1 : circleSprite, object2 : circleSprite):
    #calculate the distance between two gameobjects
    #return true if the distance between two objects is less than or equal to the sum of their radii
    objectDistance = (object1.location - object2.location).length()
        #create a new vector that points from object 1, to object 2
        #get the length or magnitude of that vector
    
    colissionDistance = object1.radius + object2.radius 

    if(objectDistance > colissionDistance):
        return False
    print(object1, "is colliding with", object2)
    return True

class input:
    #checkInput for each pygame event
    #This is executed at the start of each frame
    def handleInputQueue():
        for event in pygame.event.get():
            input.checkInput(event)

    #find if an event is a valid input, if it is execute the correct handleInput function
    def checkInput(event : pygame.event.Event):
        match event.type:
            case pygame.QUIT:
                input.handleQuit()

    #quits game by assigning False to _playing
    def handleQuit():
        global playing
        playing = False

CIRCLENUM = 5
for circle in range(CIRCLENUM):
    newCircle = circleSprite('black', pygame.Vector2(circle*100, circle*100), 30)

newestCircle = circleSprite('black', pygame.Vector2(700, 700), 50)

newestCircle.destroy()

del newestCircle

print("-----STARTING GAME LOOP-----")
while playing:
    clock.tick(FPSCAP)
    window.fill(BACKGROUNDCOLOR)

    input.handleInputQueue()

    

    circleSprite.drawCircles()
    pygame.display.flip()
print("-----ENDING GAME LOOP-----")
pygame.quit()