class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, root):
        self.root = root

    #Add at head
    def addAtHead(self, node):
        node.next = root
        self.root = node
    
    #Add at index
    def addAtIndex(self, root, index, node):
        iter = 1
        curr = root
        while iter < index - 1:
            curr = curr.next
            iter += 1

        node.next = curr.next
        curr.next = node


    #Add the provided element to the last
    def addAtLast(self, root, node):
        curr = root

        while curr.next != None:
            curr = curr.next

        curr.next = node
    
    #Delete at head
    def deleteAtHead(self):
        self.root = self.root.next

    #Delete element from the linked list at any index
    def delete(self, root, index):
        iter = 1
        curr = root

        while iter < index - 1:     #get to the prev node
            iter +=  1
            curr = curr.next

        curr.next = curr.next.next
        print()

    #Print the complete list
    def printList(self):
        curr = self.root
        while curr != None:
            print(curr.data, end = " > ")
            curr = curr.next

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
node4 = Node(00)
node5 = Node(99)

ll = LinkedList(root)
ll.addAtLast(root, node1)
ll.addAtLast(root, node2)
ll.addAtLast(root, node3)
print("List created")
ll.printList()
ll.delete(root, 2)
print("Node deleted at 2")
ll.printList()
ll.addAtHead(node4)
print("Add at Head")
ll.printList()
ll.deleteAtHead()
print("\nHead deleted")
ll.printList()
ll.addAtIndex(root, 3, node5)
print("\nAdded at 2")
ll.printList()

ll.addAtHead(Node(100))
ll.printList()