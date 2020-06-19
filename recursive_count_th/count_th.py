'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# PSEUDO CODE:
#   1. Check if the word is more than 2 letters.
#   2. else check if the "th" is in the 2 first letters and add 1 to the count
#   3. else remove the first letter and repeat with the remaining


def count_th(word):
    # Check if the word has less than 2 letters. If it's not, not possible to find "th" inside
    if len(word) < 2:
        return 0

    # If the 2 first letters at "th" add 1 to the count and count the remaining letters
    else:
        if word[0:2] == "th":
            return 1 + count_th(word[2:])
        # remove the first letter and repeat with the remaining until it finds "th"
        else:
            return count_th(word[1:])


print(count_th("thunderthstothrm"))