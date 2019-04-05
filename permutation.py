def permutations(array):
    if len(array) < 2:
        return array
    if len(array) == 2:     # base case
        return [array, [array[1], array[0]]]
    all_perms = []
    for i in array:
        new_array = []
        new_array.extend(array)
        new_array.remove(i)
        all_perms_extension = permutations(new_array)
        for group in all_perms_extension:
            group.insert(0,i)
        all_perms.extend(all_perms_extension)
    return all_perms
    
print(permutations([1,2,3]))