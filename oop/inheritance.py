#single inheritance
#Multi-level inheritance
#multiple inheritance

#This is multi-level inheritance
class A:
    def a(self):
        print("This is Class A")
class B(A):  #Class 'A' is inheritant to class 'B'
    def b(self):
        print("This is Class B")
class C(B):   #Class 'B' is inheritant to class 'C'
    def c(self):
        print("This is Class C")
classes = C()
classes.a()
classes.b()
classes.c()