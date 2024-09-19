ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!" # subscriptable
ft_tuple = ("Hello", "Türkiye!") # immutable
ft_set.remove("tutu!")
ft_set.add("Kocaeli!")
ft_dict["Hello"] = "42Kocaeli!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Expected output:
'''
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
'''
