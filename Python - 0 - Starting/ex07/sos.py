import sys

def decode(s: str) -> None:
    NESTED_MORSE = { " ": "/ ",
                    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
                    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
                    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
                    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
                    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
                    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
                    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
                    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
            }
    string = ""
    for c in s:
        if c.upper() in NESTED_MORSE:
            string += NESTED_MORSE[c.upper()]
        else:
            raise AssertionError("the arguments are bad")
    print(string.strip())
    

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("bad number of arguments")
        decode(sys.argv[1])
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
        return

if __name__ == "__main__":
    main()