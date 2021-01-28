import Node

class BinarySearchTree:

    #Data members
    root = None

    #Constructor
    def __init__(self, root):
        self.root = root

    def print(self):
        currLvl = [self.root]
        nextLvl = []
        levelNum = 0
        while len(currLvl) != 0:
            for i in currLvl:
                if i.left != None:
                    nextLvl.append(i)
                if i.right != None:
                    nextLvl.append(i)

                print("\t"*levelNum, i.data)

            currLvl.clear()
            currLvl.extend(nextLvl)  
            nextLvl.clear()

#__main__

#Nodes
root = Node.DoubleNode(10)
node1 = Node.DoubleNode(20)
node2 = Node.DoubleNode(30)
node3 = Node.DoubleNode(40)

root.left = node1
root.right = node2
node1.left = node3

#Binary Search Tree
bst = BinarySearchTree(root)
bst.print()