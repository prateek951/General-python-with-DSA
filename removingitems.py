#  A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements

# Removing items from the list

def Remove(list):
    while list:
        list.pop()
        print(list)

initial_set = set([12,12,13,15,8,9])
Remove(initial_set)
    

