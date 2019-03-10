def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result

print(countdown(4))

def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


g = gen_countdown(4)
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in gen_countdown(10):
    print(i)

# обычные функции отдают результат сразу а генераторы частями
# мы не тратим память на хранение ни промежуточного результата ни итогового
# использовать списки необходимо когда мы планируем обращаться к значениям по индексу много раз