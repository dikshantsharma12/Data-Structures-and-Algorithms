class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def LCA(root,n1,n2):
    if root==None:
        return None
    if root.data==n1 or root.data==n2:
        return root

    left=LCA(root.left,n1,n2)
    right= LCA(root.right,n1,n2)
    if left!=None and right!=None:
        return root

    if left==None and right==None:
        return None
    if left !=None:
        return LCA(root.left,n1,n2)
    return LCA(root.right,n1,n2)
def findDist(root,k,dist):
    if root==None:
        return -1
    if root.data==k:
        return dist
    left=findDist(root.left,k,dist+1)
    if (left!=-1):
        return left
    return findDist(root.right,k,dist+1)
def DistancebetweenNodes(root,n1,n2):
    lca=LCA(root,n1,n2)
    d1=findDist(lca,n1,0)
    d2=findDist(lca,n2,0)

    return d1+d2

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)


print(DistancebetweenNodes(root,4,5))
