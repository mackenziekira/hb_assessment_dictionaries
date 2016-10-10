"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""
from collections import Counter

def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    """
    # solution as a list comprehension on a set comprehension of the list
    # return [word for word in {word for word in words}]

    # more readable solution
    words = set(words)
    return list(words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # solution with set math 

    items1 = set(items1)
    items2 = set(items2)
    shared_words = items1 & items2
    return list(shared_words)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    negatives = {abs(num) for num in numbers if num <= 0}
    positives = {num for num in numbers if num >= 0}
    overlap = positives & negatives
    pairs = [[-num, num] for num in overlap]

    return sorted(pairs)


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """


    # make a word count dict

    word_count = {}
    for char in phrase:
        if char == " ":
            pass
        else:
            word_count[char] = word_count.get(char, 0) + 1

    # invert the word count dict so that the values (counts) are the keys and the keys (chars) are a list of values attached to the counts
    word_count_inv = {}
    {word_count_inv.setdefault(count, []).append(word) for word, count in word_count.iteritems()}

    # turn the inv dict into a sorted list, with highest frequency at the beginning
    ordered_counts = sorted(word_count_inv.iteritems(), reverse = True)

    # return the value (list of chars) associated with the highest frequency 
    return ordered_counts[0][1]



    # # an alternate way to complete the problem after turning the phrase into a word_count dict:

    # # turn the word_count dict into a list of tuples (word, count), and sort the list by counts

    # ordered_counts = sorted(word_count.items(), key = lambda x: x[1], reverse = True)
    
    # most_common_chars = []

    # # iterate through the (char, count) tuples until the count starts decreasing, then break

    # for index in xrange(len(ordered_counts)):
    #     char = ordered_counts[index][0]
    #     count = ordered_counts[index][1]
    #     previous_count = ordered_counts[index - 1][1]

    #     if most_common_chars == [] or count == previous_count:
    #         most_common_chars.append(char)
    #     else:
    #         break

    # return most_common_chars




    # solved using Counter class

    # char_count = Counter(phrase).most_common()
    # most_common_chars = []

    # for index in xrange(len(char_count)):
    #     char = char_count[index][0]
    #     count = char_count[index][1]
    #     prev_count = char_count[index - 1][1]
    #     if char == " ":
    #         pass
    #     elif most_common_chars == []:
    #         most_common_chars.append(char)
    #     elif count == prev_count:
    #         most_common_chars.append(char)
    #     else:
    #         break

    # return sorted(most_common_chars)


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
