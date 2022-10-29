class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class CreateQueue(object):
    def __init__(self):
        self.head=Node()
    def isempty(self):
        return self.head.next is None
    def InitializeQueue(self,data):
        P=self.head
        for i in data[0:]:
            node=Node(i)
            P.next=node
            P=node
str=input()
data=[int(n)for n in str.split() ]
Q1=CreateQueue()
Q1.InitializeQueue(data)
print(Q1.head.next.next.data)

