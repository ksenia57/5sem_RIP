# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    if len(args) == 1:
        for item in items:
            if item[args[0]] is not None: yield item[args[0]]
    elif len(args) > 1:
        for item in items:
            # Проверим, не являются ли все значения None
            count = 0
            for arg in args:
                if item[arg] is None: count += 1
            # Если нет, продолжаем
            if count != len(args):
                # Создаем словарь
                result = {}
                # Добавляем в него != None элементы
                for arg in args:
                    if item[arg] is not None:
                        result[arg] = item[arg]
                # Возвращаем словарь
                yield result