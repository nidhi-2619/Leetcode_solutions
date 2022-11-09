class Solution:
    def findCombination(self,index,target,arr,ans,ds):
        # base case
        if index==len(arr):
            if target==0:
                # copy is used so that new ds can be created else ds will take the reference only and no new ds will be created
#                 the problem with my code was when index==n and target==0, I did ans.append(ds), the ans array is storing the reference of ds object. So, when ds changes in further recursions, the referenced  values in ans array also changes. So, I did ans.append(ds.copy()). Storing a copy for ds array so that I don’t lose that particular combination
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
   
