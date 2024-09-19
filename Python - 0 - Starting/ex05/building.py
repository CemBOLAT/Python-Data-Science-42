import sys

# doc var!

def analyze_text(text: str) -> None:
    txt_properties = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "space": 0,
        "digit": 0
    }

    for char in text:
        if char.isupper():
            txt_properties["upper"] += 1
        elif char.islower():
            txt_properties["lower"] += 1
        elif char.isdigit():
            txt_properties["digit"] += 1
        elif char == ' ' or char == '\r':
            txt_properties["space"] += 1
        else:
            txt_properties["punctuation"] += 1
    
    print(f"The text contains {len(text)} characters:")
    print(f"{txt_properties['upper']} upper letters")
    print(f"{txt_properties['lower']} lower letters")
    print(f"{txt_properties['punctuation']} punctuation marks")
    print(f"{txt_properties['space']} spaces")
    print(f"{txt_properties['digit']} digits")

def main():
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
