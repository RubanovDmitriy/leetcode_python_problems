import pytest


def find_words(words: list[str]) -> list[str]:
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    result = []
    for word in words:
        letter_map = dict()
        for letter in word:
            if letter not in letter_map:
                letter_map[letter.lower()] = 1
            else:
                letter_map[letter.lower()] += 1

        for row in rows:
            if all(x in row for x in list(letter_map.keys())):
                result.append(word)

    return result


@pytest.mark.parametrize(
    "words, output",
    [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
        (["omk"], []),
        (["adsdf", "sfd"], ["adsdf", "sfd"]),
    ],
)
def test_find_words(words, output):
    assert find_words(words) == output
