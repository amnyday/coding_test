def solution(my_string, indices):
    lst = list(my_string.strip())  # Convert string to list
    for idx in sorted(indices, reverse=True):  # Iterate over indices in reverse order
        lst.pop(idx)  # Pop the element at the given index
    return ''.join(lst)  # Join the list back into a string and return