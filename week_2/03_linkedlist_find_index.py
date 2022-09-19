class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

#
    def add_node(self, index, value):
        #index 번째에 새로운 원소값 추가
        new_node = Node(value)
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        
        return


linked_list = LinkedList(2)
linked_list.append(12)
linked_list.append(5)
# [5] ->[12] -> [8]
linked_list.add_node(3,7)

print(linked_list.print_all())