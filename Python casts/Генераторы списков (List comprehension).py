# Генераторы списков List comprehension4

some_list = [1, 2]

things = [x for x in some_list]

jack = {
    'name':'jack',
    'car':'bmw'
}

john = {
    'name':'john',
    'car':'audi'
}

users = [jack, john]  # это список словарей

# cars = [person['car'] for person in users]  короткая запись
# cars = [person.get('car', '') for person in users]    лучше обращаться через .гет тк аргумента может не быть и мы получим исключение

cars = []  # длинная запись
for person in users:
    cars.append(person['car'])

print(cars)

# (values) = [(expression) for (value) in (collection)]

# фильтрация
names = ['jack', 'john', 'oleg', 'jula']

new_names = [n for n in names if n .startswith('j')]

print(new_names)

new_names2 = []

for n in names:
    if n.startswith('j'):
        new_names2.append(n)

print(new_names2)

# (values) = [(expression) for (value) in (collection) if (condition)]