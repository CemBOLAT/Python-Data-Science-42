import sys


def analyze_text(text: str) -> None:
    """
    Parameters:
        text: str -> text to analyze
    Returns:
        None
    Description:
        This function takes a string as an argument and \
            prints the number of characters in the string.
        It also prints the number of uppercase letters, lowercase letters,\
            digits, spaces, and punctuation characters in the string.
    """
    txt_properties = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "space": 0,
        "digit": 0
    }
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in text:
        if char.isupper():
            txt_properties["upper"] += 1
        elif char.islower():
            txt_properties["lower"] += 1
        elif char.isdigit():
            txt_properties["digit"] += 1
        elif char.isspace():
            txt_properties["space"] += 1
        elif char in punctuation_characters:
            txt_properties["punctuation"] += 1
        else:
            pass

    print(f"The text contains {len(text)} characters:")
    print(f"{txt_properties['upper']} upper letters")
    print(f"{txt_properties['lower']} lower letters")
    print(f"{txt_properties['punctuation']} punctuation marks")
    print(f"{txt_properties['space']} spaces")
    print(f"{txt_properties['digit']} digits")


def main():
    """
    Parameters:
        None
    Returns:
        None
    Description:
        This function is the main function that\
            takes care of the program's logic.
    Logic:
        If the number of arguments is more than 2,\
            it raises an AssertionError.
        If the number of arguments is 2, it calls the analyze_text\
            function with the second argument as the text to analyze.
        If the number of arguments is 1, it asks the\
            user to input the text to analyze.

    Raises:
        AssertionError: If the number of arguments is more than 2.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            analyze_text(sys.argv[1])
        elif len(sys.argv) == 1:
            try:
                text = input("What is the text to count?\n")
                text += '\r'
                analyze_text(text)
            except EOFError:
                pass
            except KeyboardInterrupt:
                pass
    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)


if __name__ == "__main__":
    main()
