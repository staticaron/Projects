class DoubleNode:

    #Data members
    data = 0
    left = None
    right = None

    #Constructor
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def printInfo(self):
        print(self.data)
        return [self.left, self.right]
