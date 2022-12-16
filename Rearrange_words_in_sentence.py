#Given a sentence text (A sentence is a string of space-separated words) in the following format:

#First letter is in upper case.
#Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

#Return the new text following the format shown above.


class Solution:
    def arrangeWords(self, text: str) -> str:
        #converting the string to list
        words = text.split()
        # sorting the list by the length
        words = sorted(words,key=len)
        #converting the list back to string
        s = ' '.join(words)
        #returning the string with first letter capitalize
        return s.capitalize()
