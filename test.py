def contains(text, pattern):
    pat_len = len(pattern)
    for i in range(0, len(text) - len(pattern) + 1):
        print(pattern, text[i : i + pat_len] )
        if pattern == text[i : i + pat_len]:
            return True
    return False