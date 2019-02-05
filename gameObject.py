from displayableElement import DisplayableElement


class GameObject(DisplayableElement):
    def __init__(self, position, animationFrames, animationFrameRate=3):
        DisplayableElement.__init__(self, animationFrames, animationFrameRate)
        self.moveto(position)
        self.display = False

    def instantiate(self):
        self.display = True

    def destroy(self):  # NB: ne detruit pas l'object python.
        self.display = False
        self.animationFrames = []
        self.animationFrameRate = 0
        self.currentTexture = None
