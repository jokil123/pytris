import sys
import math
import time
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

import tetrisboardgui


class Game():

    def __init__(self):
        self.GameLogic = GameLogic(self)
        self.Board = Board(self)

        self.app = QApplication(sys.argv)
        self.form = Ui(self)
        self.form.show()
        self.app.exec_()





class Ui(QtWidgets.QMainWindow, tetrisboardgui.Ui_MainWindow):
    
    def __init__(self, parent):
        super(Ui, self).__init__()
        self.setupUi(self)

        self.parent = parent
        self.parent.Ui = self

        self.timerEvent()


    def timerEvent(self):
        self.parent.GameLogic.TimeStep()
        QtCore.QTimer.singleShot(self.parent.GameLogic.tickSpeed, self.timerEvent)


    def DisplayOnWindow(self, text):
        self.Output.setText(text)

    
    def keyPressEvent(self, event):
        keybinds = {
        "left": Qt.Key_A,
        "right": Qt.Key_D,
        "accelerate" : Qt.Key_Space,
        "shift" : Qt.Key_Shift,
        "pause" : Qt.Key_P,
        "rotateCCW" : Qt.Key_W,
        "rotateCW" : Qt.Key_S,
        }

        if event.key() == keybinds["left"]:
            self.parent.GameLogic.KeyPress("leftKey")
        if event.key() == keybinds["right"]:
            self.parent.GameLogic.KeyPress("rightKey")
        if event.key() == keybinds["accelerate"]:
            self.parent.GameLogic.KeyPress("accelerateKey")
        if event.key() == keybinds["shift"]:
            self.parent.GameLogic.KeyPress("shiftKey")
        if event.key() == keybinds["pause"]:
            self.parent.GameLogic.KeyPress("pauseKey")
        if event.key() == keybinds["rotateCCW"]:
            self.parent.GameLogic.KeyPress("rotateCCWKey")
        if event.key() == keybinds["rotateCW"]:
            self.parent.GameLogic.KeyPress("rotateCWKey")





class GameLogic():

    def __init__(self, parent):
        self.parent = parent
        self.score = 0
        self.tickSpeed = 1000
        self.shapes = (
            ((0, 0),(0, 1),(0, 2),(0, -1)), # Line
            ((0, 0),(0, 1),(1, 0),(1, 1)),  # Square
            ((0, 0),(0, -1),(1, 0),(-1, 0)),   # T-piece
            ((0, 0),(0, 1),(0, -1),(1, -1)),   # L-piece
            ((0, 0),(0, 1),(0, -1),(1, 1)),   # J-piece
            ((0, 0),(0, 1),(0, -1),(1, 1)),   # Z-piece
            ((0, 0),(0, 1),(-1, 0),(1, 1)),   # S-piece
        )


    def TimeStep(self):
        for i in self.parent.Board.TetrominoeList:
            if i.isMovable:
                i.isMovable = i.MovePiece(0, 1)
            else:
                i.set_isMovable(False)

        if not self.parent.Board.ActivePieceExists():
            self.parent.Board.SpawnPiece()

        self.parent.Ui.DisplayOnWindow(self.parent.Board.GenerateDisplayString())       


    def Gameover(self):
        pass


    def UpdateScore(self):
        pass


    def Pause(self):
        pass


    def PieceRandomizer(self):
        Piece = random.randint(0, len(self.shapes) - 1)

        return Piece


    def KeyPress(self, key):
        if key == "leftKey":
            print("left is pressed")    # Debug
            for i in self.parent.Board.TetrominoeList:
                if i.isMovable:
                    i.MovePiece(-1, 0)

        elif key == "rightKey":
            for i in self.parent.Board.TetrominoeList:
                if i.isMovable:
                    i.MovePiece(1, 0)

        elif key == "accelerateKey":    # Debug
            print("accelerate is pressed")
            for i in self.parent.Board.TetrominoeList:
                if i.isMovable:
                    i.MovePiece(0, 1)
                    print("piece was accelerated")  # Debug
                    

        elif key == "shiftKey":
            k = 0
            for i in self.parent.Board.TetrominoeList:
                j = 0
                if i.isMovable:
                    while i.CanMove(i.px, i.py + 1):
                        i.MovePiece(0, 1)
                        
                        if j > self.parent.Board.boardHeight + 1:
                            print("an exception occured in shiftKey")   # Debug
                            self.parent.Board.DeletePiece(j)
                            continue
                    else:
                        i.set_isMovable(False)
            else:
                if not self.parent.Board.ActivePieceExists():
                    self.parent.Board.SpawnPiece()
                j += 1
            k += 1

        elif key == "pauseKey":
            self.Pause()

        elif key == "rotateCCWKey":
            for i in self.parent.Board.TetrominoeList:
                if i.isMovable:
                    i.RotatePiece(-90)
                
        elif key == "rotateCWKey":
            for i in self.parent.Board.TetrominoeList:
                if i.isMovable:
                    i.RotatePiece(90)

        self.parent.Ui.DisplayOnWindow(self.parent.Board.GenerateDisplayString()) 





class Board():

    def __init__(self, parent):
        self.parent = parent
        self.TetrominoeList = []
        self.matrix = []
        self.boardWidth = 10
        self.boardHeight = 29

    
    def CreateEmptyMatrix(self):
        returnboard = []
        for i in range(0, self.boardHeight):
            returnboard.append([])
            for j in range(0, self.boardWidth):
                returnboard[i].append(0)
        return returnboard


    def UpdateMatrix(self):
        # print("Matrix Update")  	# Debug
        self.matrix = test = self.CreateEmptyMatrix()

        for i in Point._registry:
            i.AddPoint()
            # print("Point Added")    # Debug


    def GenerateDisplayString(self):
        self.UpdateMatrix()

        displayString = ""

        for i in self.matrix:
            for j in i:
                if j == 0:
                    displayString += "░░"
                elif j == 1:
                    displayString += "██"
                else:
                    displayString += "▓▓"
                displayString += " "
            displayString += "\n"

        return displayString


    def DeletePiece(self, index):
        piece = self.TetrominoeList[index]

        for k in piece.points:
            Point._registry.remove(k)

        piece.points.clear()

        del piece
        del self.TetrominoeList[index]
        del k


    def DeletePoint(self, index):
        if index == None: return

        point = Point._registry[index]

        j = 0
        for i in self.TetrominoeList:
            try:
                i.points.remove(point)
                if i.points == []:
                    self.DeletePiece(j)
            except:
                pass
            j += 1

        del point
        del Point._registry[index]
        del i


    def PosToPointIndex(self, gx, gy):
        i = 0
        for x in Point._registry:
            if (gx, gy) == x.get_GlobalPos():
                return i
            i += 1
        else:
            return None

    
    def CheckFullLines(self):
        self.UpdateMatrix()

        returnIndices = []

        j = 0
        for i in self.matrix:
            if sum(i) / len(i) == 1:
                returnIndices.append(j)
            j += 1

        return returnIndices


    def RemoveFullLines(self):
        ltr = self.CheckFullLines()  # Lines to remove

        if len(ltr) == 0:
            return 0

        for y in ltr:
            x = 0
            for k in self.matrix[y]:
                self.DeletePoint(self.PosToPointIndex(x, y))
                x += 1

        self.parent.Ui.DisplayOnWindow(self.GenerateDisplayString())
            
        for i in ltr:
            for j in Point._registry:
                gx, gy = j.get_GlobalPos()

                if gy < i:
                    j.ry += 1

        return len(ltr)

    
    def ActivePieceExists(self):
        for i in self.TetrominoeList:
            if i.isMovable:
                return True
        else:
            False


    def SpawnPiece(self):
        self.TetrominoeList.append(Tetrominoe(self, 4, 2, "red", self.parent.GameLogic.PieceRandomizer()))






class Tetrominoe(): 	# Piece


    def __init__(self, parent, px, py, color, shapeIndex):
        self.parent = parent
        self.px = px
        self.py = py
        self.color = color
        self.shape = shapeIndex
        self.isMovable = True
        self.points = []
        for i in self.parent.parent.GameLogic.shapes[shapeIndex]:
            self.points.append(Point(self, i))


    def IsInBounds(self):
        for i in self.points:
            bx, by = i.get_GlobalPos()
            if bx < 0 or bx >= self.parent.boardWidth:
                return False
            if by < 0 or by >= self.parent.boardHeight:
                return False
        else:
            return True


    def TestMatrix(self):
        for i in self.parent.matrix:
            for j in i:
                if j > 1:
                    return False
        else:
            return True


    def CanMove(self, newX, newY):
        answer = True

        oldx = self.px
        oldy = self.py

        self.px = newX
        self.py = newY


        if not self.IsInBounds():
            answer = False
        else:
            self.parent.UpdateMatrix()

            if not self.TestMatrix():
                answer = False


        self.px = oldx
        self.py = oldy
        self.parent.UpdateMatrix()


        if not answer:
            print("Unvalid Movement")   # Debug

        return answer

    
    def MovePiece(self, rx, ry):
        newX = self.px + rx
        newY = self.py + ry

        if self.CanMove(newX, newY):
            self.px = newX
            self.py = newY
            return True
        else:
            return False


    def CanRotate(self, angle):
        answer = True

        for i in self.points:
            i.RotatePoint(angle)

        if not self.IsInBounds():
            answer = False
        else:
            self.parent.UpdateMatrix()

            if not self.TestMatrix():
                answer = False


        for i in self.points:
                i.RotatePoint(angle * -1)
        self.parent.UpdateMatrix()


        if not answer:
            print("Unvalid Rotation")   # Debug

        return answer


    def RotatePiece(self, angle):
        if self.CanRotate(angle):
            for i in self.points:
                i.RotatePoint(angle)
            return True
        else:
            return False


    def set_isMovable(self, moveBool):
        if moveBool != self.isMovable:
            if not moveBool:
                self.parent.RemoveFullLines()
                print(len(self.parent.TetrominoeList))

                self.isMovable = False
            else:
                self.isMovable = True





class Point():  # Square
    _registry = []


    def __init__(self, parent, coord):
        self.parent = parent
        self._registry.append(self)
        self.rx, self.ry = coord


    def get_GlobalPos(self):
        x = self.parent.px + self.rx
        y = self.parent.py + self.ry
        self.gx = 0
        self.gy = 0

        return x, y


    def AddPoint(self):
        self.gx, self.gy = self.get_GlobalPos()
        try:
            self.parent.parent.matrix[self.gy][self.gx] += 1
        except:
            self.parent.parent.DeletePoint(self.parent.parent.PosToPointIndex(self.gx, self.gy))
            print("an exception occured")   # Debug


    def RotatePoint(self, angle):
        rad = math.radians(angle)

        px = self.rx
        py = self.ry

        qx = math.cos(rad) * px - math.sin(rad) * py
        qy = math.sin(rad) * px + math.cos(rad) * py

        self.rx = int(round(qx))
        self.ry = int(round(qy))





def Main():
    tetrisgame = Game()





if __name__ == '__main__':
    Main()