friends = [
    "Aaron",
    "Umar",
    "Sumeet",
    "Harshal",
    "Ritesh",
    10,
    69.6969,
    True,
]  # Can store any type of data like string, boolean, integer, etc
friends[4] = (
    "Laughing Ritesh"  # Unlike Strings lists Can modified or we can say they are mutable...
)
print(friends)
print(friends[0])
print(friends[0:5])

friends.append("Manan")  # Modifies the existing list and add "Manan" (append -> add)
print(friends)


# Another functions
l1 = [1, 34, 54, 12, 99, 87]
# l1.sort()
# l1.reverse()
# l1.insert(3, 45) #Used to insert values on users index(here it says that insert 45 after 3rd value)
# print(l1.pop(3)) #Remove the item on 3rd index
l1.remove(99)  # Removes particular item from the list(here removes 99)

print(l1)

# Note: Lists = Mutable | Strings = Immutable
