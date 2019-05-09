def permutations(array):
    if len(array) < 2:
        return array
    if len(array) == 2:     # base case
        return [array, [array[1], array[0]]]
    all_perms = []
    for i in array:
        new_array = array[:]
        new_array.remove(i)
        all_perms_extension = permutations(new_array)
        for group in all_perms_extension:
            group.insert(0,i)
        all_perms.extend(all_perms_extension)
    return all_perms

# f = open('/usr/share/dict/words' , 'r')
# words = f.readlines()
words = open('/usr/share/dict/words' ,'r').read().split('\n')
# f.close()
words = set(words)

def find_anagrams(word):
    word_split = [char for char in word]
    all_perms = permutations(word_split)
    all_perms_strings = [''.join(word) for word in all_perms]
    all_perms_set = set(all_perms_strings)
    return all_perms_set & words

def find_two_and_six_letter_word(letters):
    letters_split = [char for char in letters]
    all_perms = permutations(letters_split)
    all_perms_strings = [''.join(word) for word in all_perms]
    all_perms_set = set(all_perms_strings)
    print(all_perms_set)


if __name__ == '__main__':
    anagrams = find_anagrams("sokik")
    print(anagrams)
