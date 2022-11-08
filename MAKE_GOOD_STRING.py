class Solution:  
    def makeGood(self, s: str) -> str:
#       we will take a stack
        stack = []
        for i in range(len(s)):
#       if the element is present in the stack then we will match it will with the string letter ,if the letter is same as the letter in stack then we will
#  pop the element from the stack 
# swapcase is used to change the case to its opposite case
            if stack and stack[-1]==s[i].swapcase():
                stack.pop()
            else:
#            if the letter is not present in the stack then we will simply append it in the stack
                stack.append(s[i])
#    the stack will contain the elements which make the string good as all the upper case is used to remove the same lower case element
        return ''.join(stack)            


             
