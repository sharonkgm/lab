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
def deletion(node, value):
    if root is None:
        return root
    if value<node.value:
        node.left = deletion(node.left, value)
    elif value>node.value:
        node.right = deletion(node.right,value)
    else:
        #node have one child or no child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        #node have two child
        temp = successor(root.right)
        node.value = temp.value
        node.right = deletion(node.right, temp.value)
    preorder(root)



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
n = int(input("enter a element to delete :"))
search(root,element)
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
print(f"after deletion of {n} , the preorder traversal is : ")
deletion(root,n)
