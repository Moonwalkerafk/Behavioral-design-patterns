#Стратегия позволяет выбрать один из возможных алгоритмов выполнения, не изменяя саму структуру объекта.


from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b


class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b


class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)


context = Context(AddStrategy())
print("Addition: ", context.execute_strategy(5, 3))

context.set_strategy(SubtractStrategy())
print("Subtraction: ", context.execute_strategy(5, 3))

context.set_strategy(MultiplyStrategy())
print("Multiplication: ", context.execute_strategy(5, 3))
