from collections import deque
from string import ascii_lowercase
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		#Code here
		q = deque()
# 		first step is the startword
		q.append((startWord,1))
# 		declare set to check if the word in set 
        s = set(wordList)
        while q:
            word,steps = q.popleft()
            # check if we have encounter the Targetword
            if word==targetWord:return steps
            # go through each letter of word
            for i in range(len(word)):
                for char in ascii_lowercase:
                    new_word = word[:i]+char+word[i+1:] 
                    if new_word in s:
                        s.remove(new_word)
                        q.append((new_word,steps+1))
        return 0            
                    


#{ 
 # Driver Code Starts
# from collections import deque 
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
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends
