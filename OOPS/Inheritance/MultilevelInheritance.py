class A:
    def m1(self):
        print("A")

class B(A):
    def m2(self):
        print("B")

class C(B):
    def m3(self):
        print("C")

c = C()
c.m1()