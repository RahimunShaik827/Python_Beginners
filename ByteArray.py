# predefined class
# sequence daa type
# stores int data type range(0,256)
# mutable --changed
# convert -->bytearray()
# slicing,indexing possible
# insertion order
# Bytes[immutable]===bytearray[mutable]

"""
ba=[1,2,3,"Rahimun"]
print(ba,type(ba))
cba=bytearray(ba)--'str' object cannot be interpreted as an integer
print(cba,type(cba))

"""

ba=[1,2,3,True]
print(ba,type(ba))
cba=bytearray(ba)
print(cba,type(cba))

for x in cba:
    print(x)

