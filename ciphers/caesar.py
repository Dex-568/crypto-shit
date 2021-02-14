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

            text = text.replace(" ", "")
            text = text.upper()

            # expected percentage values of letters in the english language
            # find more accurate values?
            expectedpercentage_eng = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022,
                                      'G': 0.020, 'H': 0.061, 'I': 0.070,
                                      'J': 0.002, 'K': 0.008, 'L': 0.040, 'M': 0.024, 'N': 0.067, 'O': 0.075,
                                      'P': 0.019, 'Q': 0.001, 'R': 0.060,
                                      'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.010, 'X': 0.002, 'Y': 0.020,
                                      'Z': 0.001}

            chisquared = 0
            expectedpercentage_cipher = {}
            chi_list = []
            # the longer the ciphertext, the lower the chi squared value

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

            for prob_cipher in results:
                prob_cipher = prob_cipher.replace(" ", "")

                cipherlen = len(prob_cipher)

                for letter, value in expectedpercentage_eng.items():
                    expectedvalue = cipherlen * value

                    expectedpercentage_cipher.update({letter: expectedvalue})

                    actualcount = prob_cipher.count(letter)

                    letterstat = (actualcount - expectedvalue) ** 2
                    letterstat = letterstat / expectedvalue

                    chisquared += letterstat

                chi_list.append(chisquared)
                chisquared = 0
            return results, chi_list


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
