from request import request
from timer import TicToc

class counter:
    def __init__(self, productCondition = "OK", quantityRegister = 10, delay = 30):
        self.count = 0
        self.productCondition = productCondition
        self.quantityRegister = quantityRegister
        self.timer = TicToc(delay)
    
    def getCount(self):
        return self.count
    
    def resetCount(self):
        self.count = 0
    
    def addCount(self):
        self.timer.setTic()
        self.count += 1
        if self.getCount() > self.quantityRegister or self.timer.canScore():
            print("Enviando registros...")
            self.saveData()
            print("Registros enviados.")
            self.resetCount()
            self.timer.setToc()

    def saveData(self):
        if self.getCount() > 0:
            r = request(self.productCondition)
            r.post_async(self.getCount())