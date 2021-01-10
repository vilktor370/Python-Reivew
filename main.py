#adding in map
l=["apple","tom","tom","dog"]
d={}
for x in l:
    d[x]=d.get(x,0)+1

for x in d:
    print(x,d[x])
print("\n")
for k,v in d.items():
    print(k,v)
print("\n")