from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars=[]
        self.speed = MOVE_INCREMENT

    
    def create_car(self):
        if random.randint(0,6) == 3:
            new_car = Turtle("square")
            new_car.shapesize(1,3)
            new_car.penup()
            new_car.color(COLORS[(random.randint(0,5))])
            new_car.setheading(180)
            START_LOCATION = (270,random.randint(-270,270))
            new_car.goto(START_LOCATION)
            self.allcars.append(new_car)
    
    def movecar(self):
        for car in self.allcars:
            car.forward(self.speed)

    def increasespeed(self):
        self.speed +=10