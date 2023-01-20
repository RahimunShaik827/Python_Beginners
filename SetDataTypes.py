# store multiple data types either same/different type or both type with unique values
# set data types-->to store multiple values either of same type or different type/both with uniqu values
# 2 types
# 1. set {mutable and immutable}
# 2. frozenset [immutable]

# a) set==================================================================================================
#predefined class 
# syntax==> setobj={val1,val2, , , }
# empthy set setobj=set()
#set belongs to both mutable[in the case add()] and immutable[~item assignment]

set1={1,2,3}
print(set1,type(set1))

s2={"cse","s/w",34,22}
print(s2,type(s2),id(s2))

# set1[0]=100 bsz set obj is not subscriptable
set1.add(1.3)
print(set1)

s3=set()
print(s3,type(s3),id(s3))

# 1)add
# syntax setobj.add(element)

s1={10,"runi"}
print(s1,type(s1),id(s1))
s1.add("javi")
s1.add("moon")
s1.add("zoo")
print(s1)

# 2)clear(): remove all elements set obj
# syntax->setobj.clear()
#set doent support deletion

s1={23,"sita"}
print(s1,len(s1))
s1.clear()
print(s1,len(s1))

# 3)remove():remove specified element from set object
# syntx:--> setobj.remove(element)
s1={"mo","hi",22}
print(s1,len(s1))
s1.remove("hi")
print(s1,len(s1))

# 4)discard():--same as remove but if elemt not there not remove/no error will returns
# syntax:-setobj.discard(element)
s1={"mo","hi",22}
print(s1,len(s1))
s1.discard("heroo")
print(s1,len(s1))

# 5)pop(): remove any arbitary element from set object[key error on empty set]
# syntx:-->setobj.pop()
set1={3+5j,1,2,3,4,"fgf","fgd"}
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)

# 6)copy(): content of one obj to anoter obj[shallow copy]
# syntx: setobj2=setobj1.copy()
s1={1,2,3}
s2=s1.copy()
print(s1,s2)
s1.add("s1")
print(s1,s2)

# Deep copy
s1={"python"}
s2=s1
print(s1,s2)
s1.add(".py")
print(s1,s2)

# 7)isdisjoint(): common elemts it returns [False] else it returns[True]
# syntx:setobj1.isdisjoint(setobj2)
# issuperset set1==set2 return True -->syntx:setobj1.issuperset(setobj2)
# issubset set1==set2 return True -->syntx:setobj1.issubset(setobj2)
#union syntx: setobj3=setobj1.union(setobj2)
# intersection():-->setobj3=setobj1.intersection(setobj2)
# difference removes common elements:-->setobj3=setobj1.difference(setobj2)
# Symentric difference return notcommon elements:-->setobj3=setobj1.symmetric_difference(setobj2)
s1={1,2,3}
s2={4,5}
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.issubset(set()))
print(set().issubset(set()))
print(s1.union(s2))
print(s1|s2)
s3={1,2}.union({3,4})
print(s3)
setobj1={100,200}
setobj2={11,22,100}
setobj3=setobj1.intersection(setobj2)
print(setobj3)
print(setobj1&setobj2)
print(setobj1.difference(setobj2))
print(setobj2.difference(setobj1))
print(setobj1-setobj2)
print(setobj2.symmetric_difference(setobj1))
print(setobj1^setobj2)
# =========================================================================================================

# b)frozenset
# predefined class , set data type ,store multiple value/same type/different type/both with unique Value
# syntx:--> frozensetobj=frozenset(collection type obj)
# no insertion order, no indexing & slicing
# same as set but immutable doesnt support item assignment  & add()

s1={1,2,3,"moooon"}
fs=frozenset(s1)
print(fs,type(fs))
# fs[0],fs[0:1],fs.add(10) doesnt wrk bcz immutable
# functions avalable in frozenset union(),intersection(),difference(),symmetric_difference(),issuperset(),issubset(),isdisjoint()

