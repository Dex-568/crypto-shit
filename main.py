import os

from ciphers.caesar import caesarcipher
from ciphers.vigenere import vigenerecipher
from ciphers.affine import affinecipher


# clears the screen
def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def main():
    # keep them hooked in
    exitcond = False
    while exitcond is False:
        try:
            menu = input("1. Caesar Cipher\n2. Vigenere Cipher\n3. Affine Cipher\n\n")

            if menu == "1":
                clear()

                encdec = input("1. Encrypt?\n2. Decrypt?\n\n")

                if encdec == "1":
                    text = input("Enter plaintext: ")
                    shift = int(input("Enter numerical shift: "))
                    if shift <= 0:
                        print("Shift cannot be a negative number!")
                        # cant reliably go back to the exact point so back to the main menu it is
                        pass
                    elif shift > 26:
                        print("Shift cannot be above 26!")
                        pass

                    enc = True

                    clear()
                    print("Given plaintext:", text)
                    print("Given shift:", shift)
                    print("Ciphertext output:", caesarcipher(enc, text, shift))

                    choice = input("\n1. Back to main menu\n2.Exit\n\n")

                    if choice == "1":
                        clear()
                        pass
                    else:
                        exitcond = True

                else:
                    enc = False
                    text = input("Enter ciphertext: ")

                    choice = input("1. Knowing the shift used.\n2. All possible combinations\n\n")

                    if choice == "1":
                        shift = int(input("Enter numerical shift: "))

                        print("Given ciphertext:", text)
                        print("Given shift:", shift)
                        print("Plaintext output:", caesarcipher(enc, text, shift))

                        choice = input("\n1. Back to main menu\n2.Exit\n\n")

                        if choice == "1":
                            clear()
                            pass
                        else:
                            exitcond = True

                    else:
                        shift = None

                        # the function returns a list of all possible combinations

                        result = caesarcipher(enc, text, shift)
                        # some probably abhorrent parsing of data but fuck it its late
                        result = zip(result[0], result[1])
                        result = list(result)

                        print("The Chi-Squared algorithm simply determines the best fit against most common english "
                              "letters.")
                        print("False positives can occur depending on the length of the ciphertext!")
                        print("The lower the number the better:\n")
                        for ele in result:
                            print(ele[0], ele[1])

                        choice = input("\n1. Back to main menu\n2.Exit\n\n")

                        if choice == "1":
                            clear()
                            pass
                        else:
                            exitcond = True

            elif menu == "2":
                clear()

                encdec = input("1. Encrypt\n2. Decrypt\n\n")

                if encdec == "1":
                    text = input("Enter plaintext: ")
                    key = input("Enter key to encrypt with: ")
                    enc = True

                    clear()
                    print("Given plaintext:", text)
                    print("Given key:", key)
                    print("Ciphertext output:", vigenerecipher(enc, text, key))

                    choice = input("\n1. Back to main menu\n2. Exit\n\n")

                    if choice == "1":
                        clear()
                        pass
                    else:
                        exitcond = True

                else:
                    enc = False
                    text = input("Enter ciphertext: ")

                    choice = input("1.Knowing the exact key used.\nOther cryptanalysis methods will come later\n\n")
                    if choice == "1":
                        key = input("Enter key used: ")

                        clear()
                        print("Given ciphertext:", text)
                        print("Given key:", key)
                        print("Plaintext output:", vigenerecipher(enc, text, key))

                        choice = input("\n1. Back to main menu\n2. Exit\n\n")

                        if choice == "1":
                            clear()
                            pass
                        else:
                            exitcond = True

            elif menu == "3":
                clear()

                encdec = input("1. Encrypt\n2. Decrypt\n\n")

                if encdec == "1":
                    enc = True

                    text = input("Enter plaintext: ")

                    print("This must be coprime to 26!")
                    a = int(input("Enter the a value: "))

                    b = int(input("Enter the b value: "))

                    clear()

                    if affinecipher(enc, text, a, b) is False:
                        print("\na not coprime with 26! Check number and try again\n\n")
                        pass

                    print("Given plaintext:", text)
                    print("Given a variable:", a)
                    print("Given b variable:", b)
                    print("Ciphertext output:", affinecipher(enc, text, a, b))

                    choice = input("\n1. Back to main menu\n2. Exit\n\n")

                    if choice == "1":
                        clear()
                        pass
                    else:
                        exitcond = True

                else:
                    enc = False

                    text = input("Enter ciphertext: ")

                    print("This must be coprime to 26!")
                    a = int(input("Enter the a value: "))

                    b = int(input("Enter the b value: "))

                    clear()

                    if affinecipher(enc, text, a, b) is False:
                        print("\na not coprime with 26! Check number and try again\n\n")
                        pass

                    print("Given ciphertext:", text)
                    print("Given a variable:", a)
                    print("Given b variable:", b)
                    print("Plaintext output:", affinecipher(enc, text, a, b))

                    choice = input("\n1. Back to main menu\n2. Exit\n\n")

                    if choice == "1":
                        clear()
                        pass
                    else:
                        exitcond = True

        except KeyboardInterrupt:
            print("Keyboard Interrupt received, exiting!")
            exit(0)


if __name__ == "__main__":
    main()
