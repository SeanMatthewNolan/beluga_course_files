def module_function():
    print(__name__)
    return 'I am in a folder in the module'


class ModuleClass:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    steve = ModuleClass('Steve')
