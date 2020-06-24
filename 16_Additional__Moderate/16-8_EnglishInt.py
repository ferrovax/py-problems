# 16.8 English Int

smalls = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

suffixes = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion"]

def english(num):
    if num == 0:
        return smalls[0]
    elif num < 0:
        return "negative " + english(num * -1)

    str, index = [], 0

    while num > 0:
        if num % 1000 != 0:
            str.append(suffixes[index])
            str.append(words(num % 1000))

        index += 1
        num //= 1000

    str.reverse()

    return " ".join(str)

def words(num):
    str = []

    if num >= 100:
        str.append(smalls[num // 100] + " hundred")
        num %= 100

    if num >= 10 and num <= 19:
        str.append(smalls[num])
    elif num >= 20:
        str.append(tens[num // 10])
        num %= 10

    if num >= 1 and num <= 9:
        str.append(smalls[num])

    return " ".join(str)
