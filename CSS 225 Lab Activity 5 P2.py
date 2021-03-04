#Miguel Rodriguez
#February 25,2021
#Lab Activity 5 Problem 2

#Write a program that:
    #• Imports the Turtle module
    #• Creates a turtle and gives it a name
    #• Gets a color from the user using the input() function
    #• Uses a for loop and the Turtle module to draw a square in that color.
    #   ◦ Remember: Every angle inside a square is 90°.
import turtle
Mig= turtle.Turtle()
black=input("What color do you want?")
Mig.pencolor(black)
for side in range(4):
    Mig.forward(50)
    Mig.right(90)


