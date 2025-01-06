#Поведенческий паттерн проектирования, который предоставляет способ последовательного доступа к элементам составного объекта (например, коллекции или массиву) независимо от его реализации.


class MyCollection:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return MyIterator(self.items)


class MyIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


collection = MyCollection([1, 2, 3, 4, 5])
for item in collection:
    print(item)
