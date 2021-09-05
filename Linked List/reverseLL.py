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
    def reverse(self):
            # currNode=self.head
            # firstNode=currNode
            # firstNode.next=None
            # while True:
            #     if currNode.next==None:
            #         while True:

            #             self.head=currNode
            #             self.head.next=prevNode
            #             break
            #     prevNode=currNode
            #     currNode=currNode.next
            previousptr=None
            currptr=self.head
            nextptr=currptr.next
            
            while nextptr.next!=None:
                
                currptr.next=previousptr
                previousptr=currptr
                currptr=nextptr
                nextptr=nextptr.next
            self.head=currptr 
    def recusiveReverse(self):
        if self.head==None :
            return 
        newhead=recusiveReverse()
        self.head.next=self.head
        self.head.next=None

    def printlist(self):
        temp=self.head
        while True:
            if temp is None:
                break
            print(temp.data)
            temp=temp.next
node=Node(10)
linkedList=LinkedList()
linkedList.insert(node)
node=Node(20)
linkedList.insert(node)
node=Node(30)
linkedList.insert(node)
linkedList.recusiveReverse()
linkedList.printlist()