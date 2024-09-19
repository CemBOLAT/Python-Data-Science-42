import sys


def decode(s: str) -> None:
    """
    Parameters:
        s: str -> string to decode
        Returns:
            None
        Description:
            This function takes a string as an argument.
            It decodes the string into Morse code.
            It prints the decoded string.
        Raises:
            AssertionError: if the string contains non-ASCII characters
            AssertionError: if the string contains characters\
                that are not in the Morse code dictionary
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
        "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
        "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ",
        "3": "...-- ", "4": "....- ",
        "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. "
    }
    string = ""
    for c in s:
        if (not c.isascii()):
            raise AssertionError("the arguments are bad")
        if c.upper() in NESTED_MORSE:
            string += NESTED_MORSE[c.upper()]
        else:
            raise AssertionError("the arguments are bad")
    print(string.strip())


def main():
    """
    Parameters:
        None
    Returns:
        None
    Description:
        This function is the main function of the program.
        It takes care of the program's logic.
    Logic:
        If the number of arguments is not 2, it raises an AssertionError.
        If the number of arguments is 2, it calls the decode function\
            with the first argument as the string.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("bad number of arguments")
        decode(sys.argv[1])
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
        return


if __name__ == "__main__":
    main()
