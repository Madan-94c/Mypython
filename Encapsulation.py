#Encapsulation
class me:
  def __init__(self):
    self.public="I am public"
    self.__private="I am private"
  def display(self):
    print(self.__private)
obj=me()
obj.display()
