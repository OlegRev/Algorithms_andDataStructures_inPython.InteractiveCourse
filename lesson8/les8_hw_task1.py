"""
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?

Примечание. Решите задачу при помощи построения графа.
"""
from collections import deque


def get_handshake_graph(number_of_friends: int = 0,
                        edge_list: bool = False):
    # Ввод количества друзей встречи
    number_of_friends = int(input('Введите количество друзей на встрече: '))
    # бызовый случай
    if number_of_friends < 2:
        return 'Нет друзей, нет рукопожатий'

    # количество вершин графа рукопожатий (количество друзей)
    handshake_v = deque([_ for _ in range(number_of_friends)])
    # создаем масив для хранени списка рёбер
    handshake_edge_list = []

    # заполнение списка рёбер
    for friend_n in range(number_of_friends):
        # выбор вершины(друга)
        curent_v = handshake_v.popleft()
        # создания граней(рукопожатий) вeршины(выбранного друга) для графа
        handshake_friend = [(curent_v, handshake) for handshake in handshake_v]
        # расширение списка граней
        handshake_edge_list.extend(handshake_friend)

    # если флаг edge_list == True
    if edge_list:
        # вернуть список граней
        return handshake_edge_list
    else:
        # иначе вернуть строку с указанием количества граней(рукопожатий)
        return (f'Количество рукопожатий на встрече {number_of_friends}'
                f' друзей:\t{len(handshake_edge_list)}')


print(get_handshake_graph())
print(get_handshake_graph(edge_list=True))
