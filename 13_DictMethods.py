marks = {
    "Omkar": 100,
    "Harshal": 96,
    "Aaron": 95,
    "Sumeet": 98,
}

print(marks.items()) 
print(marks.keys())
print(marks.values())
marks.update({"Omkar": 99, "Ritesh": 100}) # Mutable and can also add new items
print(marks)
print(marks.get("Aaron2")) # Get marks of Aaron, prints 'None'
print(marks["Aaron2"]) # Return Error
