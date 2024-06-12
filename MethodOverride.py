class A:
    def show(self):
        print("Show from A")
class B(A):
    def show(self):
        super().show()
        print("Show from B")
class C(A):
    def show(self):
        super().show()
        print("Show from C")
class D(C,B):
    def show(self):
        super().show()
        print("Show from D")

d1=D()
d1.show()
