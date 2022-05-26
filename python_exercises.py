# Given a blob of text, determine if a specific string of text can be created from that blob of text
# blob_of_text = "hello my name is david.  what is your name?"
blob_of_text = "hello my name is david.  what is your name?"
# string_to_find = "david"
string_to_find = "david"
TextBlob(blob_of_text).words.extract(string_to_find)
"""
Two words are anagrams of each other if they contain the same combination of characters,
including counts, but regardless of order.  "BEAR" and "BARE" are anagrams of each other, but
"ARREAR" and "RARE" are not.
Write a function that accepts as input a list of strings and partitions that list into
groups, such that all strings in a group are anagrams of each other.  For example, given
the input list ["add", "cab", "ad", "abc", "dad"], your function should determine that
"add" and "dad" are in one group, "cab" and "abc" another, and "ad" is in a group on its own.
Please use whatever programming language you prefer to solve this problem.
"""
list_of_words = ["add", "cab", "ad", "abc", "dad"]


def group_anagrams(words: list) -> list:
    """
    >>> group_anagrams(list_of_words)
    [['add', 'dad'], ['cab', 'abc']]
    """
    # create a dictionary of anagrams
    anagrams = {}
    for word in words:
        # sort the word
        sorted_word = "".join(sorted(word))
        # if the sorted word is in the dictionary, append the word to the list
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        # if the sorted word is not in the dictionary, create a new key value pair
        else:
            anagrams[sorted_word] = [word]
    # return the dictionary's values
    return list(anagrams.values())


print(group_anagrams(list_of_words))
