#Sum of N
# n = int(input("Enter the number: "))
# i = 0
# sum = 0
# while(i<=n):
#     sum+=i
#     i+=1

# print(sum)

#Factorial of N
# n = int(input("Enter the number: "))
# i = 1
# f = 1
# for i in range(1, n+1):
#     f = f*i
#     i+=1
# print(f"Factorial of {n} is {f}")




# Patterns
""""
1. Print the following pattern n = 3
  * 
 ***
*****
"""
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

""""
2. Print the following pattern n = 3
* 
**
***
"""
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     #print(" "*(n-i), end="")
#     print("*"*(i), end="")
#     print("")


""""
3. Print the following pattern n = 3
***
* *
***
"""

n = int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n ):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")


