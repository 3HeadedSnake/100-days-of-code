# create the class Node and the attrbutes 
class Node:
    def __init__(self, letter):
        self.childleft = None
        self.childright = None
        self.nodedata = letter

# create the nodes for the tree
root = Node('A')
root.childleft = Node('B')
root.childright = Node('C')
root.childleft.childleft = Node('D')
root.childleft.childright = Node('E')

# In-order transversal
def InOrd(root):
    if root:
        InOrd(root.childleft)
        print(root.nodedata)
        InOrd(root.childright)
InOrd(root)

#Pre-order transversal
def PreOrd(root):
    if root:
        print(root.nodedata)
        PreOrd(root.childleft)
        PreOrd(root.childright)
PreOrd(root)

#Post-order transversal
def PostOrd(root):
    if root:
        PostOrd(root.childleft)
        PostOrd(root.childright)
        print(root.nodedata)
PostOrd(root)