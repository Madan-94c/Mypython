#creating  a class area of circle
class circle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return 3.14*self.radius*self.radius
obj=circle(5)
obj.area()
