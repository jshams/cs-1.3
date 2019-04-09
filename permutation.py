from random import randint
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
    
def generate_random_permutation(text):
    for index, char in enumerate(text):
        rando = randint(0, len(text) - 1)
        text[index], text[rando] = text[rando], text[index]
    return text

print(generate_random_permutation(['J','A','K','E']))
