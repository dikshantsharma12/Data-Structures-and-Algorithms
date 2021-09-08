class Node:
    def __init__(self,data):
        self.data=data
        self.children = []
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.chidren.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces=" "* self.get_level()*3
        prefix=spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def Tree():
    root=Node("Electronics")

    laptop=Node("Laptop")
    laptop.add_child(("Mac"))
    laptop.add_child(("Dell"))
    laptop.add_child(("Lenovo"))

    cellphone=Node("Cell Phone")
    cellphone.add_child(("iPhone"))
    cellphone.add_child(("Mi"))
    cellphone.add_child(("Samsung"))

    tv=Node("Laptop")
    tv.add_child(("LG"))
    tv.add_child(("Sony"))
    tv.add_child(("Realme"))
        
    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)

    return root

root=Tree()
