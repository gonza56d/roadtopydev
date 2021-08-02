"""Max two childs per node."""

from typing import Any, List


class BinaryTreeSearchNode:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'{self.data} (L: {self.left}, R: {self.right})'

    def add_child(self, data) -> None:
        if self.data == data:
            return
        if self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeSearchNode(data)
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeSearchNode(data)

    def in_order_traversal(self) -> List:
        node = []

        if self.left:
            node += self.left.in_order_traversal()
        
        node.append(self.data)

        if self.right:
            node += self.right.in_order_traversal()
        
        return node

    def search(self, value) -> int:
        if value == self.data:
            return True
        if value < self.data:
            return self.left.search(value) if self.left else False
        elif value > self.data:
            return self.right.search(value) if self.right else False


root = BinaryTreeSearchNode(15)
root.add_child(2)
root.add_child(51)
root.add_child(13)
root.add_child(17)
root.add_child(21)
root.add_child(74)
root.add_child(3)
root.add_child(17)
root.add_child(4)
print(root)
print(root.in_order_traversal())
print(root.search(2))
