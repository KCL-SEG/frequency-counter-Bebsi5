"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items = [str(i) for i in items]
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    
    return frequencies
