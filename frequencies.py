"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    #extend the code, such that it produces a dictionary based on the items list. For each item in items, the dictionary must contain a key. If the item is not a string, the key must be the item converted to a string. The value must be a positive integer counting the number of times the item represented by the key occurs in items.
    #For example, frequencies(['a', 'a', 'b', 'b', 'b', 'c']) must return the following dictionary: { 'a': 2, 'b': 3, 'c': 1 }
    #For example, frequencies([100, 'Hello', '100', '100', 100]) must return the following dictionary: { '100': 4, 'Hello': 1 }

    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    
    return frequencies
