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

# 첫번째와 두번째 사이에 넣고 싶으면 
#   사이를 끊어 줘야함   
# [첫번째]  [두번째]  [세번째]
#   node    next_node 에 값 저장
#     [세로운 값]   new_node에 저장
#   node.next 값에 next_node에 저장 
#   node.next 에 new_node를 저장
#   new_node.next = next_node 를 저장

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        #index 번째에 새로운 원소값 추가
        
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return
    
    def delet_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next

        return
    


linked_list = LinkedList(2)
linked_list.append(12)
linked_list.append(5)
# [5] ->[12] -> [8]
linked_list.add_node(3,7)
linked_list.delet_node(2)

print(linked_list.print_all())