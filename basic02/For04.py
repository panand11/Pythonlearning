"""
***Nested for loop***
Outer for loop
for element in sequence:
    inner for loop body
    for element in sequence:
        body of inner for loop
    body of outer for loop
"""

for i in range(1,11):
    for j in range(1,11):
        print(i * j, end = '\t')        # inner for loop body
    print('\n')                       # outer for loop body