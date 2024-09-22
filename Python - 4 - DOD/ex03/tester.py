from new_student import Student

try:
    print("Correct init")
    student = Student(name="Edward", surname="agle")
    print(student)
except TypeError as e:
    print(f"TypeError: {e}")

try:
    print("Wrong initialization")
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print(f"TypeError: {e}")
