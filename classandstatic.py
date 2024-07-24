class SomeClass:
    some_class_variable = 10

    def __init__(self):
        pass

    @staticmethod
    def compute_sum(a, b):
        return a + b

    @classmethod
    def print_class_variable(cls):
        print(cls.some_class_variable)



if __name__ == "__main__":
    SomeClass.print_class_variable()
    print(SomeClass.compute_sum(10, 2))
