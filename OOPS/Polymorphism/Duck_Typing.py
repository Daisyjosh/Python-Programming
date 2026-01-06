class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VSCode:
    def execute(self):
        print("Linting")
        print("Compiling")
        print("Running")

def myIDE(ide):
    ide.execute()

myIDE(Pycharm())
myIDE(VSCode())
