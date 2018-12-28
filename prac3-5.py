from tkinter import *
import time
import random
import _tkinter


tk = Tk()
tk.title("Pinball Game")
canvas = Canvas(tk, width = 800, height = 600, bg = "pink", bd = 0,highlightthickness = 0)
tk.resizable(0,0)
canvas.pack()
tk.update()

class Ball: # Class of Ball
    def __init__(self,canvas,paddle,color): # initialize the ball
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10, 25, 25, fill = color) # draw a ball on the canvas
        self.canvas.move(self.id,240,100) # at the start state the position of ball
        stat = [-3,-2,-1,1,2,3]
        random.shuffle(stat)
        self.x = stat[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3]<= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y =3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x = -3
class Paddle:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,150,10,fill = color)
        self.canvas.move(self.id ,400,450)
        self.x = 0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<Key-Left>",self.turn_left)
        self.canvas.bind_all("<Key-Right>", self.turn_right)
    def turn_left(self,event):
        self.x = -5
    def turn_right(self,event):
        self.x = 5
    def draw(self):
        pos = self.canvas.coords(self.id)
        self.canvas.move(self.id,self.x,0)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
paddle = Paddle(canvas,"blue")
ball = Ball(canvas,paddle,"red")
while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)