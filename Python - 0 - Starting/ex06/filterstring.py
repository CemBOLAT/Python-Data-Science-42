from ft_filter import ft_filter
import sys


def filterString(s: str, n: int):
    words = s.split()
    res = list(ft_filter(lambda word: (len(word) > n), words))
    print(res)


def main():
    try:
        try:
            if len(sys.argv) != 3:
                raise AssertionError("bad number of arguments")
            string = str(sys.argv[1])
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)

    filterString(string, number)


if __name__ == "__main__":
    main()