#!/usr/bin/python2.7
from collections import OrderedDict
from timeit import Timer

insertion_sort = """
def sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
"""

shell_sort = """
def sort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)


      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
"""

python_sort = """
def sort(a_list):
    a_list.sort()
"""
        
create_list = """
from random import sample
my_list = sample(range(100000), $size)
"""        

def main():
    # Create the sorted lists.
    sizes = [500, 1000, 10000]
    
    # Time the sorts.
    algorithms = OrderedDict([
        ("Insertion Sort", insertion_sort),
        ("Shell Sort",     shell_sort),
        ("Python Sort",    python_sort),
    ])
    for algorithm, definition in algorithms.iteritems():
        for size in sizes:
            setup = definition + create_list.replace("$size", str(size))
            times = Timer("sort(my_list)", setup=setup).repeat(100, 1)
            time = sum(times) / len(times)
            print "%s took %.3E seconds to run for %d elements, on average" % (algorithm, time, size)
            
if __name__ == "__main__":
    main()