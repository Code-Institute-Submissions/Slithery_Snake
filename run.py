# My Imports
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Sneaky Snake")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0,100)

segments = []