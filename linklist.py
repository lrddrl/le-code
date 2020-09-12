class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next = b
# b.next = c

# print(a.next.next. item)

def create_linklist(li):
    head = Node(li[0])
    print(Node(li[0]).item)
    for element in li[1:]:
        node = Node(element)
        print(node.item)
        node.next = head
        print(node.item)
        head = node
        print(node.item)
    return head

# 列表第一个元素是1，指针是0，
# 循环从第二个元素开始，值是2，指针是1
# node.item, next = Node(2).item, next
# 把第二个元素的头，从1夺过来，所以
# node.next = Node(1)
# 以此类推，3把头从2夺过来

lk = create_linklist([1,2,3])
print(lk.item)