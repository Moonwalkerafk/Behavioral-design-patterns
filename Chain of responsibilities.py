#В этом паттерне обработчики могут передавать запросы по цепочке, пока кто-то из них не обработает его.

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            self._next_handler.handle(request)


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handler A processed the request.")
        elif self._next_handler:
            self._next_handler.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handler B processed the request.")
        elif self._next_handler:
            self._next_handler.handle(request)


handler_chain = ConcreteHandlerA(ConcreteHandlerB())
handler_chain.handle("C")
handler_chain.handle("B")
handler_chain.handle("A")

