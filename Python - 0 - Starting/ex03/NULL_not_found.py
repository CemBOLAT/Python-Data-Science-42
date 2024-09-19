
def NULL_not_found(object: any) -> int:
    if object is None and type(object) == type(None):
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and type(object) == float:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    elif isinstance(object, bool) and object == False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0



""""
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
"""