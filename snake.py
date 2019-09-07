"""My first attempt at code to play snake game"""
import matplotlib.pyplot as plt
import math
from collections import deque
import random

n=21 #the size of our grid, looks nicer if an odd number!

snake = deque([[math.ceil(n/2),math.ceil(n/2)-2],
               [math.ceil(n/2),math.ceil(n/2)-1],
               [math.ceil(n/2),math.ceil(n/2)]])

#The END of this array stores the FRONT of the snake
#(We initally start with a snake which is just three units long)
game_state = 0
rate = 0.1 #controls the snake's speed
ms = 10 #controls the size of the chunks the snake is made of
snake_dir = 'up'

fig, ax = plt.subplots()
ax.set(xlim=(-0.5,n-0.5),ylim=(-.5,n-0.5))
food_array=[]
for i in range(n):
    for j in range(n):
        if [i,j] not in snake:
            food_array.append([i,j])
food = random.choice(food_array)
foods = plt.plot(food[0], food[1],'o',color='red', markersize=ms-1)[0]

points=[]
for snk in snake:
    points.extend(plt.plot(snk[0],snk[1],'s',color='black',markersize=ms))


def dirrection():
    global food, foods, game_state, snake_dir, snake, n
    if snake_dir == 'up':
        snake.append([snake[len(snake)-1][0],(snake[len(snake)-1][1]+1)%n])
    elif snake_dir == 'down':
        snake.append([snake[len(snake)-1][0], (snake[len(snake)-1][1]-1)%n])
    elif snake_dir == 'right':
        snake.append([(snake[len(snake)-1][0]+1)%n, snake[len(snake)-1][1]])
    elif snake_dir == 'left':
        snake.append([(snake[len(snake)-1][0]-1)%n, snake[len(snake)-1][1]])

    snake.popleft()
    points.extend(plt.plot(snake[len(snake)-1][0],snake[len(snake)-1][1], 's',color='black',markersize=ms))
    points[0].remove()
    del points[0]
        
    for i in range(len(snake)-2):
        if snake[i] == snake[len(snake)-1]:
            game_state = 1
            print("Game Over!")
            print("You scored " , len(snake) -3, " points!")
    
    plt.pause(rate)

    if snake[len(snake)-1] == food:
        if snake_dir == 'up':
            snake.append([snake[len(snake)-1][0],(snake[len(snake)-1][1]+1)%n])
        elif snake_dir == 'down':
            snake.append([snake[len(snake)-1][0], (snake[len(snake)-1][1]-1)%n])
        elif snake_dir == 'right':
            snake.append([(snake[len(snake)-1][0]+1)%n, snake[len(snake)-1][1]])
        elif snake_dir == 'left':
            snake.append([(snake[len(snake)-1][0]-1)%n, snake[len(snake)-1][1]])
            
        points.extend(plt.plot(snake[len(snake)-1][0],snake[len(snake)-1][1], 's',color='black',markersize=ms))
        
        foods.remove()
        del foods
        food_array=[]
        for i in range(n):
                for j in range(n):
                    if [i,j] not in snake:
                        food_array.append([i,j])
        food = random.choice(food_array)
        foods = plt.plot(food[0], food[1],'o',color='red', markersize=ms-1)[0]
        plt.pause(rate)

def on_press(event):
    global snake_dir, game_state
    snake_dir = event.key
    if event.key == 'esc':
        plt.close()
        game_state =1

cid = fig.canvas.mpl_connect('key_press_event',on_press)   

while game_state == 0:
    dirrection()     
        