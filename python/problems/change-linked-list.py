from linked_list import LinkedList

ll = LinkedList()
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.insert(2)
ll.insert(1)

#ll.printLinkedList()

node = ll.getRoot()
count = ll.getNodeCount()
print node.data
print count
