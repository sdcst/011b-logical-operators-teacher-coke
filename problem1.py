#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

i = int(input("Enter a number: "))
i1 = i % 6
i2 = i % 8
if i1 == 0 and i2 != 0:
    print(f"{i} is true")
else:
    print(f"{i} is not true")


