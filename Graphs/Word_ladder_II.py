
# __________________Giving TLE on GFG and LEETCODE But good approach for explaining in interview__________________________

#User function Template for python3
from string import ascii_lowercase
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
from collections import deque
# this bfs will be different from standard bfs ,we'll be storing the 
# list to keep track of the sequence
class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #Code here
        # THE GIST OF THIS QUESTION IS THAT ,
        # UNLIKE PREVIOUS WORD LADDER WE WILL NOT ERASE/DELETE THE WORD FROM SET
        # WE WILL REMOVE THE WORD WHEN , ALL THE SEQUENCE OF THAT LEVEL IS COMPLETED 
        # REASON: There is a possibility that the word may appear in future sequence of same level for eg:
        #  bat->bot->pot->poz->coz
        #  bat->pat->pot->poz->coz
        #  both sequence are almost same but with just the difference of pat and bot
        # so we will del after we go through the pot for bat->bot and bat->pat
        q = deque()
        q.append([startWord])
        # to keep track of the words
        s = set(wordList)
        s.add(startWord)
        # initially we are at level 0
        level = 0
        ans = []
        lastUsed = []
        lastUsed.append(startWord)
        while q:
            sequence = q.popleft()
            # when length of sequence increase that means we reach to next level 
            #  then we can erase the word that has been visited or used
            if len(sequence)>level:
                # increase the level
                level+=1
                # erase from set
                for word in lastUsed:
                    s.remove(word)
                lastUsed.clear()    
            
            org_word  = sequence[-1]   
        # the first sequence where we reach the end word
        #  that length is the shortest length we can achieve
            if org_word==targetWord:
                if not ans:
                    ans.append(sequence)
        # all the sequence with same length will be included in the answer 
                elif len(ans[0])==len(sequence):
                    ans.append(sequence)    

            for i in range(len(org_word)):
                for ch in ascii_lowercase:
                    new_word = org_word[:i]+ch+org_word[i+1:]
                    if new_word in s:
                        # we will add the word in the sequence but for creating other sequence of same level we have to remove the new word so that for iteration we can add new words
                        sequence.append(new_word)
                        q.append(sequence)
                        # tell the level user that we have used which word 
                        lastUsed.append(new_word)
                        # del the new word
                        sequence.pop()
        return ans



        


#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends
