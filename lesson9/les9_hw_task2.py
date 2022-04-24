"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, namedtuple

# создаем именовоный кортеж "лист" "узел"
# используются в класе HaffmanCode
Leaf = namedtuple("Leaf", 'key, value')
Node = namedtuple("Node", 'value, left, right')


class HaffmanCode:

    def __init__(self):
        # создаем таблицу кодов по Хаффману
        # используется в функции recursive_tree_traversal
        self.haffman_code_table = dict()
        # основной список для формирования листьев->дерева
        self.data_list = []

    def _make_leafs_list(self, string):
        # создаем счетчик символов в строке и сортируем его
        self.sort_counter = sorted(Counter(string).items(),
                                   key=lambda k: k[1], reverse=True)
        # формируем список "листев"
        for k, v in self.sort_counter:
            # добавляем лист в список
            self.data_list.append(Leaf(k, v))
        # выводим на экран
        # print(data_list)

    def _make_tree(self):
        # Формируем дерево созданием узлов для дерева
        # print(data_list)
        while len(self.data_list) >= 2:
            # формируем переменные
            left, right = self.data_list.pop(), self.data_list.pop()
            # создаем узел из сформированых переменных left, right
            node = Node(left.value + right.value, left, right)
            # print(data_list)
            # добавляем созданый узел обратно с наш список
            self.data_list.append(node)
            # сортируем наш список по атрибуту value
            # необходимо что бы у объектов Leaf, Node были атрибуты value
            self.data_list = sorted(self.data_list,
                                    key=lambda k: k.value,
                                    reverse=True)
            # print(node)
            # print(f"{'*' * 50}\n{self.data_list}\n{'*' * 50}")

    def _recursive_tree_traversal(self, data: Node, code=''):
        """Рекурсивный обход построенного дерева
        с созданием таблицы кодов по Хаффману"""
        # если поданный объект имеет тип Node то формируем код
        if isinstance(data, Node):
            # print(data)
            self._recursive_tree_traversal(data.left, code=f'{code}0')
            self._recursive_tree_traversal(data.right, code=f'{code}1')
        # если поданный объект имеет тип Leaf
        # то записываем code в таблицу кодов
        elif isinstance(data, Leaf):
            # print(data)
            self.haffman_code_table[data.key] = code

    def _encode_string(self, string):
        """Кодирование введенной строки по таблице кодов по Хаффману"""
        h_list = []
        for itm in string:
            h_list.append(self.haffman_code_table[itm])
        return ' '.join(h_list)

    def get_haffman_code_table(self):
        if self.haffman_code_table:
            return self.haffman_code_table
        return False

    def haffman_encode(self, string):
        """Основной метод который вызывает внутрение методы HaffmanCode"""
        self._string = string
        self._make_leafs_list(string)
        self._make_tree()
        self._recursive_tree_traversal(*self.data_list)
        encode_string = self._encode_string(string)
        return encode_string


if __name__ == '__main__':
    string = input('Введите строку для кодирования: ')
    haffman = HaffmanCode()

    print(f'Закодированная строка:\n'
          f'{haffman.haffman_encode(string)}\n\n'
          f'Таблица кодирования по Хаффману:\n'
          f'{haffman.get_haffman_code_table()}')
