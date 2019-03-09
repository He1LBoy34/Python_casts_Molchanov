def do_smth(*args, **kwargs):
    pass

def gen():
    for i in range(10):
        yield i

def add(*args, **kwargs):  # ключевой момент установка * перед множеством аргументов
    print(sum(args))
    print(kwargs)

# kwargs - именнованные аргументы

add(2, 3)

l = [1, 2, 3]

add(*l, street='Lenina', house=12)  # при вызове списка обязательно прописсывать *

add(*gen())  # генератор нельзя отдавать как аргумент при вызове функции через * т.к. он весь отрабатывается, что может занять очень много времени
