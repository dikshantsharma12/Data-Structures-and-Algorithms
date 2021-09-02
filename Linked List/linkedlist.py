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


firstNode=Node("Dikshant")
linkedList=LinkedList()
linkedList.insert(firstNode)
firstNode=Node("aman")

linkedList.insert(firstNode)
firstNode=Node("ritik")
linkedList.insert(firstNode)
firstNode=Node("xyz")
linkedList.insertAtHead(firstNode)
firstNode=Node("xyz1")
linkedList.insertAtHead(firstNode)
firstNode=Node("xyz2")
linkedList.insertbetween(firstNode,1)
linkedList.deletenode(2)
linkedList.printlist()

