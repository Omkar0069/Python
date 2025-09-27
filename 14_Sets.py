Emptyset = set() # Method of writing Emptyset 
print(type(Emptyset))
Set = {
    1,2,34,5,5,
}
print(Set)  # Sets dont repeat same no.
Set.remove(2)
print(Set)

# # PROPERTIES
# Sets are unordered -> Elements order doesnt matter
# Sets are unindexed -> Cannot access element by index
# There is no way to change item in sets
# Does not contain Duplicate values


#TYPES IN SETS
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}
print("Union of s1 and s2 is",s1.union(s2))
print("Intersection of s1 and s2 is",s1.intersection(s2))
print("Difference of s1 and s2 is",s1.difference(s2))
print({1,2,3}.issubset(s1))
print({1,2,3,4,5,6,7}.issuperset(s1))