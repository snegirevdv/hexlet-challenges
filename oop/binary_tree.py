class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

    def insert(self, number):
        if self.key is None:
            self.key = number

        if self.key == number:
            return

        if self.key > number:
            if self.left is None:
                self.left = self.__class__()
            target = self.left

        else:
            if self.right is None:
                self.right = self.__class__()
            target = self.right

        target.insert(number)
