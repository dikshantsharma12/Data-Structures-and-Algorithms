class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,newnode):
        if self.head==None:
            self.head=newnode
            return
        temp=self.head
        while (temp.next!=None):
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp   
    def insertAtHead(self,newnode):
        self.head.prev=newnode
        if self.head==None:
            newnode.next=self.head
        self.head=newnode

    def display(self):
        temp=self.head
        while(temp.next!=None):
            print(temp.data,end="->")
            temp=temp.next
        print("NULL")
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
linkedList.display()
