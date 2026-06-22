class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new = Node(value)

        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new

    def middle_node(self):
        p1 = self.head
        p2 = self.head

        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next

        return p1.data
ll = LinkedList()

n = int(input("How many nodes? "))

for i in range(n):
    num = int(input("Enter value: "))
    ll.add_node(num)

print("Middle element is:", ll.middle_node())