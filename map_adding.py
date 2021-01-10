#adding in map
l=["apple","tom","tom","dog"]
d={}
for x in sorted(l):
    d[x]=d.get(x,0)+1
print(d)