def wordPattern(pattern: str, s: str) -> bool:
    lst = s.split()
    if len(pattern) != len(lst):
        return False
    char_to_word_map = {}
    word_to_char_map = {}
    for char, word in zip(pattern, lst):
        if (char in char_to_word_map and char_to_word_map[char] != word) or (word in word_to_char_map and word_to_char_map[word] != char):
            return False

        char_to_word_map[char] = word
        word_to_char_map[word] = char

    return True
