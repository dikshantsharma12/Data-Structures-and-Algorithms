from linkedlist import Node,LinkedList
def reverse_node(head,k):
    if head==None:
        return None
    prev=None
    current=head
    next=None
    count=1
    while current!=None and count<=k:
        next = current.next
        current.next=prev
        prev=current
        current=next
        count=count+1
    if next !=None:
        head.next=reverse_node(next,k)

    return prev



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
k=2
linkedList.head=reverse_node(linkedList.head,k)
linkedList.printlist()