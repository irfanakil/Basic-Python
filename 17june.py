#creating class shapes

class ShapeClass:
    'Shape related operations and info'
    #class variable
    shapecount=0
     def __init__(self):
         #instance variable(has diff options)
          self.color=''
          self.borderwidth=0
         shape.shapecount+=1
     def getcolor(self):
         return self.color
     def setcolor(self,c):
         self.color=c
     def getborderwidth(self):
         return self.borderwidth
     def setborderwidth(self,bw):
         self.borderwidth=bw

