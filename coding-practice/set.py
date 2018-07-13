"""

 Insert, Remove, and GetRandomElement

use a map

 """
class MySet():
    def __init__(self):
	self.items = []

    def Insert(self, item):
	if item not in self.items:
	    self.items.append(item)

    def Remove(self, item):
        if item in self.items:
            index = self.items.index(item)
            size = len(self.items)
            self.items[index], self.items[size - 1] = self.items[size - 1], self.items[index]


    def GetRandomElement(self):
	pass


