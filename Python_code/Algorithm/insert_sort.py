#coding=GBk
def insert_sort(li):
    length_li=len(li)
    for i in range(1,length_li):
        j=i-1
        temp=li[i]
        while j>=0 and temp<li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
    return li
A=[5,2,1,4,6,8,7,9,3]
print(insert_sort(A))

