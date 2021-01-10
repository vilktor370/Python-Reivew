#adding in map
l=["apple","tom","tom","dick"]
d={}
for x in l:
    d[x]=d.get(x,0)+1
print(d)