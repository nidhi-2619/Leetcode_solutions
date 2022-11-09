class Solution:
    def findCombination(self,index,target,arr,ans,ds):
        # base case
        if index==len(arr):
            if target==0:
                # copy is used so that new ds can be created else ds will take the reference only and no new ds will be created
                ans.append(ds.copy())
            return 
#  the intuition is pick and not pick the element 
        # picking up the element
        if arr[index]<=target:
            ds.append(arr[index])
            # recursive call for making all possible picks 
            self.findCombination(index,target-arr[index],arr,ans,ds) 
            # removing the element so non pick part case be done
            ds.pop()
        self.findCombination(index+1,target,arr,ans,ds)        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        ans = []
        ds = []
        self.findCombination(0,target,candidates,ans,ds)
        return ans
   
