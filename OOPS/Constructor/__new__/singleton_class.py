class Singleton:
    _instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

a = Singleton()
b = Singleton()

print(a is b) # Both Variable refer to same object