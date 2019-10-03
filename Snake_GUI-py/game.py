import simplegraphics as graphic
import time
import random
import sys

# TODO(Elvis): Fix Flickering

pos = [ 100.0, 100.0 ]
direction = [ 20, 0 ]
snake = []
foodPos = [ 200, 200 ]
eaten = False
score = 0

def randomizeFood():
    foodPos[0] = (random.randint(0, 780) // 20 * 20)
    foodPos[1] = (random.randint(0, 580) // 20 * 20)

def gameOver():
    graphic.text(400, 10, "Game Over! Your Score was: %s" % score)
    sys.exit(0)
    graphic.exit(0)

def drawSnake(x, y, eaten = False):
    graphic.setFill(0,0,0)
    snake.insert(0, y) 
    snake.insert(0, x)

    if(snake[0] < 0 or snake[0] > 800 or snake[1] < 0 or snake[1] > 600):
        gameOver()

    if(len(snake) > 1):
        for item in range(0, (len(snake)), 2):
            graphic.rect(snake[item], snake[item + 1], 20, 20)

            if(item != 0 and (snake[0] == snake[item] and snake[1] == snake[item + 1])):
                gameOver()
    else:
        graphic.rect(snake[0], snake[1], 20, 20)

    if(snake[0] == foodPos[0] and snake[1] == foodPos[1]):
        randomizeFood()
        eaten = True
        global score
        score += 1

    graphic.rect(foodPos[0], foodPos[1], 20, 20)

    if(len(snake) > 0 and not eaten):
        snake.pop()
        snake.pop()

def isValid(k):
    if(k == {'w'} or k == {'a'} or k == {'s'} or k == {'d'}):
        return True
    else:
        return False

while not graphic.closed():
    key = graphic.getHeldKeys()
    
    if(isValid(key)):
        if(key == {'w'} and direction[1] != 20):
            direction[1] = -20
            direction[0] = 0
        elif(key == {'a'} and direction[0] != 20):
            direction[0] = -20
            direction[1] = 0
        elif(key == {'s'} and direction[1] != -20):
            direction[1] = 20
            direction[0] = 0
        elif(key == {'d'} and direction[0] != -20):
            direction[1] = 0
            direction[0] = 20

    drawSnake(pos[0], pos[1])

    pos[0] += direction[0]
    pos[1] += direction[1]
    
    graphic.text(400, 10, score)
    time.sleep(0.1)
    graphic.clear()