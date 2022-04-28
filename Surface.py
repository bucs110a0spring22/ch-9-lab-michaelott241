from Rectangle import Rectangle

class Surface:
  def __init__(self,filename,x,y,h,w):
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    self.image = filename
    self.rect = Rectangle(self.x,self.y,self.height,self.width)
  def getRect(self):
    return self.rect
    
  
  