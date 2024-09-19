from ft_filter import ft_filter
import sys


def filterString(s: str, n: int):
    """
    Parameters:
        s: str -> string to filter
        n: int -> number of characters
    Returns:
        None
    Description:
        This function takes a string and a number as arguments.
        It splits the string into words and filters the words\
            that have more than n characters.
        It prints the list of words that have more than n characters.
    """
    words = s.split()
    res = list(ft_filter(lambda word: (len(word) > n), words))
    print(res)


def main():
    """
    This function is the main function of the program.

    Parameters:
        None
    Returns:
        None
    Description:
        This function is the main function of the program.
        It takes care of the program's logic.
    Logic:
        If the number of arguments is not 3, it raises an AssertionError.
        If the number of arguments is 3, it calls the filterString function\
            with the first argument as the string and the second argument\
                as the number.
    """
    try:
        try:
            if len(sys.argv) != 3:
                raise AssertionError("bad number of arguments")
            string = str(sys.argv[1])
            number = int(sys.argv[2])
            filterString(string, number)
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as err:
        print("AssertionError:", err)


if __name__ == "__main__":
    main()
