import os, random
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk

class MainWindow:
    gameTitle = "GUI GAME"
    windowWidth = 900
    windowHeigth = 800
    icons = []
    gameSize = 12  # ゲームのサイズ
    iconKind = gameSize * gameSize / 4  # 種類
    iconWidth = iconHeight =60
    classmap = []
    delta = 25
    isFirst = True
    isGameStart = False
    formerPoint = None
    EMPTY = -1
    NONE_LINK = 0
    STRAIGHT_LINK = 1
    ONE_CORNER_LINK = 2
    TWO_CORNER_LINK = 3

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(self.gameTitle)
        self.centerWindow(self.windowWidth, self.windowHeigth)
        self.root.minsize(460, 460)
        self.__addComponets()
        self.extractSmallIconList()
        self.root.mainloop()

    def __addComponets(self):
        self.menubar = tk.Menu(self.root, bg="lightgrey", fg="black")
        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(label="NEW", command=self.file_new)
        self.menubar.add_cascade(label="START", menu=self.file_menu)
        self.root.configure(menu=self.menubar)
        num=min(self.windowHeigth,self.windowWidth)-50
        self.canvas = tk.Canvas(self.root, bg='white', width=num, height=num)
        self.canvas.pack(side=tk.TOP, pady=5)
        self.canvas.bind('<Button-1>', self.clickCanvas)

    def centerWindow(self, width, height):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
        self.root.geometry(size)

    def file_new(self, event=None):
        self.iniMap()
        self.drawMap()
        self.isGameStart = True

    def clickCanvas(self, event):
        if self.isGameStart:
            point = self.getInnerPoint(Point(event.x, event.y))
            if point.isUserful() and not self.isEmptyInMap(point):
                if self.isFirst:
                    self.drawSelectedArea(point)
                    self.isFirst = False
                    self.formerPoint = point
                else:
                    if self.formerPoint.isEqual(point):
                        self.isFirst = True
                        self.canvas.delete("rectRedOne")
                    else:
                        linkType = self.getLinkType(self.formerPoint, point)
                        if linkType['type'] != self.NONE_LINK:
                            self.ClearLinkedBlocks(self.formerPoint, point)
                            self.canvas.delete("rectRedOne")
                            self.isFirst = True
                            if self.isGameEnd():
                                tk.messagebox.showinfo("You Win!")
                                self.isGameStart = False
                        else:
                            self.formerPoint = point
                            self.canvas.delete("rectRedOne")
                            self.drawSelectedArea(point)

    def isGameEnd(self):
        for y in range(0, self.gameSize):
            for x in range(0, self.gameSize):
                if self.classmap[y][x] != self.EMPTY:
                    return False
        return True

    def extractSmallIconList(self):
        PATH=os.path.dirname(os.path.abspath(__file__))
        root_dir = os.getcwd()
        imagePath = os.path.join(PATH, "pic", "colored.png")
        imageSouce = Image.open(imagePath)
        index = random.sample(range(1, 1079),int(self.iconKind))
        for img in index:
            region = imageSouce.crop((img%49 * 17, img//49*17,img%49 * 17+17, img//49*17+17))
            enlarged_region = region.resize((self.iconWidth, self.iconWidth), Image.Resampling.LANCZOS)
            self.icons.append(ImageTk.PhotoImage(enlarged_region))

    def iniMap(self):
        self.classmap = []
        tmpRecords = []
        records = []
        for i in range(0, int(self.iconKind)):
            for j in range(0, 4):
                tmpRecords.append(i)

        total = self.gameSize * self.gameSize
        for x in range(0, total):
            index = random.randint(0, total - x - 1)
            records.append(tmpRecords[index])
            del tmpRecords[index]

        for y in range(0, self.gameSize):
            for x in range(0, self.gameSize):
                if x == 0:
                    self.classmap.append([])
                self.classmap[y].append(records[x + y * self.gameSize])

    def drawMap(self):
        self.canvas.delete("all")
        for y in range(0, self.gameSize):
            for x in range(0, self.gameSize):
                point = self.getOuterLeftTopPoint(Point(x, y))
                im = self.canvas.create_image((point.x, point.y),
                                            image=self.icons[self.classmap[y][x]],
                                            anchor='nw', tags='im%d%d' % (x, y))

    def getOuterLeftTopPoint(self, point):
        return Point(self.getX(point.x), self.getY(point.y))

    def getOuterCenterPoint(self, point):
        return Point(self.getX(point.x) + int(self.iconWidth / 2),
                    self.getY(point.y) + int(self.iconHeight / 2))

    def getX(self, x):
        return x * self.iconWidth + self.delta

    def getY(self, y):
        return y * self.iconHeight + self.delta

    def getInnerPoint(self, point):
        x = -1
        y = -1

        for i in range(0, self.gameSize):
            x1 = self.getX(i)
            x2 = self.getX(i + 1)
            if point.x >= x1 and point.x < x2:
                x = i

        for j in range(0, self.gameSize):
            j1 = self.getY(j)
            j2 = self.getY(j + 1)
            if point.y >= j1 and point.y < j2:
                y = j

        return Point(x, y)

    def drawSelectedArea(self, point):
        pointLT = self.getOuterLeftTopPoint(point)
        pointRB = self.getOuterLeftTopPoint(Point(point.x + 1, point.y + 1))
        self.canvas.create_rectangle(pointLT.x, pointLT.y,
                                    pointRB.x - 1, pointRB.y - 1,
                                    outline='red', tags="rectRedOne")

    def ClearLinkedBlocks(self, p1, p2):
        self.classmap[p1.y][p1.x] = self.EMPTY
        self.classmap[p2.y][p2.x] = self.EMPTY
        self.canvas.delete('im%d%d' % (p1.x, p1.y))
        self.canvas.delete('im%d%d' % (p2.x, p2.y))

    def isEmptyInMap(self, point):
        if self.classmap[point.y][point.x] == self.EMPTY:
            return True
        else:
            return False

    def getLinkType(self, p1, p2):
        if self.classmap[p1.y][p1.x] != self.classmap[p2.y][p2.x]:
            return {'type': self.NONE_LINK}

        if self.isStraightLink(p1, p2):
            return {'type': self.STRAIGHT_LINK}
        
        res = self.isOneCornerLink(p1, p2)
        if res:
            return {
                'type': self.ONE_CORNER_LINK,
                'p1': res
            }
        
        res = self.isTwoCornerLink(p1, p2)
        if res:
            return {
                'type': self.TWO_CORNER_LINK,
                'p1': res['p1'],
                'p2': res['p2']
            }
        
        return {'type': self.NONE_LINK}

    def isStraightLink(self, p1, p2):
        start = -1
        end = -1
        if p1.y == p2.y:
            if p2.x < p1.x:
                start = p2.x
                end = p1.x
            else:
                start = p1.x
                end = p2.x
            for x in range(start + 1, end):
                if self.classmap[p1.y][x] != self.EMPTY:
                    return False
            return True
        elif p1.x == p2.x:
            if p1.y > p2.y:
                start = p2.y
                end = p1.y
            else:
                start = p1.y
                end = p2.y
            for y in range(start + 1, end):
                if self.classmap[y][p1.x] != self.EMPTY:
                    return False
            return True
        return False

    def isOneCornerLink(self, p1, p2):
        pointCorner = Point(p1.x, p2.y)
        if self.isStraightLink(p1, pointCorner) and self.isStraightLink(pointCorner, p2) and self.isEmptyInMap(pointCorner):
            return pointCorner
        pointCorner = Point(p2.x, p1.y)
        if self.isStraightLink(p1, pointCorner) and self.isStraightLink(pointCorner, p2) and self.isEmptyInMap(pointCorner):
            return pointCorner
        return None

    def isTwoCornerLink(self, p1, p2):
        for y in range(-1, self.gameSize + 1):
            pointCorner1 = Point(p1.x, y)
            pointCorner2 = Point(p2.x, y)
            if y == p1.y or y == p2.y:
                continue
            if y == -1 or y == self.gameSize:
                if self.isStraightLink(p1, pointCorner1) and self.isStraightLink(pointCorner2, p2):
                    return {'p1': pointCorner1, 'p2': pointCorner2}
            else:
                if self.isStraightLink(p1, pointCorner1) and self.isStraightLink(pointCorner1, pointCorner2) and self.isStraightLink(pointCorner2, p2) and self.isEmptyInMap(pointCorner1) and self.isEmptyInMap(pointCorner2):
                    return {'p1': pointCorner1, 'p2': pointCorner2}
        for x in range(-1, self.gameSize + 1):
            pointCorner1 = Point(x, p1.y)
            pointCorner2 = Point(x, p2.y)
            if x == p1.x or x == p2.x:
                continue
            if x == -1 or x == self.gameSize:
                if self.isStraightLink(p1, pointCorner1) and self.isStraightLink(pointCorner2, p2):
                    return {'p1': pointCorner1, 'p2': pointCorner2}
            else:
                if self.isStraightLink(p1, pointCorner1) and self.isStraightLink(pointCorner1, pointCorner2) and self.isStraightLink(pointCorner2, p2) and self.isEmptyInMap(pointCorner1) and self.isEmptyInMap(pointCorner2):
                    return {'p1': pointCorner1, 'p2': pointCorner2}
        return None

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def isUserful(self):
        if self.x >= 0 and self.y >= 0:
            return True
        else:
            return False

    def isEqual(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False

    def clone(self):
        return Point(self.x, self.y)

    def changeTo(self, point):
        self.x = point.x
        self.y = point.y

MainWindow()