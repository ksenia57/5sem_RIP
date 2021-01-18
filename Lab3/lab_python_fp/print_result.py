def print_result(func_to_print):
    def decorated_func(arg):
        # Вывод названия функции
        print(func_to_print.__name__)

        # Исполнение фукнции
        result = func_to_print(arg)

        # Вывод результата в зависимости от его типа
        if type(result) is list:
            for item in result:
                print(item)
        elif type(result) is dict:
            for key, item in result.items():
                print(f'{key} = {item}')
        else:
            print(result)

        # Возвращение значения функции
        return result

    return decorated_func

def test_1():
    return 1

def test_2():
    return 'iu5'

def test_3():
    return {'a': 1, 'b': 2}

def test_4():
    return [1, 2]

def main():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == '__main__':
    main()
