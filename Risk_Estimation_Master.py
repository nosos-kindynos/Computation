''' Data Input format:
    sources= # List of nodes #                                                                                                       eg [1,3,6....]
    target=    # Node Number #                                                                                                       eg    5
    mapping=   # Dictionary with key as node number and value as list of all first degree connected nodes#                           eg {1:[2,3],2:[1,4],3:[1,4],4:[2,3,5],5:[4]}
    risk_mapping = #  Dictionary with key as edge denoted by tuple of joint nodes and value as risk probability in decimal system #  eg  {(1,2):0.5 , (2,4):0.5 , (3,4): 0.5, (4,5): 0.5, (1,3):0.5 , }   
'''





def estimate_risk(sources, target, mapping, risk_mapping,accuracy):

    from itertools import combinations
    import time

    
    
    
    
    def calculate_risk(risk_mapping):

        paths=[]
        for source in sources:
            relative_mapping = mapping.copy()
            other_sources=sources.copy()
            other_sources.remove(source)
            for other_source in other_sources:
                relative_mapping.pop(other_source)
            for vertex in relative_mapping:
                connections=relative_mapping.get(vertex)
                for connection in connections:
                    if connection in other_sources:
                        connections.remove(connection)
                relative_mapping.update({vertex:connections})
                        
            paths.extend(find_all_possible_paths(source, target, relative_mapping,accuracy))

        paths=convert_path_to_edges(paths)

        print(len(paths))
        sum=0
        for i in range(1,len(paths)+1):
            sign = (-1)**(i+1)
            combos=list(combinations(paths,i))
            print(i)
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

    
    
    
    
    def find_all_possible_paths(source,target,mapping,accuracy): 
        
        paths=[]
        path=[source]
        visited={}
        for i in mapping:
            visited.update({i:[]})

        current=source
        while True:
            
            just_visited=[]
            backtrack=True
            
            for vertex in mapping[current]:
                
                if vertex==target and vertex not in visited.get(current):
                    path.append(vertex)
                    k=path.copy()
                    paths.append(k)
                    path.remove(vertex)
                    just_visited.append(vertex)
                elif vertex not in path and vertex not in visited.get(current) and len(path)<accuracy:
                    path.append(vertex)
                    just_visited.append(vertex)
                    backtrack=False
                    break
                else:
                    pass
            
            just_visited=just_visited+visited.get(current)
            visited.update({current:just_visited})
            if backtrack==True:
                path.remove(current)
                visited.update({current:[]})
                
                if path!=[]:
                    current=path[-1]
                else:
                    break
            else:
                current = vertex
            
            
 
            
        return(paths)


    
    
    
    
    
    return(calculate_risk(risk_mapping))



