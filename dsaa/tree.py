from typing import Any, List


class TreeNode:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def __repr__(self) -> str:
        return f'<{self.data} Tree[{self.children}]>'

    def add_childs(self, *childs: List) -> None:
        for child in childs:
            self.add_child(child)

    def add_child(self, child) -> None:
        if not isinstance(child, TreeNode):
            raise TypeError('TreeNode child must be another instance of TreeNode.')
        child.parent = self
        self.children.append(child)

    def add_parent(self, parent) -> None:
        if not isinstance(parent, TreeNode):
            raise TypeError('TreeNode parent must be another instance of TreeNode.')
        parent.add_child(self)

    def get_level(self) -> int:
        level = 0
        parent = self.parent
        while parent is not None: # count the parents to get level
            level += 1
            parent = parent.parent
        return level


def build_products_tree():
    tree = TreeNode('Electronics')
    laptops = TreeNode('Laptops')
    phones = TreeNode('Phones')
    tree.add_childs(laptops, phones)
    macbook = TreeNode('MacBook')
    dell = TreeNode('Dell')
    laptops.add_childs(macbook, dell)
    samsung = TreeNode('Samsung')
    iphone = TreeNode('iPhone')
    phones.add_childs(samsung, iphone)
    print(tree)
    print(iphone.get_level())
    print(phones.get_level())
    print(tree.get_level())


if __name__ == '__main__':
    build_products_tree()
