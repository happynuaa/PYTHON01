from tkinter import Tk, Canvas
from time import sleep

WX = 1260
WY = 720
TY = 4
TX = 30
FY = 50
FX = 50
FH = 40
SPX = 20
x = SPX
x2 = WX-SPX
y = WY/2
y2 = WY/2
t = 0
t2 = 0


class Fighter():
    def __init__(self, c, ypoz, color, keyRight, keyLeft, keyUp, keyDown):
        self.c = c
        self.ship = self.c.create_polygon(
            SPX+FX, WY/2+ypoz,
            SPX+FX-FH, WY/2-FY/2+ypoz,
            SPX, WY/2+ypoz,
            SPX+FX-FH, WY/2+FY/2+ypoz,
            fill=color)
        self.c.bind_all(keyRight, self.right)
        self.c.bind_all(keyLeft, self.left)
        self.c.bind_all(keyUp, self.up)
        self.c.bind_all(keyDown, self.down)

    def right(self, event):
        global x
        if x < WX/2 - FX:
            self.c.move(self.ship, 10, 0)
            x += 10

    def left(self, event):
        global x
        if x > FX / 2:
            self.c.move(self.ship, -10, 0)
            x += -10

    def up(self, event):
        global y
        if y > FY/2:
            self.c.move(self.ship, 0, -10)
            y += -10

    def down(self, event):
        global y
        if y < WY-FY/2:
            self.c.move(self.ship, 0, 10)
            y += 10


if __name__ == "__main__":
    window = Tk()
    window.title('シューティングゲーム')
    c = Canvas(window, height=WY, width=WX, bg='blue')
    c.pack()
    f = Fighter(c, 100, 'yellow', '<KeyPress-d>',
                '<KeyPress-a>', '<KeyPress-w>', '<KeyPress-s>')
    f2 = Fighter(c, 200, 'red', '<KeyPress-Right>',
                 '<KeyPress-Left>', '<KeyPress-Up>', '<KeyPress-Down>')

    window.mainloop()
