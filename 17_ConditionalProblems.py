#PROBLEM 1:

# marks1 = int(input("Enter marks 1: "))
# marks2 = int(input("Enter marks 2: "))
# marks3 = int(input("Enter marks 3: "))

# Total_Percent = (marks1+marks2+marks3) / 300 * 100 

# if(Total_Percent >= 40 and marks1 and marks2 and marks3 >= 33):
#     print(f"You're Passed with {Total_Percent}%!")

# else:
#     print(f"You're Failed with {Total_Percent}%!")



#PROBLEM 2:
m = input("Enter your message: ")

p1 = "Spam"
p2 = "Click me!"
p3 = "Win Money"

if((p1 in m) or (p2 in m) or (p3 in m)):
    print("Spam Message!!")

else:
    print("Not a Spam Message")