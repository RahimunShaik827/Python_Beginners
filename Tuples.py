# predefined class
# list/collection of data type
# immutable (....,.....,,,,,,)


t1=()
t2=tuple()
t3=(11,2,33)
t4=(True,34,45,22,13,"XYZ")
print(type(t1),type(t2),type(t3),type(t4))
q=list(t3)

# q.sort()
print(q,type(q))
q.sort()
print(q)
print(t4[0])
print(t4[-1])
print(t4[2:5:-1])
print(t4[5:2:-1])

# additional functions in tuple 1.count() 2.index()
# tuple allow deep copy not shallow copy

a=10
t=tuple((a,))
print(t,type(t))