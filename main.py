import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
def moveplayer():
    player.move()

screen.listen()
screen.onkey(moveplayer,"Up")

game_is_on = True
while game_is_on:
    cars.create_car()
    cars.movecar()
    for car in cars.allcars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()
            scoreboard.forward(1)
        elif player.ycor() >=270:
            scoreboard.increasescore()
            player.reset()
            cars.increasespeed()
                                                  
    time.sleep(0.1)
    screen.update()

screen.exitonclick()