#coding=GBK
def Bubble(nums):
    n=len(nums)
    for i in range(n-1):
        flag=0
        for j in range(n-i-1):
            if nums[j]<nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                flag=1
        if flag==0:
            break
    return nums

x=input()
nums=[int(n) for n in x.split()]
print(Bubble(nums))