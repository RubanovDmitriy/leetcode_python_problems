def unique_morse_representations(words: list[str]) -> int:
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    morse = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
    mapa = {x[0]: x[1] for x in zip(alphabet, morse)}

    res = []
    for word in words:
        word_srt = ""
        for letter in word:
            word_srt += mapa[letter]

        res.append(word_srt)

    return len(set(res))


assert unique_morse_representations(["gin", "zen", "gig", "msg"]) == 2
assert unique_morse_representations(["a"]) == 1
