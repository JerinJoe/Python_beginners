#cant modify tuples

# tuple1=('History','math','phy','compsci')
# tuple2=tuple1

# print(tuple1, tuple2)

# tuple1[0]='Art'
# print(tuple1, tuple2)


#sets
# unordered and no duplicates

cs_course= {'History','math','phy','compsci'}
art_course= {'History','math','art','design'}

print(cs_course.intersection(art_course))

print(cs_course.difference(art_course)) 

print(cs_course.union(art_course))


#empty list
empl1=[]
empl2=list()

#empty tuple
empt1=()
empt2=tuple()

#empty sets

emps={}# its a dict
emps=set()
