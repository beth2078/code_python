# Remove Duplicates from a string

def remove_duplicates(a_list):
    ''' a function that is used to maintain a signle copy of each unique values in a list

    argument
        a_list: a list of various objects

    result
        new_list: containing all unique values 
    '''
    new_list = []

    for item in a_list: 
        if item not in new_list:
            new_list.append(item)
        
    return new_list
# end of remove_duplicates

test = ["a", "b", "b", "c", "c", "b", "c", "a", "a", "d"]
print(f'test list: {test}')
print(f'duplicates removed: {remove_duplicates(test)}')