import map
from tkinter import *
from PIL import Image, ImageTk


class Drawing():

    def __init__(self):
        self.gameBoard = map.mapLevel1

        self.root = Tk()
        self.canvas = Canvas(self.root, width=960, height=795, bg='white')
        self.canvas.pack()

        floorImg = Image.open("images/floor.png")
        wallImg = Image.open("images/wall.png")
        heroDownImg = Image.open("images/hero-down.png")
        heroUpImg = Image.open("images/hero-up.png")
        heroLeftImg = Image.open("images/hero-left.png")
        heroRightImg = Image.open("images/hero-right.png")
        skeletonImg = Image.open("images/skeleton.png")
        bossImg = Image.open("images/boss.png")
        heroProfile = Image.open("images/hero_profile.jpeg")

        self.floorImg = ImageTk.PhotoImage(floorImg)
        self.wallImg = ImageTk.PhotoImage(wallImg)
        self.heroDownImg = ImageTk.PhotoImage(heroDownImg)
        self.heroUpImg = ImageTk.PhotoImage(heroUpImg)
        self.heroLeftImg = ImageTk.PhotoImage(heroLeftImg)
        self.heroRightImg = ImageTk.PhotoImage(heroRightImg)
        self.skeletonImg = ImageTk.PhotoImage(skeletonImg)
        self.bossImg = ImageTk.PhotoImage(bossImg)
        self.heroProfile = ImageTk.PhotoImage(heroProfile)

    def map(self):
        self.canvas.delete('all')

        for i in range(11):
            for j in range(10):
                if self.gameBoard[i][j] == 'w':
                    self.canvas.create_image(j*72, i*72, anchor=NW, image=self.wallImg)
                else:
                    self.canvas.create_image(j*72, i*72, anchor=NW, image=self.floorImg)

    def skeleton(self, skeleton):
        self.canvas.create_image(skeleton.posX*72, skeleton.posY*72, anchor=NW, image=self.skeletonImg)

    def boss(self, boss):
        self.canvas.create_image(boss.posX*72, boss.posY*72, anchor=NW, image=self.bossImg)

    def hero(self, hero):
        if hero.direction == 'Up':
            self.canvas.create_image(hero.posX*72, hero.posY*72, anchor=NW, image=self.heroUpImg)
        if hero.direction == 'Down':
            self.canvas.create_image(hero.posX*72, hero.posY*72, anchor=NW, image=self.heroDownImg)
        if hero.direction == 'Left':
            self.canvas.create_image(hero.posX*72, hero.posY*72, anchor=NW, image=self.heroLeftImg)
        if hero.direction == 'Right':
            self.canvas.create_image(hero.posX*72, hero.posY*72, anchor=NW, image=self.heroRightImg)

    def infoScreen(self):
        self.canvas.create_image(730, 25, anchor=NW, image=self.heroProfile)

    def mainloop(self):
        self.canvas.mainloop()