import turtle
import random

#Exercise 1
def tree(branchLen,t):
    if branchLen > 5:
        if branchLen < 20:
            t.color("#1fe31b")
        t.width((branchLen) / 9)
        t.forward(branchLen)
        angle = random.randrange(18,40)
        subtractBranch = random.randrange(8,10)
        t.right(angle)
        tree(branchLen-subtractBranch,t)
        t.left(angle * 2)
        tree(branchLen-subtractBranch,t)
        t.right(angle)
        t.backward(branchLen)
        t.color("#402d1c")
        
def main():
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(0)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("#402d1c")
    tree(75,t)
    myWin.exitonclick()
    
main()

#Exercise 2
#1
def power(x,n,acc):
    if n == 0:
        return acc
    else:
        return power(x,n-1,acc*x)

#2
def powerH(x,n):
    if n == 0:
        return 1
    elif (n % 2 == 0):
        return powerH(x,n/2) * powerH(x, n/2)
    else:
        return powerH(x,(n-1)/2) * powerH(x,(n-1)/2) * x

#3
def C(n,k):
    if (k==0 or k==n) and n>=0:
        return 1
    else:
        return C(n-1,k) + C(n-1,k-1)