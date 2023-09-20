class A:
    def a(self):
        print("My Name is Anjila Tripathi")
class B:
    def b(self):
        print("I study in PadmaKanya Multiple Campus")
class C(A,B):
    def c(self):
        print("Class 'C' inherited class 'A' and class 'B'")

classes = C()
classes.a()
classes.b()
classes.c()