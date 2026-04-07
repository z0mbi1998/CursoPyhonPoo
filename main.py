class BaseList:
    def __init__(self):
        self.isCheck = False
        self.name = ''
        self.archive = False

    def checkitem(self):
        self.isCheck = not self.isCheck

    def isarchive(self):
        self.archive = not self.archive

l1 = BaseList()
l1.name = 'study'
l1.checkitem()
print(f'{l1.name} is a item in a base list and is done = {l1.isCheck} and archive = {l1.archive}')