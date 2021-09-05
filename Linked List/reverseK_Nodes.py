from linkedlist import Node,LinkedList
def reverse_node(linkedList,k):
    prev=None
    current=linkedList.head
    count=0
    while current!=None and count<=k:
        nextptr = current.next
        current.next=prev
        prev=current
        current=nextptr
        count=count+1

    reverse_node()



nodeOne =Node(1)
nodeTwo=Node(3)
nodeThree =Node(6)
nodefour=Node(8) 
nodeFive =Node(9)
nodeSix=Node(7)
linkedList=LinkedList()
linkedList.insert(nodeOne)
linkedList.insert(nodeTwo)
linkedList.insert(nodeThree)
linkedList.insert(nodefour)
linkedList.insert(nodeFive)
linkedList.insert(nodeSix)
linkedList.printlist()
k=3
reverse_node(linkedlist,k)