# структурный паттерн - АДАПТЕР
# область - упаковка той же самой мебели

# Адаптер - связь между мебелью в упакованном состоянии и той,
# которую только предстоит упаковать
class Box:

    def __init__(self, count, newsize):
        self.count = count
        self.newsize = newsize

    def get_count(self):
        return self.count

    def get_newsize(self):
        return self.newsize

    def fit(self, packed):
        if (self.count >= packed.get_count()) & (self.newsize >= packed.get_newsize()):
            return f"Поместится " \
                    f"\n"\
                   f"Высота БЛОКА {packed.get_count()}, объём {packed.get_newsize()}" \
                    f"\n"\
                   f"Высота БОКСА {self.get_count()}, объём {self.get_newsize()}"
        else:
            return f"Не поместится " \
                    f"\n"\
                   f"Высота БЛОКА {packed.get_count()}, объём {packed.get_newsize()}" \
                    f"\n"\
                   f"Высота БОКСА {self.get_count()}, объём {self.get_newsize()}"


class Furniture:

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


class Packed:

    def __init__(self, count, newsize):
        self.count = count
        self.newsize = newsize

    def get_count(self):
        return self.count

    def get_newsize(self):
        return self.newsize


class Adapter(Packed):
    def __init__(self, furn):
        self.furn = furn

    def get_count(self):
        if self.furn.get_size() % 2 == 0:
            return self.furn.get_size() // 2
        else:
            return (self.furn.get_size() // 2) + 1

    def get_newsize(self):
        if self.furn.get_size() % 2 == 0:
            return (self.furn.get_size() // 2) * 3 * 6
        else:
            return ((self.furn.get_size() // 2) + 1) * 3 * 6


def client_code():
    box = Box(3, 60)
    packed1 = Packed(3, 54)
    packed2 = Packed(4, 100)
    furn1 = Furniture(5)
    furn2 = Furniture(7)

    print("Проверим упакованную")
    print("======================================================")
    print(box.fit(packed1))
    print("-----")
    print(box.fit(packed2))
    print("======================================================")

    print("Проверим неупакованную")
    print("======================================================")
    furn1_adapted = Adapter(furn1)
    furn2_adapted = Adapter(furn2)
    print(box.fit(furn1_adapted))
    print("-----")
    print(box.fit(furn2_adapted))


if __name__ == "__main__":
    client_code()
