# coding=GBK
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class CreateStack(object):
    def __init__(self):
        self.head = Node()

    def isempty(self):
        return self.head.next is None

    def init_stack(self, data):
        P = self.head
        for i in data[0:]:
            node = Node(i)
            node.next = P.next
            P.next = node

    def Push(self, item):
        node = Node(item)
        node.next = self.head.next
        self.head.next = node

    def Pop(self):
        if self.isempty():
            print("Stack is None")
            return -1
        else:
            Temp = self.head.next
            self.head.next = Temp.next
            return Temp.data


str = input()
data = [int(n) for n in str.split()]
S1 = CreateStack()
S1.init_stack(data)
First = S1.head.next
while First != None:
    print(First.data)
    First = First.next
S1.Push(6)
print(S1.Pop())
