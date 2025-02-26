class Calculator:

    def __init__(self, num_1: [int, float], num_2: [int, float]) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

    def plus(self) -> [int, float]:
        return self.num_1 + self.num_2

    def multiply(self) -> [int, float]:
        return self.num_1 * self.num_2

    def pow(self) -> [int, float]:
        return self.num_1 ** self.num_2
