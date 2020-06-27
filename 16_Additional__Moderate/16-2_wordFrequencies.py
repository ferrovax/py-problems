# 16.2 Word Frequencies

# Solution for single query:
def getFrequency(book, word):
    word = word.strip().lower()
    count = 0

    for i in range(len(book)):
        if book[i].strip().lower() == word:
            count += 1

    return count

# ------------------------------------------------------------------------------

# Solution for multiple queries:
def getFrequencies(book):
    frequencies = {}

    for word in book:
        word = word.lower()

        if word.strip() != "":
            if word not in frequencies.keys():
                frequencies[word] = 0
            frequencies[word] += 1

    return frequencies

def getFreq(dict, word):
    if not dict or not word:
        return -1

    word = word.lower()

    if word in dict.keys():
        return dict[word]

    return 0
