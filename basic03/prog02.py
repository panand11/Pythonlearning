#slicing in Python
''' u can return a range of characters in a string using slicing in python
specify the start index and end index sperated by colon to indicate the range of slicing'''

str = "PYTHON"
print(str[1:4])
print(str[:3])
print(str[2:])
print(str[-4:-2])

str1="Good vibes only"
print(str1[2:9:3]) #syntax: [start:stop:increment step]