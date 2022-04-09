lst = []

lst.append(1)
lst.extend([2, 3, 4])

print(lst)

lst.insert(1, 5)
print(lst)

last = lst.pop()
print(lst, last)

last = lst.pop()
print(lst, last)

lst.remove(5)
print(lst)
