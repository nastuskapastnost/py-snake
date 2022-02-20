# from tkinter import*
import time
from tkinter import *
import random

Game_Running = True
# Окно
window_width = 700
window_height = 700
# Змейка
snake = 20
snake_colour = "ForestGreen"
snake_colour2 = "DarkGreen"
food_colour = "#F1C40F"
food_colour2 = "#C70039"
snakex = 17
snakey = 17
snakex_new =0
snakey_new =0
snake_size =3
food_size =5
realfoodx = window_width/snake
realfoody = window_height/snake
snake_list = []
food_list = []


# ~~~~~~~~~~~~~~~~~~~~~~~
# Само окошко
tk = Tk ()
tk.title ("ИГРА ЗМЕЙКА ~~~~~~~~")
# tk.resizable (0, 0)
tk.resizable (False, False)
tk.wm_attributes ("-topmost", 1)
canvas = Canvas (tk, width=window_width, height=window_height, bd=0, highlightthickness=0)
canvas.pack ()
tk.update ()
# ~~~~~~~~~~~~~~~~~~~~~~~
for i in range(food_size):
    x = random.randrange(realfoodx)
    y = random.randrange(realfoody)
    id1 = canvas.create_oval (x * snake, y * snake, x * snake + snake, y * snake + snake, fill=food_colour2)
    id2 = canvas.create_oval (x * snake + 2, y * snake + 2, x * snake + snake - 2, y * snake + snake - 2,fill=food_colour)
    food_list.append([x, y, id1, id2])
# print(food_list)
# ~~~~~~~~~~~~~~~~~~~~~~~
def snake_paint (canvas,x,y):
    global snake_list
    id1 = canvas.create_rectangle (x*snake,y*snake,x*snake+snake,y*snake+snake,fill = snake_colour2)
    id2 = canvas.create_rectangle (x * snake + 2, y * snake + 2, x * snake+snake - 2, y * snake+snake - 2, fill = snake_colour)
    snake_list.append([x,y,id1,id2])
   # print (snake_list)
snake_paint(canvas,snakex,snakey)

def snake_size_delete ():
    if len (snake_list) >= snake_size:
        e=snake_list.pop (0)
        #print(e)
        canvas.delete (e[2])
        canvas.delete (e[3])

def snake_move (event):
    global snakex
    global snakey
    global snakex_new
    global snakey_new
    if event.keysym == "Right":
        snakex_new = 1
        snakey_new = 0
        snake_size_delete()
    if event.keysym == "Left":
        snakex_new = -1
        snakey_new = 0
        snake_size_delete()
    if event.keysym == "Up":
        snakex_new = 0
        snakey_new = -1
        snake_size_delete()
    if event.keysym == "Down":
        snakex_new = 0
        snakey_new = 1
        snake_size_delete()
    snakex = snakex + snakex_new
    snakey = snakey + snakey_new
    snake_paint(canvas,snakex,snakey)
    eat_food()
def eat_food ():
    global snake_size
    for i in range (len (food_list)):
        if food_list [i][0] == snakex and food_list [i][1] == snakey:
            snake_size = snake_size + 1
            canvas.delete (food_list[i][2])
            canvas.delete (food_list[i][3])

# ~~~~~~~~~~~~~~~~~~~~~~~
def tach_borders ():
    if snakex<0 or snakey<0 or snakex>realfoodx or snakey>realfoody:
        game_over ()
def game_over ():
    global Game_Running
    Game_Running = False
def snake_stop ():
    if not (snakex_new==0 and snakey_new==0):
        for i in range (len(snake_list)):
            if snake_list [i][0]==snakex + snakex_new and snake_list [i][1]== snakey + snakey_new:
                game_over()
# ~~~~~~~~~~~~~~~~~~~~~~~
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)
# ~~~~~~~~~~~~~~~~~~~~~~~
# Бесконечный цикл
while Game_Running:
    snakex = snakex + snakex_new
    snakey = snakey + snakey_new
    snake_paint(canvas, snakex, snakey)
    #print (snake_list)
    tach_borders()
    snake_stop()
    time.sleep(0.5)
    snake_size_delete()
    eat_food()
    tk.update ()
