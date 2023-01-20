# store multiple values
# 2 types--list[mutable/changed], tuple[immutable/cannt change]
# 2 types of list objs-->Empty, Non Empty list
# Empty list-->length=0-->Syntax-->listobj=[], listobj=list()


#Empty List
l1=[]
print(l1)

#Non Empty List

ls=[1,2,1,3,"rahimun","hacker"]
print(len(ls),type(ls))


#list

# Indexing----- Slicing

# predefined functions in list
# 1.append()
# 2.insert()
# 3.clear()
# 4.remove()
# 5.pop()
# 6.pop(index)
# 7.count()
# 8.index()
# 9.reverse()
# 10.copy()--shallow copy, Deep copy
# 11.sort()
# 12. extend()

# innner/nested list----

# In inner list we can apply slicing and all the methods

l1=[1,"rahim",[1,2,3],[4,5,6],"moon"]
print(l1)
print(l1[2])
print(l1[2][1])
print(l1[3][::2])
print(l1[2][-2:])
l1[2].append(22)
print(l1)
l1[2].insert(1,100)
print(l1)
l1[2].sort()
print(l1)
l1[2].sort(reverse=True)
print(l1)
