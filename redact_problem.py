def redact_words(words, banned_words):
    '''Takes in 2 array inputs words and banned_words
    Output is a new array of words without the words found in banned words
    Time complexity: O(n)
    '''
    banned_words_set = set(banned_words) # I create a set of banned_words because searching a set is constant time
    difference = [] # create a new array to store our values
    for word in words: # iterate over words
        if not word in banned_words_set: # if the word is not in set_banned_words
            difference.append(word) # append the word to difference
    return difference # once the loop is complete we can return what we've collected