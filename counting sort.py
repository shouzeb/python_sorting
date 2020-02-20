# -*- coding: utf-8 -*-
"""

Created on Fri Feb  7 21:44:52 2020

@author: Shouzeb
"""

# counting Sort In Python
#
def get_sortkey(n):
    """ Define the method to retrieve the key """
    return n
 
def counting_sort(array, k, get_sortkey):
    """ Counting sort algo with sort in place.
        Args:
            tlist: target list to sort
            k: max value assume known before hand
            get_sortkey: function to retrieve the key that is apply to elements of tlist to be used in the count list index.
            map info to index of the count list.
        Adv:
            The count (after cum sum) will hold the actual position of the element in sorted order
            Using the above, 
 
    """
 
    # Create a count list and using the index to map to the integer in list.
    count_list = [0]*(k)
 
    # iterate the tgt_list to put into count list
    for n in array:
        count_list[get_sortkey(n)] = count_list[get_sortkey(n)] + 1 
 
    # Modify count list such that each index of count list is the combined sum of the previous counts
    # each index indicate the actual position (or sequence) in the output sequence.
    for i in range(k):
        if i ==0:
            count_list[i] = count_list[i]
        else:
            count_list[i] += count_list[i-1]
 
    output = [None]*len(array)
    for i in range(len(array)-1, -1, -1):
        sortkey = get_sortkey(array[i])
        output[count_list[sortkey]-1] = array[i]
        count_list[sortkey] -=1
 
    return output
 
## Create list for demo counting sort.
unsorted_list = [8,2,1,3,5,4180,0,150,80]
print("Unsorted List")
print(unsorted_list)
 
## Perform the counting sort.
print("\nSorted list")
output = counting_sort(unsorted_list, max(unsorted_list) +1, get_sortkey) # assumption is known the max value in list  for this case.
print(output)