class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def isCycle(head):
    p1 = head
    p2 = head
    while p2 != None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


def LengthofCycle(head):
    p1 = head
    p2 = head
    count = 0
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:

            count=1
            p1=p1.next
            p2=p2.next.next
            while p1!=p2:
                p1=p1.next
                p2=p2.next.next
                count+=1
            return count
    return count


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None
print(isCycle(node1))
print(LengthofCycle(node1))
