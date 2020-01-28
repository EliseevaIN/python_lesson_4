from random import choices
from collections import Counter

print('1. Функция (F): на вход список из 20 имён и целое число N; на выходе список длины N=100 случайных имён из первого списка.')
def choice_name(name, n=100):
    return choices(name, k=n)
names = choice_name(['Герасим', 'Мичлов', 'Мелисса', 'Владлен', 'Лука', 'Мариан', 'Ада', 'Мелисса', 'Гастон', 'Тимофей', 'Владимир', 'Гурий', 'Василиса', 'Федор', 'Рем', 'Александра', 'Рубен', 'Флорентий', 'Ульманас', 'Валентина'])
print('100 имён:', names)
print()

print('2. Функция  вывода самого частого имени из списка на выходе функции F.')
name_dict = {}
for i in range(len(names)):
    name_dict[names[i]] = names.count(names[i])
often_name = Counter(name_dict).most_common(1)
print('Самое частое имя:', often_name)
print()

print('3. Функция  вывода самой редкой буквы, с которой начинаются имена в списке на выходе функции F.')
letters = []
for word in names:
    letters+= word[0]
letters_dict = {}
for let in letters:
    letters_dict[let] = letters.count(let)
print('Самая редкая буква:', list(letters_dict)[-1])
print()

from datetime import datetime
with open('log.txt', mode='r', encoding='utf-8') as file:
    last_date = 0
    for line in file:
        if not last_date:
            last_date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
            continue
        date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
        if date > last_date:
            last_date = date
print('4. Дата самого позднего лога:', last_date)