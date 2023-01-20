# dict: to share the data in the form of key[unique],Value[may/not unique]
# syntx:--> dictobj1={key1:val1,key2:val2,...}
# inserion order
# no indexing/slicing bcz we have values of keys for accessig values of values
# dict-->mutable
# values of keys-->immutable
# values of values -->mutable
# two types of dict objs 
# 1. Empty dict-----with o keys,values, len=0 : syntx:-->  dictobj={}/ dictobj=dict()

d1={}
d2=dict()
print(d1,type(d1),d2,type(d2))
d1[1]="name"
d1[2]='adrs'
d1["num"]=3
print(d1)

# 2.Non-Empty dict
# syntx of non empty
# dictobj[key1]=valu1
# dictobj[key-n]=val-n
d1={1:"rahim",2:"karim",3:"yes"}
print(d1)
d1[4]="no"
print(d1)

# predefined operations in dict
# 1.clear()   removes all elements    dictobj.clear() 
# 2. copy()   copy one dict obj to another dict   dictobj2=dictobj1.copy()
# 3. get()    getting the key value      dictobj.get(key)
# 4. pop()    remove the key& val         dictobj.pop(key)
# 5. popitem()    removing last item          dictobj.popitem()
# 6. keys()          return only keys             dictobj.keys()
# 7. values()         return all values       disctobj.values()
# 8. items()          return all keysand vals     dictobj.items()
# 9. update()          union of d1 & d2         d1.update(d2)

print(d1.clear())
d1={1:"a",2:"b"}
d2=d1.copy()
print(d2)

