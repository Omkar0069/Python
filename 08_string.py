a = 'Omkar' #Single quoted string
a = "Omkar" #Double quoted string
a = '''Omkar''' #Triple quoted string usually used for big paragraphs

#String slicing
name = "Yenaswamimuthhaswamirenubalgopaliyer"
#nameshort = name[0:4] #Start from 0 = 'Y' including all the way to index 4 excluding 4
nameshort = name[-12:-1] #negative slicing
print(nameshort)
print(name[0: ]) # Is same as print(name[0:37]) mean till end

#Slicing using skip value
Name = "Yenaswamimuthhaswamirenubalgopaliyer"
print(Name[0:24:2]) # In range from 0 to 24 print value with the gap of 2 like skip 2 including the first print 3rd and so on
