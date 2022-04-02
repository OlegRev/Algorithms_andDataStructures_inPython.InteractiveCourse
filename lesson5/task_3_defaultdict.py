from collections import defaultdict

a = defaultdict()
print(a)

s = 'dgwebfgewkmvoicemwiowenvirwnvrwbbnteiobne'
b = defaultdict(int)
for i in s:
    b[i] += 1

print(b)

# пример для датчиков ("название датчика", статус_датчика)
# накопление сигналов с датчиков(повторяющиеся тоже)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)

print(c)

# пример для датчиков ("название датчика", статус_датчика)
# накопление сигналов с датчиков (уникальные сигналы)

list_2 = [('cat', 1), ('dog', 5), ('cat', 2),
          ('cat', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)

print(d)


# пример использования своей функции в defaultdict(функция)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
