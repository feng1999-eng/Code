class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return i-1

作者：xiaoweixiang
链接：https://leetcode-cn.com/problems/B1IidL/solution/di-yi-xing-yuan-li-by-xiaoweixiang-64yq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        def get(i:int)->int:
            if i==-1 or i==n:
                return float('-inf')
            return arr[i]
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if get(mid-1)<get(mid)>get(mid+1):
                return mid
            elif get(mid-1)>get(mid):
                right=mid-1
            elif get(mid+1)>get(mid):
                left=mid+1
        return left