#!/usr/bin/python2.7
from collections import OrderedDict
from timeit import Timer

sequential_search = """
def search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found
"""

ordered_sequential_search = """
def search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos = pos+1
    return found
"""

binary_search_iterative = """
def search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
                last = midpoint - 1
        else:
            first = midpoint + 1
    return found
"""

binary_search_recursive = """
def search(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    elif item < a_list[midpoint]:
            return search(a_list[:midpoint], item)
    else:
        return search(a_list[midpoint + 1:], item)
"""
        
create_list = """
from random import sample
my_list = sorted(sample(range(100000), $size))
"""        

def main():
    # Create the sorted lists.
    sizes = [500, 1000, 10000]
    
    # Time the searches.
    algorithms = OrderedDict([
        ("Sequential Search",         sequential_search),
        ("Ordered Sequential Search", ordered_sequential_search),
        ("Iterative Binary Search",   binary_search_iterative),
        ("Recursive Binary Search",   binary_search_recursive),
    ])
    for algorithm, definition in algorithms.iteritems():
        for size in sizes:
            setup = definition + create_list.replace("$size", str(size))
            times = Timer("search(my_list, -1)", setup=setup).repeat(100, 1)
            time = sum(times) / len(times)
            print "%s took %.3E seconds to run for %d elements, on average" % (algorithm, time, size)
            
if __name__ == "__main__":
    main()