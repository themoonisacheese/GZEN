import pygame
from wall import Wall
from spike import Spike
from coin import Coin
from bat import Bat
from slime import Slime
from slime2 import Slime2
from slime3 import Slime3
from slime4 import Slime4
from slime5 import Slime5
from bat2 import Bat2
from bat3 import Bat3
from bat4 import Bat4
from bat5 import Bat5
from backwall import BackWall
from slime import Slime
from spring import Spring
from spawnPoint import SpawnPoint
from antiGravButton import Button
from pnj import PNJ
from displayableElement import DisplayableElement
from table import Table

class Room(DisplayableElement):
    def __init__(self, roomnumber, floorNumber): #FIXME: les couleurs dans design niveaux ne sont pas homogenes.
        self.floorNumber = floorNumber
        if floorNumber ==1:#python doesn't have switch statements smh
            floordesignPath = 'design niveaux/lvl1.png'
        elif floorNumber == 2:
            floordesignPath = 'design niveaux/lvl2.png'
        elif floorNumber == 3:
            floordesignPath = 'design niveaux/lvl3.png'
        elif floorNumber == 4:
            floordesignPath = 'design niveaux/lvl4(antigrav).png'
        elif floorNumber == 5:
            floordesignPath = 'design niveaux/lvl5.png'

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
                    #enemy
                    if floordesign.get_at((x + (roomnumber*16), y+1)) == (0,0,0,255):
                        if floorNumber == 1:
                            self.roomBlocks.append(Slime((x, y)))
                        elif floorNumber == 2:
                            self.roomBlocks.append(Slime2((x,y)))
                        elif floorNumber == 3:
                            self.roomBlocks.append(Slime3((x,y)))
                        elif floorNumber == 4:
                            self.roomBlocks.append(Slime4((x,y)))
                        elif floorNumber == 5:
                            self.roomBlocks.append(Slime5((x,y)))
                    else:
                        # bat
                        if floorNumber == 1:
                            self.roomBlocks.append(Bat((x, y)))
                        elif floorNumber == 2:
                            self.roomBlocks.append(Bat2((x,y)))
                        elif floorNumber == 3:
                            self.roomBlocks.append(Bat3((x,y)))
                        elif floorNumber == 4:
                            self.roomBlocks.append(Bat4((x,y)))
                        elif floorNumber == 5:
                            self.roomBlocks.append(Bat5((x,y)))
                elif color == (23, 18, 198, 255):
                    #spring
                    self.roomBlocks.append(Spring((x,y)))
                elif color ==(215,223,1,255):
                    self.roomBlocks.append(SpawnPoint((x,y)))
                elif color ==(230,89,1, 255):
                    self.roomBlocks.append(Button((x,y)))
                elif color == (168, 7, 125, 255):
                    self.roomBlocks.append(PNJ((x,y)))
                elif color ==(9,199,254):
                    self.roomBlocks.append(Table((x,y)))

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
