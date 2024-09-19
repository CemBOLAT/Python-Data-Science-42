
def all_thing_is_obj(object: any) -> int:
    if (type(object) == list):
        print(f"List : {type(object)}")
    elif (type(object) == tuple):
        print(f"Tuple : {type(object)}")
    elif (type(object) == set):
        print(f"Set : {type(object)}")
    elif (type(object) == dict):
        print(f"Dict : {type(object)}")
    elif (type(object) == str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42

#Write a function that prints the object types and returns 42.
"""
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
>
"""