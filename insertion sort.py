# -*- coding: utf-8 -*-
"""

Created on Fri Feb  7 21:44:52 2020

@author: Shouzeb
"""

# Insertion Sort In Python
#
# Performance Complexity = O(n^2)
# Space Complexity = O(n)

def insertionSortFunction(array):
    # for every element in our array
    for index in range(1, len(array)):
        current = array[index]
        position = index

        while position > 0 and array[position-1] > current:
            print("Swapped {} for {}".format(array[position], array[position-1]))
            array[position] = array[position-1]
            print(array)
            position -= 1

        array[position] = current

    return array
#unsorted array
array = [8,2,1,3,5,4180,0,150,80]
#to print sorted array
print(insertionSortFunction(array))