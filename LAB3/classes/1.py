class in_out:
    def __init__(self):
        self.text=""
    def getString(self):
        self.text=input()
    def printString(self):
        print(self.text.upper())

a=in_out()
 
a.getString()
a.printString()

