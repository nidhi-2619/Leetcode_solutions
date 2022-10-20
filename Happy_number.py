 def isHappy(self, n: int) -> bool:
        seen = set()
        set is use to avoid the duplicacy
        while n not in seen:
            seen.add(n)
#             to calculate the further number
            n = sum([int(x) **2 for x in str(n)])#n will be the new number and we are doing this because square of 1 is 1 then we will out of loop 
        return n == 1
