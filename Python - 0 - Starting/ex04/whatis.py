import sys

def odd_or_evenn(object: int) -> str:
    if object % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"

if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            try:
                print(odd_or_evenn(int(sys.argv[1])))
            except ValueError:
                raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)
