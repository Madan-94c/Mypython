#Polymorphism
class animal:
  def name(self):
    print("Lion")
class weight(animal):
  def name(self):
    print("Tiger")
obj=weight()
obj.name()
