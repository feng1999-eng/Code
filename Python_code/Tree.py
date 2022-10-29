#coding=GBK
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # 将新值与父节点进行比较
        if self.data:  # 非空
            if data < self.data:            #新值较小，放左边
                if self.left is None:       #若空，则新建插入节点
                    self.left = Node(data)
                else:                       #否则，递归往下查找
                    self.left.insert(data)
            elif data > self.data:          #新值较大，放右边
                if self.right is None:      #若空，则新建插入节点
                    self.right = Node(data)
                else:                       #否则，递归往下查找
                    self.right.insert(data)
        else:
            self.data = data                

    # 打印这棵树，中序遍历
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()
    def PrintPre(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.PrintPre(root.left)
            res=res+self.PrintPre(root.right)
        return res
    def PrintBack(self,root):
        res=[]
        if root:
            res=res+self.PrintBack(root.left)
            res=res+self.PrintBack(root.right)
            res.append(root.data)
        return res
    def layerPrint(self,root):
        temp=[]
        res=[]
        temp.append(root)
        while len(temp)>0:
            TEMP=temp.pop(0)
            res.append(TEMP.data)
            if TEMP.left:
                temp.append(TEMP.left)
            if TEMP.right:
                temp.append(TEMP.right)
        return res
# 使用insert方法添加节点
str=input()
data=[int(n) for n in str.split()]
root=Node(data[0])
for i in data[1:]:
    root.insert(i)
root.PrintTree()
print("*"*50)
Pre=root.PrintPre(root)
for i in Pre[:]:
    print(i)
print(root.PrintBack(root))
print(root.layerPrint(root))