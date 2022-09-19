class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node


class LinkedList:

    def __init__(self, data):
        self.head = Node(data)


    def append(self, data):
        #head가 None일때 head에 데이터를 넣어준다.
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next  is not None:
            cur = cur.next
        cur.next = Node(data)
    #head 가 None일 경우 None 에는 next 라는 경우가 없어 에러가 발생한다.
    #head -> -> -> -> -> -> -> None
    #None이 될때까지 이동

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()


