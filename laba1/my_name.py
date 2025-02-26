class Calculator:

    def __init__(self, num_1: int, num_2: int) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

    def plus(self) -> int:
        return self.num_1 + self.num_2


test = Calculator(2, 2)
print(test.plus())
