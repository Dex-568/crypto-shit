import string


def caesarcipher(enc, text, shift):
    if enc is True:

        # fixes the problem of converting different ascii values depending on
        # lowercase or uppercase characters
        alphaupper = string.ascii_uppercase
        alphalower = string.ascii_lowercase

        # creates a rotated version of the alphabet using the shifts given
        rotupper = alphaupper[shift:] + alphaupper[:shift]
        rotlower = alphalower[shift:] + alphalower[:shift]

        # combines the two into strings the translation table can use
        combinedoriginal = alphalower + alphaupper
        combinedrotated = rotlower + rotupper

        trans_table = str.maketrans(combinedoriginal, combinedrotated)

        return text.translate(trans_table)

    else:
        if shift is None:

            results = []

            # should i really be initialising these each time? fuck it
            alphaupper = string.ascii_uppercase
            alphalower = string.ascii_lowercase

            # scale the whoooooooooooole alphabet
            for i in range(0, 26):
                rotupper = alphaupper[-i:] + alphaupper[:-i]
                rotlower = alphalower[-i:] + alphalower[:-i]

                combinedoriginal = alphalower + alphaupper
                combinedrotated = rotlower + rotupper

                trans_table = str.maketrans(combinedoriginal, combinedrotated)

                results.append(text.translate(trans_table))

            return results
            # should i go down the route of calculating the entropy of a string,
            # and determining the best possible, by human readable characteristics?
            # nah fuck it thats a story for another day

        else:
            # reversible algorithms make me happy

            alphaupper = string.ascii_uppercase
            alphalower = string.ascii_lowercase

            rotupper = alphaupper[-shift:] + alphaupper[:-shift]
            rotlower = alphalower[-shift:] + alphalower[:-shift]

            combinedoriginal = alphalower + alphaupper
            combinedrotated = rotlower + rotupper

            trans_table = str.maketrans(combinedoriginal, combinedrotated)

            return text.translate(trans_table)
