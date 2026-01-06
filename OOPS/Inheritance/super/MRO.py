# => MRO - Method Resolution Order

class A:
    def show(self):
        print("A")
    
class B:
    def show(self):
        print("B")

class C(A,B):
    pass

c = C()
c.show() #prints B because of MRO goes from Left to right

print(C.mro())