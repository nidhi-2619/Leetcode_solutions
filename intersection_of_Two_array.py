class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = dict()
        ans = []
# 				count the occurence of number
        for i in nums1:
            n[i]=n.get(i,0)+1
# 			check if the number exist in second list and its count is greater than 0
        for i in nums2:
            if i in n and n[i]>0:
                ans.append(i)
                n[i]-=1 # this is to decrease the count after appending the element in the answer list
        return ans    
