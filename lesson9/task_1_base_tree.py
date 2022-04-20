from binarytree import tree, bst, Node, build
# pip install binarytree


class MyNode:
    '''
    Класс структуры 'дерева'
    '''
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print('a', a, sep='\n')

b = bst(height=3, is_perfect=True)
print('b', b, sep='\n')

c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
c.left.left.left = Node(0)
c.left.left.right = Node(2)
c.left.right.left = Node(4)
c.left.right.right = Node(6)
c.right.left.left = Node(8)
c.right.left.right = Node(10)
c.right.right.left = Node(12)
c.right.right.right = Node(14)
print('c', c, sep='\n')

d = build([7, 3, 11, 1, 5, 9, 3, None, 2, None, 6, 8, 10, 12, 14])
print('d', d, sep='\n')
