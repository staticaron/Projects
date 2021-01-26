class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, root):
        self.root = root

    #Add the provided element to the last
    def addLast(self, root, node):
        curr = root

        while curr.next != None:
            curr = curr.next

        curr.next = node
    
    #Delete element from the linked list at any index
    def delete(self, root, index):
        iter = 1
        curr = root

        while iter < index - 1:     #get to the prev node
            iter +=  1
            curr.next

        curr.next = curr.next.next
        print()

    #Print the complete list
    def printList(self, root):
        curr = root
        while curr != None:
            print(curr.data, end = " -> ")
            curr = curr.next
        print()

    #Get the linked list as Simple list
    def getList(self, root):
        _list = []
        curr = root
        while curr != None:
            _list.append(curr.data)
            curr = curr.next

        return _list
#__main__
root = Node(10)
node1 = Node(28)
node2 = Node(38)
node3 = Node(48)

ll = LinkedList(root)
ll.addLast(root, node1)
ll.addLast(root, node2)
ll.addLast(root, node3)
ll.printList(root)
ll.delete(root, 2)
ll.printList(root)


