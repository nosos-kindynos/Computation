from math import factorial
mapping={}
n=40
for i in range(1,n+1):
    k=[]
    for j in range(1,n+1):
        if j!=i:
            k.append(j)
    mapping.update({i:k})

s=0
for i in range(n-1):
    s+=factorial(n)/factorial(n-i)
print(int(s))
#find_all_possible_paths(1, 2, mapping)

