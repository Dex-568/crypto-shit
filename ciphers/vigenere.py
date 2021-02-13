import itertools
import string


def vigenerecipher(enc, text, key):
    print("1. Encrypt?\n2. Decrypt?")

    if enc is True:
        # make it easier on myself
        text = text.replace(" ", "")
        text = text.upper()

        ciphertext = ''

        msgkey_tuple = list(zip(text, itertools.cycle(key)))

        # encrypts each letter individually and sticks them into a list
        # to be joined
        for letter, keyletter in msgkey_tuple:
            alphabet = string.ascii_uppercase
            shift = alphabet.find(keyletter.upper())
            new_alphabet = alphabet[shift:] + alphabet[:shift]
            table = str.maketrans(alphabet, new_alphabet)

            ciphertext += letter.translate(table)

        return ciphertext

    else:

        text = text.replace(" ", "")
        text = text.upper()

        plaintext = ''

        msgkey_tuple = list(zip(text, itertools.cycle(key)))

        # does the exact opposite, practically a reverse lookup
        for letter, keyletter in msgkey_tuple:
            alphabet = string.ascii_uppercase
            shift = alphabet.find(keyletter.upper())
            new_alphabet = alphabet[-shift:] + alphabet[:-shift]
            table = str.maketrans(alphabet, new_alphabet)

            plaintext += letter.translate(table)

        return plaintext
