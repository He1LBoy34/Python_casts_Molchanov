# closures
# замыкания

# все переменные это всегда ссылки на объект

def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner()

o = one()

# a = o.__closure__[0].cell_contents
print(dir(o))

# нихрена не понял, но интересно ))
# возможно синтаксис изменился на момент написания видеоурока