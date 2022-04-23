"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, namedtuple

# TODO class HaffmanCode


# TODO def __init__
# создаем именовоный кортеж "лист" "узел"
Leaf = namedtuple("Leaf", 'key, value')
Node = namedtuple("Node", 'value, left, right')

# создаем таблицу кодов по Хаффману
# используется в функции recursive_tree_traversal
huffman_code_table = dict()
# основной список для формирования листьев->дерева
data_list = []


# строка для кодирования
s = "beep boop beer!"

# создаем счетчик символов в строке и сортируем его
sort_counter = sorted(Counter(s).items(), key=lambda k: k[1], reverse=True)

# TODO def __make_leafs_list
# формируем список "листев"

for k, v in sort_counter:
    # добавляем лист в список
    data_list.append(Leaf(k, v))

# выводим на экран
# print(data_list)


# TODO def __make_tree

# Формируем дерево созданием узлов для дерева
# print(data_list)
while len(data_list) >= 2:
    # формируем переменные
    left, right = data_list.pop(), data_list.pop()
    # создаем узел из сформированых переменных left, right
    node = Node(left.value + right.value, left, right)
    # print(data_list)
    # добавляем созданый узел обратно с наш список
    data_list.append(node)
    # сортируем наш список по атрибуту value
    # необходимо что бы у объектов Leaf, Node были атрибуты value
    data_list = sorted(data_list,
                       key=lambda k: k.value,
                       reverse=True)
    # print(node)
print(f"{'*' * 50}\n{data_list}\n{'*' * 50}")

# TODO __recursive_tree_traversal


def recursive_tree_traversal(data: Node, code=''):
    """Рекурсивный обход построенного дерева
    с созданием таблицы кодов по Хаффману"""
    # если поданный объект имеет тип Node то формируем код
    if isinstance(data, Node):
        # print(data)
        recursive_tree_traversal(data.left, code=f'{code}0')
        recursive_tree_traversal(data.right, code=f'{code}1')
    # если поданный объект имеет тип Leaf то записываем code в таблицу кодов
    elif isinstance(data, Leaf):
        # print(data)
        huffman_code_table[data.key] = code


recursive_tree_traversal(*data_list)
# TODO def get_haffman_code
print(huffman_code_table)
