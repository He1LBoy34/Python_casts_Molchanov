# filter(func, iterable) функция принимает на два аргумента - фильтрующую функцию и итерируемый объект чаще всего список

def has_o(string):
    return 'o' in string.lower()

l = ['One', 'two', 'three', 'shfabuir']

nl = list(filter(has_o, l))

print(nl)

newl = list(filter(lambda string: 'o' in string.lower(), l))

print(newl)

nl2 = [string for string in l if has_o(string)]

print(nl2)