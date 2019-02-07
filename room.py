import pygame
from wall import Wall
from spike import Spike
from coin import Coin
from bat import Bat
from slime import Slime
from backwall import BackWall
from displayableElement import DisplayableElement

class Room(DisplayableElement):
    def __init__(self, floordesignPath, roomnumber, floorNumber): #FIXME: les couleurs dans design niveaux ne sont pas homogenes.
        floordesign = pygame.image.load(floordesignPath)
        self.roomnumber=roomnumber
        self.roomBlocks=[]
        for y in range(9):
            for x in range(16):
                color = floordesign.get_at((x + (roomnumber*16), y))
#                print("x = " + str(x+ (roomnumber*16)) + "; y = " + str(y) + "; color = " + str(color))
                if color == (0,0,0,255):  # wall
                    self.roomBlocks.append(Wall((x, y)))
                elif color == (88,88,88,255):  # spike
                    if floordesign.get_at((x + (roomnumber*16), y+1)) == (0, 0, 0, 255):
                        self.roomBlocks.append(Spike((x, y)))
                    elif floordesign.get_at((x + (roomnumber*16) +1, y)) == (0, 0, 0, 255):
                        self.roomBlocks.append(Spike((x, y), 1))
                    elif floordesign.get_at((x + (roomnumber*16) -1, y)) == (0, 0, 0, 255):
                        self.roomBlocks.append(Spike((x, y), 3))
                    elif floordesign.get_at((x + (roomnumber*16) , y-1)) == (0, 0, 0, 255):
                        self.roomBlocks.append(Spike((x, y), 2))
                    else:
                        self.roomBlocks.append(Spike((x, y)))
                elif color == (18, 189, 99, 255):
                    self.roomBlocks.append(Coin((x, y)))
                elif color == (189, 18, 18, 255):
                    # enemy
                    if floordesign.get_at((x + (roomnumber*16), y+1)) == (0, 0, 0, 255):
                        # slime
                        pass
                    else:
                        # bat
                        self.roomBlocks.append(Bat((x, y)))



    def draw(self, screen):
        if self.display:
            for block in self.roomBlocks:
                block.draw(screen)

    def moveto(self,pos):
        raise AssertionError('cannot use moveto() on a room!')

    def move(self, movement):
        for block in self.roomBlocks:
            block.move(movement)

    def animate(self, clocktick):
        if self.display:
            for block in self.roomBlocks:
                block.animate(clocktick)
    def update(self, ticktime, objlist):
        for obj in self.roomBlocks:
            obj.update(ticktime, objlist)

    def changeAnimation(self, newAnimation, animationFrameRate):
        raise AssertionError('cannot change animation on a room!')

    def show(self, show):
        self.display = show
        for block in self.roomBlocks:
            block.display = show
