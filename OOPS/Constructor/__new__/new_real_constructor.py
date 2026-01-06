# Allocates Memory
# Returns Object Instance

#Uses
# => Making immutable classes (str,tuple)
# => Custom Memory Management
class Demo:
    def __new__(cls):
        print("__new__ called object created")
        return super()._new_(cls)
    def __init__(self):
        print("__init__ called object initialized")