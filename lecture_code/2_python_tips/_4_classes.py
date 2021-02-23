import time


class Animal(object):
    def __init__(self, name, owner=None):
        self.name = name
        self._owner = owner
        self.alive = True

    def die(self):
        self.alive = False

    @staticmethod
    def sleep(duration):
        time.sleep(duration)

    def __call__(self, x):
        print(x)


class Dog(Animal):
    def __init__(self, name, owner=None):
        super().__init__(self, name)

        self.legs = 4

    def die(self):
        print('Went to Heaven')







