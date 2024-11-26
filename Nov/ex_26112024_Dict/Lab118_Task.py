# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=False))

print(sorted_dict)