from math import gcd


def affinecipher(enc, text, a, b):
    cipherarray = []

    if gcd(a, 26) != 1:
        return False

    text = text.replace(" ", "")
    text = text.lower()

    textarray = [char for char in text]
    if enc is True:

        for ele in textarray:
            # get the corresponding number (not ascii) from the letter
            x = ord(ele) - 97

            # ax+b mod 26
            y = ((a * x) + b) % 26

            # revert the letter back to its ascii equivalent
            y += 97
            cipherarray.append(chr(y))

        return ''.join(cipherarray)
    else:

        for ele in textarray:
            x = ord(ele) - 97

            # find the modular multiplicative inverse of a
            c = pow(a, -1, 26)

            # c(x-b) mod 26
            y = c * (x - b) % 26

            y += 97
            cipherarray.append(chr(y))
        return ''.join(cipherarray)
