import turtle
branchLen = 30

t = turtle.Turtle()

myWin = turtle.Screen() 

t.left(90) 

t.up()

t.backward(100)

t.down()

t.color("green")

#--------------STARTS-------------------
for drawing in range(3):
    t.forward(branchLen) 

    t.right(20)
    
t.color("blue")

t.right(20)

t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.backward(branchLen)
t.color("red")
t.left(40)
t.color("red")
t.forward(branchLen)
t.color("red")
t.right(20)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.right(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.right(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.left(40)
t.color("red")
t.forward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.forward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.right(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.right(40)
t.color("red")
t.forward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.right(40)
t.color("red")
t.forward(15)
t.color("red")
t.backward(15)
t.color("red")
t.left(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.left(20)
t.color("red")
t.backward(branchLen)
t.color("red")
t.right(20)
t.color("red")
t.backward(branchLen)
t.color("red")

# ---------------------------------------------------
#t.color("") is to change the colour
#t.backward is to make it go backwards
#t.right or t.left is so it goes left or right
#t.forward is so it goes forward
#branchLen is the length
#t = turtle.Turtle() is the turtle
#myWin = turtle.Screen() so the screen pops up
#myWin.exitonclick() so the thing doesn't crash when the code ends and you can just press the X on the screen
#----------------------------------------------------
# The Questions:

# What is difference in the recursive code and the iterative code?
# Recursion the function calls to shutdown the stuff inside of the function
# and iteration is loops like while
# How does the code execute differently in each?
# Recursion just executes the stuff in the function 
# and iteration just uses while to execute.
# What is the difference between recursion and iteration?
# one is using whle and Recurision calls to execute code
# Part 2:

#        Explain:
#
# Where would recursion be the best option?
# Recursion would be the best option in like a bigger program that has steps that you could use recursion in
# When would it not?
#  if you need to stack it's not the best 
#What are some specific examples of recursion that can work for you?
#To solve a bit of problems




#I helped patty out on this because I learnt how use turtles and It was my idea to use the code like this before you told patty to do it like
#this and I teached him on how to write it down :) hopefully u could understand

myWin.exitonclick()
