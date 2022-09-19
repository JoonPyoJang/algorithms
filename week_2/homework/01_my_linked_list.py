# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
#[6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때, 
                  # 끝에서 2번째 값은 7을 반환해야 합니다!
#마지막 None 까지의 리스트를 확인하고 거기서 뒤로 N번째 만큼 움직이기
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

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        count = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            count +=1
        answer = self.head
        for _ in range(count-k):
            answer=answer.next

        return answer

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
