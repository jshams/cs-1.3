def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    pat_len = len(pattern)
    list_of_indexes = []
    for i in range(0, len(text) - len(pattern) + 1):
        print(pattern, text[i : i + pat_len] )
        if pattern == text[i : i + pat_len]:
            list_of_indexes.append(i)
    return list_of_indexes
