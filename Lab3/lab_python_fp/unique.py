from lab_python_fp.gen_random import gen_random
# Итератор для удаления дубликатов
class unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.used = set()
        self.index = 0
        self.items = items if type(items) is list else [i for i in items]
        self.ignore_case = True if len(kwargs) > 0 and kwargs['ignore_case'] == True else False

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            if (self.index >= len(self.items)):
                raise StopIteration
            else:
                current = self.items[self.index]
                self.index += 1
                if (self.ignore_case and current not in self.used or not self.ignore_case and str(
                        current).lower() not in self.used):
                    self.used.add(
                        current if self.ignore_case else str(current).lower())
                    return current

    def __iter__(self):
        return self