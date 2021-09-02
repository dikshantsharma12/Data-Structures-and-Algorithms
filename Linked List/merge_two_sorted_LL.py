class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head==None:
            self.head = newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def insertAtHead(self,newNode):
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            self.head=newNode
            self.head.next=temp
            del temp
    def length(self):
        temp=self.head
        lengthll=0
        if self.head==None:
            return 0
        else:
            while True:
                if temp.next==None:
                    return lengthll
                temp=temp.next
                lengthll+=1
    def insertbetween(self,newNode,pos):
        if pos==1:
            self.insertAtHead(newNode)
            return
        if pos < 1 and pos>self.length():
            print("Invalid Statement")
            return
        currNode=self.head
        currPos=1
        while True:
            if currPos==pos:
                previousNode.next=newNode
                newNode.next=currNode
                break
            previousNode=currNode
            currNode=currNode.next
            currPos+=1

    def deletenode(self,pos):
        if self.head==None:
            print("No Element to Print")
            return
        if pos==1:
            todelete=self.head
            self.head=self.head.next
            del todelete
            return
        if pos<1 and pos>self.length():
            print("Invaling Position")
            return
        currPos=1
        currNode=self.head
        while True:
            if currPos==pos:
                todelete=currNode
                prevNode.next=currNode.next
                
                del todelete
                
                
                break
            prevNode=currNode
            currNode=currNode.next
            currPos+=1
    def printlist(self):
        temp=self.head
        while True:
            if temp is None:
                break
            print(temp.data)
            temp=temp.next

def merLinkedList(linkedlist1,linkedlist2,mergelist):
    currentFirst=linkedlist1.head
    currentSecond=linkedlist2.head
    while True:
        if currentFirst is None:
            mergelist.insert(currentSecond)
            break
        if currentSecond is None:
            mergelist.insert(currentFirst)
            break
        if currentFirst.data<currentSecond.data:
            currentFirstNext=currentFirst.next
            currentFirst.next=None
            mergelist.insert(currentFirst)
            currentFirst=currentFirstNext
        else:
            currentSecondNext=currentSecond.next
            currentSecond.next=None
            mergelist.insert(currentSecond)
            currentSecond=currentSecondNext



linkedList1=LinkedList()
linkedList2=LinkedList()
item=Node(1)
linkedList1.insert(item)
item=Node(2)
linkedList1.insert(item)
item=Node(3)
linkedList1.insert(item)
item=Node(4)
linkedList1.insert(item)

item=Node(3)
linkedList2.insert(item)
item=Node(5)
linkedList2.insert(item)
item=Node(7)
linkedList2.insert(item)
item=Node(9)
linkedList2.insert(item)

mergelist=LinkedList()
merLinkedList(linkedList1,linkedList2,mergelist)
mergelist.printlist()