''' Data Input format:
    sources= # List of nodes #                                                                                                       eg [1,3,6....]
    target=    # Node Number #                                                                                                       eg    5
    mapping=   # Dictionary with key as node number and value as list of all first degree connected nodes#                           eg {1:[2,3],2:[1,4],3:[1,4],4:[2,3,5],5:[4]}
    risk_mapping = #  Dictionary with key as edge denoted by tuple of joint nodes and value as risk probability in decimal system #  eg  {(1,2):0.5 , (2,4):0.5 , (3,4): 0.5, (4,5): 0.5, (1,3):0.5 , }   
'''




import time
from functools import reduce
def estimate_risk(sources, target, mapping, risk_mapping,accuracy):

    from itertools import combinations
    import time
    import operator as op




    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom  # or / in Python 2
    
    
    
    
    def calculate_risk(risk_mapping):

        paths=[]
        for source in sources:
            relative_mapping = mapping.copy()
            for other_sources in sources:
                if other_sources != source:
                    relative_mapping.pop(other_sources)
            paths.extend(find_all_possible_paths(source, target, mapping,accuracy))
        n=len(paths)
        print(len(paths))
        print(paths)
        paths=convert_path_to_edges(paths)
        s=0
        p=3
        for i in range(1,n+1):
            s+=i*p*(ncr(n,i))
        k=s/(290000)
        print('estimated time is ',k)
        sum=0
        for i in range(1,len(paths)+1):
            print(i)
            sign = (-1)**(i+1)
            combos=list(combinations(paths,i))
            for j in combos:
                d=()
                for k in j:
                    d+=k
                d=distinct(d)
                intersection=1
                for t in d:
                    h = risk_mapping.get(t)
                    if h==None:
                        intersection *= risk_mapping.get((t[1],t[0]))
                    else:
                        intersection *= h
                sum+=(sign)*intersection
        return(sum)

    
    
    
    
    def convert_path_to_edges(paths):
        path_list=[]
        for path in paths:
            vertex_to_vertex=[]
            for i in range(len(path)-1):
                vertex_to_vertex.append((path[i],path[i+1]))
            path_list.append(tuple(vertex_to_vertex))
        return(path_list)

    
    
    
    
    def eq(x,y):
        x = list(x)
        y = list(y)
        x.sort()
        y.sort()
        if x==y:
            return(True)
        else:
            return(False)

   
    def distinct(x):
        k = []
        for i in x:
            append = True
            for j in k:
                if eq(i, j) == True:
                    append = False
            if append == True:
                k.append(i)
        return(k)

    
    
    
    
    def find_all_possible_paths(source,target,mapping,accuracy): # Uses depth first search to traverse graph
        
        paths=[]
        path=[source]
        visited={}
        for i in mapping:
            visited.update({i:[]})

        current=source
        while True:
            
            backtrack=True
        
            just_visited = []
            for vertex in mapping[current]:
                if vertex == target and vertex not in visited.get(current):
                    path.append(vertex)
                    k=path.copy()
                    paths.append(k)
                    path.remove(vertex)
                    just_visited=just_visited+[vertex]
                elif vertex not in path and vertex not in visited.get(current) and len(path)<accuracy:
                    path.append(vertex)
                    just_visited = just_visited+[vertex]
                    backtrack=False
                    break
                else:
                    pass
            
            just_visited = visited.get(current)+just_visited
            visited.update({current:just_visited})

            if current == source and eq(visited.get(source), mapping.get(source)):
                break
            if backtrack == True:
                path.remove(current)
                visited.update({current:[]})
                current=path[-1]
            else:
                current = vertex
            
            
        return(paths)


    
    
    
    
    
    return(calculate_risk(risk_mapping))


sources = [1]
target = 6
mapping = {1: [2, 3, 4, 5,6,7], 2: [1, 3, 4, 5,6,7], 3: [1, 2, 4, 5, 6,7],
           4: [1, 2, 3, 5, 6,7], 5: [1, 2, 3, 4,6,7], 6: [1,2,3, 4,5,7], 7:[1,2,3,4,5,6]}
risk_mapping = {(1, 2): 0.4, (1, 3): 0.4, (1, 4): 0.4, (1, 5): 0.4, (1, 6): 0.4, (2, 6): 0.4, (3, 6): 0.4,
                (5, 6): 0.4, (2, 3): 0.4, (2, 4): 0.4, (2, 5): 0.4, (3, 4): 0.4, (3, 5): 0.4, (4, 5): 0.4, (4, 6): 0.4,
                (1,7): 0.4, (2,7): 0.4, (3,7): 0.4,(4,7): 0.4,(5,7): 0.4,(7, 6): 0.4}

a=time.time()
print(estimate_risk(sources, target, mapping, risk_mapping, 2))
b=time.time()
print(b-a)