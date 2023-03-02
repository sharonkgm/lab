#creating class for node
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#insertion
def insert(node,value):
    if node is None:
        return Node(value)
    if value<node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

#traversal
def preorder(root):
    if root is not None:
        print(root.value,end ="->")
        preorder(root.left)
        preorder(root.right)
def inorder(root):
     if root is not None:
         inorder(root.left)
         print(root.value,end ="->")
         inorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end ="->")

#searching
def search(root,element):
    if root.value == element:
        print("element is present")
        return
    if element<root.value:
        if root.left:
            search(root.left,element)
        else:
            print("empty node")
    else:
        if root.right:
           search(root.right,element)
        else:
            print("empty node")

#finding successor
def successor(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

#deletion
def deletion(root, value):
    if root is None:
        return root
    if value<root.value:
        root.left = deletion(root.left, value)
    elif value>root.value:
        root.right = deletion(root.right,value)
    else:
        #node have one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            #node have two child
            temp = successor(root.right)
            root.value = temp.value
            root.right = deletion(root.right, temp.value)

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
element = int(input("enter element to search :"))
search(root,element)
n = int(input("\nenter a element to delete :"))

print('\n')
print("preorder traversal is :")
preorder(root)
print('\n')
print("inorder traversal is :")
inorder(root)
print('\n')
print("postorder traversal is :")
postorder(root)
print('\n')
deletion(root,n)
print(f"node {n} deleted")

