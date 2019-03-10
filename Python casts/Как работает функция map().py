# map(func, *iterable)

def upper2(string):
    return string.upper()

l = ['one', 'two', 'three']

new_list = list(map(upper2, l))
print(new_list)

new_l = list(map(lambda string: string.upper(), l))

print(new_l)

nl = [string.upper() for string in l]
print(nl)

def map2(func, iterable):
    for i in iterable:
        yield func(i)

