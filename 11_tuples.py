a = ()  # Empty Tuple
print(type(a))
b = (1, "Hello World", 69.96, "Fugga🎈", "Laughing Ritesh", "Sumeet Uncle")  # Tuple
print(type(b))

# Tuple Methods
no = b.count(1)  # Counts how many time 1 appeared
print(no)
i = b.index(69.96)  # Returns the position of 69.96
print(i)

# Note: Lists = Mutable | Tuples = Immutable
