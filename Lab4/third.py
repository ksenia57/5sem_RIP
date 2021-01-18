# поведенческий паттерн - СОСТОЯНИЕ
# область - упаковка - доставка - сборка той же самой мебели

# State - абстрактный класс состояний(в упаковке, в доставке, в сборке)
# Context - Класс нашей мебели
# handle(1, 2, 3) - функции перехода между состояниями
# upakovka, doctavka, sborka - функции, обозначающие процесс в новом сост-ии
from abc import ABC, abstractmethod


class Context:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов. Он также
    хранит ссылку на экземпляр подкласса Состояния, который отображает текущее
    состояние Контекста.
    """

    _state = None
    """
    Ссылка на текущее состояние Контекста.
    """

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        """
        Контекст позволяет изменять объект Состояния во время выполнения.
        """

#        print(f"Переход к {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    Контекст делегирует часть своего поведения текущему объекту Состояния.
    """

    def upakovka(self):
        self._state.handle1()

    def dostavka(self):
        self._state.handle2()

    def sborka(self):
        self._state.handle3()


class State(ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

    @abstractmethod
    def handle3(self) -> None:
        pass

"""
Конкретные Состояния реализуют различные модели поведения, связанные с
состоянием Контекста.
"""


class Upakovka(State):
    def handle1(self) -> None:
        print("Началась упаковка...")
        print("Упаковка кончилась, перехожу к доставке")
        self.context.transition_to(Dostavka())

    def handle2(self) -> None:
        print("ОТКАЗАНО => Ещё не упаковано - доставка невозможна")

    def handle3(self) -> None:
        print("ОТКАЗАНО => Ещё не упаковано и не доставлено - сборка невозможна")


class Dostavka(State):
    def handle1(self) -> None:
        print("ПРОТИВОРЕЧИЕ => Товар уже упакован и доставляется")

    def handle2(self) -> None:
        print("Товар доставляется...")
        print("Товар доставлен, перехожу к сборке")
        self.context.transition_to(Sborka())

    def handle3(self) -> None:
        print("ОТКАЗАНО => Ещё не доставлено - сборка невозможна")


class Sborka(State):
    def handle3(self) -> None:
        print("Мебель собирают...")
        print("Мебель собрали. Ура!")
        print("Приходите к нам снова")

    def handle2(self) -> None:
        print("ПРОТИВОРЕЧИЕ => Товар уже доставлен")

    def handle1(self) -> None:
        print("ПРОТИВОРЕЧИЕ => Товар уже упакован")


if __name__ == "__main__":
    # Клиентский код.
    print("Пройдем весь процесс сначала")
    print("===============================================================")
    context = Context(Upakovka())
    context.upakovka()
    context.dostavka()
    context.sborka()
    print("===============================================================")
    print("Попробуем начать с доставки")
    print("===============================================================")
    context = Context(Dostavka())
    context.dostavka()
    context.sborka()
    print("===============================================================")
    print("Теперь по противоречиям: попробем доставить неупакованный товар")
    print("===============================================================")
    context = Context(Upakovka())
    context.dostavka()
    print("===============================================================")
    print("Попробем собрать недоставленный")
    print("===============================================================")
    context = Context(Dostavka())
    context.sborka()
    print("===============================================================")
    print("Попробуем упаковать собираемый")
    print("===============================================================")
    context = Context(Sborka())
    context.upakovka()
    context.dostavka()
