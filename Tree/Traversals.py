class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Preorder",end=": ")
preorder(root)
print("\nInorder",end=": ")
inorder(root)
print("\nPostorder",end=": ")
postorder(root)