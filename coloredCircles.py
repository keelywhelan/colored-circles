#Keely Whelan
#Creates a randomly colored circle of the users determined point of origin and radius then makes inner circles
#each with a radius 10% smaller than the last, only while radius is greater than 4
from graphics import *
import math
import random

def main():
    win =GraphWin("window",600,600)
    win.setCoords(0,0,40,40)

    pntMsg=Point(20,5)
    txtMsg=Text(pntMsg, "click where you want the circle's point of origin")
    txtMsg.draw(win)
    
    p1=win.getMouse()

    txtMsg.setText("click where you want the edge of the circle to reach")
    
    p2=win.getMouse()

    txtMsg.undraw()

    a=int(p2.getX())
    print("a :",a)
    b=int(p1.getX())
    c=int(p2.getY())
    d=int(p1.getY())

    r=math.sqrt((a-b)**2+(c-d)**2)
    print("r: " ,r)

    cir=Circle(Point(b,d),r)

    cir.draw(win)
    randColor=color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cir.setFill(randColor)
    
    while (r>=5):
        r=r-r/10
        cir=Circle(Point(b,d),r)
        cir.draw(win)
        randColor=color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        cir.setFill(randColor)

                   
main()
