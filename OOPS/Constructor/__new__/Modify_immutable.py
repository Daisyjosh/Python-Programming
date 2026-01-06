class MyStr(str):

    def __new__(cls, value):
        value = value.upper()
        return super().__new__(cls, value)

s = MyStr("hello")
print(s)