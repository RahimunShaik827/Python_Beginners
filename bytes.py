# Bytes must be in range(0,256)

a=[1,2,3,0,255]
b=bytes(a)
print(b,type(b))

# Error 
# a=[-10,2,3,0,256]
# b=bytes(a)
# print(b,type(b))

for x in b:
    print(x)

print(b[0])
print(b[0:4])

for x in b[0:4]:
    print(x)