
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None

    def __str__(self) -> str:
        return self.data


class LinkedList:

    first_node = None

    def find(self, data) -> Node:
        node = self.first_node
        while node:
            if node.data == data:
                return node
            node = node.next_node
        return None

    def get(self, index: int) -> Node:
        node = self.first_node
        count = 0
        while node:
            if count == index:
                return node
            node = node.next_node
            count += 1
        if node is None:
            raise IndexError(f'No node in linked list at index {index}.')

    def all(self) -> None:
        node = self.first_node
        while node:
            print(node)
            node = node.next_node

    def append(self, node: Node) -> None:
        if not self.first_node:
            self.first_node = node
        else:
            _node = self.first_node
            while _node:
                if _node.next_node is None:
                    _node.next_node = node
                    break
                _node = _node.next_node


ll = LinkedList()
ll.append(Node('junior'))
ll.append(Node('junior adv'))
ll.append(Node('semi senior'))
ll.append(Node('semi senior adv'))
ll.append(Node('senior'))
print(ll.get(2))
print(ll.find('juniors'))
