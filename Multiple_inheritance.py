#Multiple inheritance
class A:
  def feature1(self):
    print("Feature1")
class B:
  def feature2(self):
    print("Feature2")
class C(A,B):
  pass
obj=C()
obj1=A()
obj1.feature1()
obj2=B()
obj2.feature2()
