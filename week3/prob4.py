# 定义单链表的节点
class linknode:
    def __init__(self, val):
        # 实例化单链表的类时：定义两个成员变量：一个是head指针，一个是节点存储的值
        self.val = val
        self.next = None


# 定义单链表类：并定义单链表的成员函数：增删改查
class linklist:
    def __init__(self):
        self.head = None

    # 初始化单链表
    def init_linklist(self, data):
        self.head = linknode(data[0])  # 创建头节点，头节点的值存放data的第0个元素
        r = p = self.head
        for i in data[1:]:
            node = linknode(i)
            p.next = node
            p = p.next
        return r

    # 判断单链表是否为空
    def is_empty(self):
        return self.head == None

    # 获取单链表的长度
    def length(self):
        count = 0
        cur = self.head  # 定义游标
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 遍历整个链表
    def travel(self):
        cur = self.head  # 定义游标
        while cur != None:
            print(cur.val, end=' ')
            cur = cur.next

    # 单链表查询指定元素x所在的位置
    def search(self, x):
        cur = self.head  # 定义游标
        count = 1
        while cur != None:
            if cur.val == x:
                return count
            else:
                cur = cur.next
                count += 1
        return "无"


    # 单链表表头增加元素x
    def insert_to_head(self, x):
        node = linknode(x)
        node.next = self.head
        self.head = node

    # 单链表末尾增加元素x
    def insert_to_end(self, x):
        node = linknode(x)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # 单链表指定位置添加元素x
    def insert_to_index(self, x, pos):
        if pos <= 0:
            self.insert_to_head(x)
        elif pos > (self.length() - 1):
            self.insert_to_end(x)
        else:
            cur = self.head
            count = 0
            node = linknode(x)
            while count < pos - 1:  # 从0开始，循环结束后 cur指向 要插入元素的上一个节点
                count += 1
                cur = cur.next
            node.next = cur.next  # 先：新的节点的next指向原来该位置的节点，再：当前节点的next指向新的节点
            cur.next = node

    def inserti(self, choice):
        if choice == 1:
            x = int(input("请输入要添加的数字："))
            self.insert_to_head(x)
            n.append(x)
        elif choice == 2:
            x = int(input("请输入要添加的数字："))
            self.insert_to_end(x)
            n.append(x)
        elif choice == 0:
            print("取消增加操作")
            self.travel()
        else:
            x = int(input("请输入要添加的数字："))
            y = int(input("请输入要添加的位置："))
            self.insert_to_index(x, y)
            n.append(x)




    def remove(self, element):
        """删除指定元素"""
        cur, prev = self.head, None
        while cur is not None:
            if cur.val == element:
                if cur == self.head:  # 如果该节点是头结点
                    self.head = cur.next
                else:
                    prev.next = cur.next
                break
            else:
                prev, cur = cur, cur.next
        return cur.val


    def modify(self, pos, element):
        """修改指定位置的元素"""
        cur = self.head
        if pos < 0 or pos > self.length():
            return False
        for i in range(pos - 1):
            cur = cur.next
        cur.val = element
        return cur




if __name__ == '__main__':
    l = linklist()
    n = list(map(int, input("请输入链表：").split()))
    for value in n:
        l.init_linklist(n)
    print("链表是否为空？", l.is_empty())
    l.travel()
    print("\n头部插入请输入1；尾部插入请输入2；指定位置请输入3；取消操作请输入0：")
    a = int(input())
    l.inserti(a)
    l.travel()
    print("\n请输入要查找的数字：")
    index1 = int(input())
    print(l.search(index1))
    l.travel()
    print("\n请输入要删除的某个值对应的节点：")
    index2 = int(input())
    if index2 in n is True:
        l.remove(index2)
        l.travel()
        n.remove(index2)
    else:
        print("该数字不存在")
        l.travel()
    print("\n请输入要修改的位置和值：")
    index3 = int(input("位置："))
    index4 = int(input("值："))
    if index3 <= len(n):
        print(l.modify(index3, index4))
        l.travel()
    else:
        l.insert_to_end(index4)
        l.travel()




