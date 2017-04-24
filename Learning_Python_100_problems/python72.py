###############################################################################################################
###################################################SREENIDHIN C C##############################################
###############################################################################################################

"""
Question:

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
"""

def bsearch(li,item,left,right):
    if left<right:
        mid = (left + right)/2
        if item == li[mid]:
            return mid
        elif item < li[mid]:
            return bsearch(li, item, left, mid)
        elif item > li[mid]:
            return bsearch(li, item, mid,right)
        return "not found"

li = [2,5,7,9,11,17,222]
x = int(raw_input("Enter the item to search: "))    
print bsearch(li, x, 0, len(li)-1)
