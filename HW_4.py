# бинарное дерево с балансировкой, добавление, удалением элементов

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# определяем высоту правого поддерева и левого
class Height:
    def __init__(self):
        self.height = 0


# определяем сбалансированное дерево или нет
def TreeBalanced(root):
    left_height = Height()
    right_height = Height()
    if root is None:
        return True
    return ((abs(left_height.height - right_height.height) <= 1) and TreeBalanced(root.left) and TreeBalanced(
        root.right))


# Рекурсивная функция для вставки значения
def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


# Функция удаления значения
def deleteNode(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left and root.right:
            predecessor = findMaximumKey(root.left)
            root.data = predecessor.data
            root.left = deleteNode(root.left, predecessor.data)
        else:
            child = root.left if root.left else root.right
            root = child
    return root


# отсортируем для наглядности
def order(root):
    if root is None:
        return
    order(root.left)
    print(root.data, end=' ')
    order(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

if TreeBalanced(root):
    print('Сбалансированное бинарное дерево!')
else:
    print('Не сбалансированное бинарное дерево!')



lst_data = [3, 1, 5, 2, 4, 6, 7]

root = None
for data in lst_data:
    root = insert(root, data)

root = deleteNode(root, 2)
print(lst_data)
order(root)