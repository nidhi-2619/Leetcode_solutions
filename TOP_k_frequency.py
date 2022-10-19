 # Word as key and its frequency in words as value
        dictionary = {}
        # Finding the word count and storing in dictionary
        for word in words:
            if word in dictionary: dictionary[word] += 1
            else: dictionary[word] = 1
        # Converting the dictionary into list of tuples using dictionary.items()
        # Using Lambda function to sort that tuple, first using Word count using 
        # -word[1]. Why -word[1] but not word[1] is we want to sort in descending 
        # order according to word count. For words having count same we have to sort
        # them lexographically so we next add word[0]. That is the use of
        # (-word[1], word[0]). 
        dictionary = sorted(dictionary.items(), key = lambda word: (-word[1], word[0]))
        # Using List Comprehension and creating a list with words from dictionary till
        # k length
        return [word[0] for word in dictionary[:k]]
