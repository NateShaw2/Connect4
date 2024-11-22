# Final Project
# Nate Shaw
# November 18, 2021

from random import choice
from tkinter import *

class Connect4:
     
    def __init__(self, width, height, window=None):
        self.width = width
        self.height = height
        self.data = []
        self.clear()
        self.lastCheckerLocation = {'row': None, 'column': None}
     
    def __repr__(self):
        s = ''
        numberedColumns = []
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'  
        s += '--' * self.width + '-\n' 
        for col in range(self.width):
            numberedColumns += [str(col)]
            while len(str(self.width)) > len(numberedColumns[col]):
                numberedColumns[col] += ' '
        while len(numberedColumns[-1]) > 0:
            for i in range(len(numberedColumns)):
                if numberedColumns[i][0] == ' ':
                    s += '  '
                else:
                    s += ' ' + numberedColumns[i][0]
                numberedColumns[i] = numberedColumns[i][1:]
            s += '\n'
        return s  

    def addMove(self, col, ox):
        if not self.allowsMove(col):
            return
        row = -1
        while True:
            if self.data[row][col] == ' ':
                break
            row += -1
        self.data[row][col] = ox
        self.lastCheckerLocation['row'] = row
        self.lastCheckerLocation['column'] = col

    def clear(self):
        self.data = []
        self.lastCheckerLocation = {'row': None, 'column': None}
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' '] 
            self.data += [boardRow]

    def delMove(self, col):
        if col not in range(self.width):
            return
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                break

    def allowsMove(self, col):
        if col not in range(self.width):
            return False
        elif self.data[0][col] != ' ': 
            return False
        else:
            return True

    def isFull(self):
        for col in range(self.width):
            if self.allowsMove(col):
                return False
        return True

    def winsFor(self, ox):
        for shift in range(4):
            if self.lastCheckerLocation['column'] - 3 + shift  < 0 or\
            self.lastCheckerLocation['column'] + shift  > self.width - 1 or\
            self.lastCheckerLocation['row'] + shift  > -1 or\
            self.lastCheckerLocation['row'] - 3 + shift  < -1 * self.height:
                pass
            elif self.data[self.lastCheckerLocation['row'] - 3 + shift]\
            [self.lastCheckerLocation['column'] - 3 + shift] == ox and\
            self.data[self.lastCheckerLocation['row'] - 2 + shift]\
            [self.lastCheckerLocation['column'] - 2 + shift] == ox and\
            self.data[self.lastCheckerLocation['row'] - 1 + shift]\
            [self.lastCheckerLocation['column'] - 1 + shift] == ox and\
            self.data[self.lastCheckerLocation['row'] + shift]\
            [self.lastCheckerLocation['column'] + shift] == ox:
                return True

            if self.lastCheckerLocation['column'] - 3 + shift < 0 or\
            self.lastCheckerLocation['column'] + shift > self.width - 1 or\
            self.lastCheckerLocation['row'] + 3 - shift > -1 or\
            self.lastCheckerLocation['row'] - shift < -1 * self.height:
                pass
            elif self.data[self.lastCheckerLocation['row'] + 3 - shift]\
            [self.lastCheckerLocation['column'] - 3 + shift] == ox and\
            self.data[self.lastCheckerLocation['row'] + 2 - shift]\
            [self.lastCheckerLocation['column'] - 2 + shift] == ox and\
            self.data[self.lastCheckerLocation['row'] + 1 - shift]\
            [self.lastCheckerLocation['column'] - 1 + shift] == ox and\
            self.data[self.lastCheckerLocation['row'] - shift]\
            [self.lastCheckerLocation['column'] + shift] == ox:
                return True

            if self.lastCheckerLocation['column'] - 3 + shift < 0 or\
            self.lastCheckerLocation['column'] + shift > self.width - 1:
                pass
            elif self.data[self.lastCheckerLocation['row']]\
            [self.lastCheckerLocation['column'] - 3 + shift] == ox and\
            self.data[self.lastCheckerLocation['row']]\
            [self.lastCheckerLocation['column'] - 2 + shift] == ox and\
            self.data[self.lastCheckerLocation['row']]\
            [self.lastCheckerLocation['column'] - 1 + shift] == ox and\
            self.data[self.lastCheckerLocation['row']]\
            [self.lastCheckerLocation['column'] + shift] == ox:
                return True

        if self.lastCheckerLocation['row'] < -3:
            if self.data[self.lastCheckerLocation['row']]\
            [self.lastCheckerLocation['column']] == ox and\
            self.data[self.lastCheckerLocation['row'] + 1]\
            [self.lastCheckerLocation['column']] == ox and\
            self.data[self.lastCheckerLocation['row'] + 2]\
            [self.lastCheckerLocation['column']] == ox and\
            self.data[self.lastCheckerLocation['row'] + 3]\
            [self.lastCheckerLocation['column']] == ox:
                return True
        return False

    def hostGame(self):
        print('\nHello, welcome to Connect 4!')
        checkerType = 'o', 'x'
        checkerTypeIndex = 0
        while not self.isFull():
            print('\n' + str(self))
            print('It is ' + checkerType[checkerTypeIndex] + '\'s turn.')
            col = eval(input('Enter which column you want to place your \
checker: '))
            while self.allowsMove(col) == False:
                col = eval(input('Error: You can not place your checker \
there. Please enter which column you want to place your checker: '))
            self.addMove(col, checkerType[checkerTypeIndex])
            if self.winsFor(checkerType[checkerTypeIndex]):
                print('\n' + str(self))
                print(checkerType[checkerTypeIndex] + ' is the winner!')
                return
            checkerTypeIndex = abs(checkerTypeIndex) - 1       
        print('\n' + str(self))
        print('The game is a draw.')

    def playGameWith(self, aiPlayer):
        print('\nHello, welcome to Connect 4!')
        while not self.isFull():
            print('\n' + str(self))
            print('It is your turn.')
            col = eval(input('Enter which column you want to place your \
checker: '))
            while self.allowsMove(col) == False:
                col = eval(input('Error: You can not place your checker \
there. Please enter which column you want to place your checker: '))
            self.addMove(col, 'x')
            if self.winsFor('x'):
                print('\n' + str(self))
                print('You win!')
                return
            print('\n' + str(self))
            print('The AI is thinking...')
            oMove = aiPlayer.nextMove(self, aiPlayer.checker, aiPlayer.ply)
            self.addMove(oMove, 'o')
            if self.winsFor('o'):
                print('\n' + str(self))
                print('AI wins!')
                return
        print('\n' + str(self))
        print('The game is a draw.')

class Player:
    
    def __init__(self, ox, ply):
        self.checker = ox
        self.ply = ply

    def __repr__(self):
        return 'checker type: ' + self.checker +\
        '\nply level: ' + str(self.ply)

    def nextMove(self, board, ox, ply):
        scores = self.scoresFor(board, ox, ply)
        if ply == self.ply: 
            print(board)
            print(scores)
            print()
        maxScoreCol = []
        maxScore = max(scores['scoresList'])
        if maxScore == 100 or maxScore == -1:
            while True:
                if scores['scoresList'][-1] == maxScore:
                    return len(scores['scoresList']) - 1
                scores['scoresList'] = scores['scoresList'][:-1]
        elif maxScore == 50 and ply >= 4 and board.width >= 7:
            for i in range(3, board.width - 3):
                if scores['scoresList'][i] == 50:
                    maxScoreCol.append(i)
            if len(maxScoreCol) > 0:
                return choice(maxScoreCol)
        elif maxScore == 0:
            latestLose = max(scores['losingTurns'])
            latestLoseCol = []
            for i in range(len(scores['losingTurns'])):
                if scores['losingTurns'][i] == latestLose:
                    latestLoseCol.append(scores['loseColumns'][i])
            for col in latestLoseCol:
                scores['scoresList'][col] = 50
        for col in range(len(scores['scoresList'])):
            if scores['scoresList'][col] == 50:
                maxScoreCol.append(col)
        return choice(maxScoreCol)

    def scoresFor(self, board, ox, ply):      
        scores = {'scoresList': [], 'loseColumns': [], 'losingTurns': []}
        addedMoves = []
        for col in range(board.width):
            if not board.allowsMove(col):
                scores['scoresList'].append(-1)
                continue
            board.addMove(col, ox)
            if board.winsFor(ox):
                scores['scoresList'].append(100)
                board.delMove(col)
                return scores
            elif ply == 0 or ply == 1:
                scores['scoresList'].append(50)
                board.delMove(col)
                continue
            addedMoves.append(col)
            opponentChecker = self.opponentChecker(ox)
            for turn in range(2, ply + 1):
                nextMove = None
                if turn % 2 == 0:
                    nextMove = self.nextMove(board,
                    opponentChecker, ply + 1 - turn)
                    if not board.allowsMove(nextMove):
                        scores['scoresList'].append(50)
                        break
                    board.addMove(nextMove, opponentChecker)
                    addedMoves.append(nextMove)
                    if board.winsFor(opponentChecker):
                        scores['scoresList'].append(0)
                        scores['loseColumns'].append(col)
                        scores['losingTurns'].append(turn)
                        break
                else:
                    nextMove = self.nextMove(board, ox, ply + 1 -
                    turn)
                    if not board.allowsMove(nextMove):
                        scores['scoresList'].append(50)
                        break
                    board.addMove(nextMove, ox)
                    addedMoves.append(nextMove)
                    if board.winsFor(ox):
                        ply = turn
                        scores['scoresList'].append(100)
                        break
                if turn == ply:
                    scores['scoresList'].append(50)
            while len(addedMoves) > 0:
                    board.delMove(addedMoves[-1])
                    addedMoves = addedMoves[:-1]
        return scores

    def opponentChecker(self, ox):
        if ox == 'o':
            return 'x'
        return 'o'

class DemoScreen:

    def __init__(self, window):
        self.window = window
        self.frame = Frame(window)
        self.frame.grid(sticky = 'e')

        self.board = Connect4(7, 6)
        self.aiPlayer = Player('o', 6)
        self.userChecker = self.aiPlayer.opponentChecker\
        (self.aiPlayer.checker)

        if window.winfo_screenheight() > 480:
            self.canvasWidth = 480 + (window.winfo_screenheight() - 480) / 3
        else:
            self.canvasWidth = window.winfo_screenheight()
        if self.board.height > self.board.width:
            self.canvasWidth *= self.board.width / self.board.height
        self.canvasHeight = (self.board.height / self.board.width) *\
        self.canvasWidth
        self.size = self.board.width
        self.diameter = self.canvasWidth / self.size

        self.label = Label(self.frame, text = 'Hello, welcome to Connect 4!',
        font = 1, width = 42, relief = 'groove')
        self.labelShift = 0
        if self.canvasWidth > 480:
            self.labelShift = (self.canvasWidth - 480) / 10
        self.label.grid(padx = self.labelShift)

        self.newGame = Button(self.frame, text = 'New Game', width = 8)
        self.newGame.grid(row = 0, column = 1)
        self.newGame.bind('<Button-1>', self.setupGame)
        self.newGame.bind('<ButtonRelease-1>', self.disableButton)
        self.isButtonReleased = BooleanVar()

        self.quitButton = Button(self.frame, text = 'Quit!', width = 4,
        command = self.quitGame)
        if self.labelShift > 0:
            self.quitButton.grid(row = 0, column = 2, padx = 15)
        else:
            self.quitButton.grid(row = 0, column = 2)

        self.draw = Canvas(window, height = self.canvasHeight,
        width = self.canvasWidth)
        self.draw.create_polygon(0, 0, 0, self.canvasHeight,
        self.canvasWidth, self.canvasHeight, self.canvasWidth, 0,
        fill='yellow')
        self.draw.grid()

        self.circles = []
        self.emptyBoardDisplay()
        self.userCol = None
        self.didUserPickCol = BooleanVar()
        self.draw.bind('<Button-1>', self.mouseInput)
        self.draw.bind('<ButtonRelease-1>', self.buttonRelease)

    def mouseInput(self, event):
        col = int(event.x/self.diameter)
        self.userCol = col
        self.didUserPickCol.set(True)

    def buttonRelease(self, event):
        self.isButtonReleased.set(True)

    def disableButton(self, event):
        self.isButtonReleased.set(True)
        self.newGame.unbind('<Button-1>')
        self.newGame['state'] = DISABLED
        
    def emptyBoardDisplay(self):
        y = self.canvasWidth / (13 * self.size)
        for row in range(self.board.height):
            circleRow = []
            x = self.canvasWidth / (13 * self.size)
            for col in range(self.board.width):
                circleRow += [self.draw.create_oval(x, y,
                x + self.diameter * 0.85, y + self.diameter * 0.85,
                fill = 'white')]
                x += self.diameter
            self.circles += [circleRow]
            y += self.diameter
    
    def setupGame(self, event):
        self.isButtonReleased.set(False)
        self.board.clear()
        self.circles = []
        self.emptyBoardDisplay()
        nextChecker = choice(['o', 'x'])
        if nextChecker == self.aiPlayer.checker:   
            self.label['text'] = 'The AI is thinking...'
            self.window.wait_variable(self.isButtonReleased)
        self.displayGame(nextChecker)
        
    def displayGame(self, nextChecker, userError = False):
        if userError:
            self.label['text'] = 'That column is full,\
 choose a different column.'
            self.placeUserChecker(self.userChecker)
        elif self.board.isFull():
            self.label['text'] = 'The game is a draw.'
            self.newGame.bind('<Button-1>', self.setupGame)
            self.newGame['state'] = NORMAL
        elif self.userChecker == nextChecker:
            self.label['text'] = 'It\'s your turn,\
 click on a column to make your move.'
            self.placeUserChecker(self.userChecker)
        else:
            self.board.addMove(self.aiPlayer.nextMove(self.board,
            self.aiPlayer.checker, self.aiPlayer.ply),
            self.aiPlayer.checker)
            self.draw.itemconfig(self.circles[
            self.board.lastCheckerLocation['row']]\
            [self.board.lastCheckerLocation['column']],\
            fill = self.getColor(self.aiPlayer.checker))
            if self.board.winsFor(self.aiPlayer.checker):
                self.label['text'] = 'You Lose.'
                self.newGame.bind('<Button-1>', self.setupGame)
                self.newGame['state'] = NORMAL
            else:
                self.displayGame(self.userChecker)

    def placeUserChecker(self, ox):
        self.didUserPickCol.set(False)
        self.isButtonReleased.set(False)
        self.window.wait_variable(self.didUserPickCol)
        if not self.board.allowsMove(self.userCol):
            self.displayGame(self.userChecker, True)
        else:
            self.board.addMove(self.userCol, self.userChecker)
            self.draw.itemconfig(self.circles[self.board.lastCheckerLocation
            ['row']][self.userCol], fill = self.getColor(self.userChecker))
            if self.board.winsFor(self.userChecker):
                self.label['text'] = 'You Win!'
                self.newGame.bind('<Button-1>', self.setupGame)
                self.newGame['state'] = NORMAL
            else:
                self.label['text'] = 'The AI is thinking...'
                self.window.wait_variable(self.isButtonReleased)
                self.displayGame(self.aiPlayer.checker)

    def getColor(self, ox):
        if ox == 'o':
            return 'black'
        return 'red'

    def quitGame(self):
        self.didUserPickCol.set(True)
        self.window.destroy()

def main():
    root = Tk()
    root.title('Connect 4')
    myScreen = DemoScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()