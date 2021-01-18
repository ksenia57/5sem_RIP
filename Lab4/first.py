# порождающий паттерн проектирования
# абстрактная фабрика или просто фабрика
# короче что-то между
# предметная область: мебель
from abc import ABC, abstractmethod


def define_mat(platform):
    if platform == "Деревянный":
        return "дерево"
    elif platform == "Металлический":
        return "металл"
    elif platform == "Плетеный":
        return "бамбук"


def define_stil(stilchik):
    if stilchik == "Современный":
        return "современном"
    elif stilchik == "Классический":
        return "классическом"


# абстрактный класс материала
class Material(ABC):

    @abstractmethod
    def paint(self, mat):
        pass


# абстрактный класс стиля
class Style(ABC):

    @abstractmethod
    def paint(self, stil):
        pass


# абстрактный класс того, что делают с мебелью
class Metod(ABC):

    @abstractmethod
    def paint(self):
        pass


# Абстрактная фабрика
class FurnFactory(ABC):

    @abstractmethod
    def create_material(self):
        pass

    @abstractmethod
    def create_style(self):
        pass

    @abstractmethod
    def create_metod(self):
        pass


# класс материала для стола
class TableMaterial(Material):

    def paint(self, mat):
        return f"Создание стола из материала {mat}"


# класс материала для стула
class ChairMaterial(Material):

    def paint(self, mat):
        return f"Создание стула из материала {mat}"


# класс стиля для стола
class TableStyle(Style):

    def paint(self, stil):
        return f"В {stil} стиле"


# класс стиля для стула
class ChairStyle(Style):

    def paint(self, stil):
        return f"В {stil} стиле"


# класс применения для стола
class TableMetod(Metod):

    def paint(self):
        return "На нём едят"


# класс применения для стула
class ChairMetod(Metod):

    def paint(self):
        return "На нём сидят"


# фабрика для стола
class TableFactory(FurnFactory):

    def create_material(self):
        return TableMaterial()

    def create_style(self):
        return TableStyle()

    def create_metod(self):
        return TableMetod()


# фабрика для стула
class ChairFactory(FurnFactory):

    def create_material(self):
        return ChairMaterial()

    def create_style(self):
        return ChairStyle()

    def create_metod(self):
        return ChairMetod()


# клиентский код
def client_code(factory):
    material = factory.create_material()
    style = factory.create_style()
    kak = factory.create_metod()

    print(material.paint(define_mat("Деревянный")))
    print(style.paint(define_stil("Современный")))
    print(kak.paint())
    print("***********************************")
    print(material.paint(define_mat("Металлический")))
    print(style.paint(define_stil("Современный")))
    print(kak.paint())
    print("***********************************")
    print(material.paint(define_mat("Плетеный")))
    print(style.paint(define_stil("Классический")))
    print(kak.paint())
    print("***********************************")


if __name__ == "__main__":
    print("Соберем мебель - стол")
    print("==================================")
    client_code(TableFactory())

    print('\n')

    print("Соберем мебель - стул")
    print("==================================")
    client_code(ChairFactory())

    print('\n')
