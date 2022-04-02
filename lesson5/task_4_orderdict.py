from collections import OrderedDict


a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

b = {'cat': 5, 'dog': 2, 'mouse': 4}
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)

print(new_a == new_b)

new_b.move_to_end('mouse')
print(new_b)
new_b.move_to_end('mouse', last=False)
print(new_b)

new_b.popitem()
print(new_b)
new_b.popitem(last=False)
print(new_b)

new_b['cow'] = 1
print(new_b)

new_b['cat'] = 5
new_b['dog'] = 8

print(new_b)

print('*' * 50)
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)

for key in reversed(new_c):
    print(key, new_c[key])
