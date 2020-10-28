''' Data Input format:
    sources= # List of nodes #                                                                                                       eg [1,3,6....]
    target=    # Node Number #                                                                                                       eg    5
    mapping=   # Dictionary with key as node number and value as list of all first degree connected nodes#                           eg {1:[2,3],2:[1,4],3:[1,4],4:[2,3,5],5:[4]}
    risk_mapping = #  Dictionary with key as edge denoted by tuple of joint nodes and value as risk probability in decimal system #  eg  {(1,2):0.5 , (2,4):0.5 , (3,4): 0.5, (4,5): 0.5, (1,3):0.5 , }   
'''





def estimate_risk(sources, target, mapping, risk_mapping):

    from itertools import combinations
    import time

    
    
    
    
    def calculate_risk(risk_mapping):

        paths=[]
        for source in sources:
            relative_mapping = mapping.copy()
            for other_sources in sources:
                if other_sources != source:
                    relative_mapping.pop(other_sources)
            paths.extend(find_all_possible_paths(source, target, mapping))

        print(paths)
        sum=0
        for i in range(1,len(paths)+1):
            combos=list(combinations(paths,i))
            for j in combos:
                d=()
                for k in j:
                    k=convert_path_to_edges(k)
                    d+=k
                d=list(set(d))
                intersection=1
                for t in d:
                    h = risk_mapping.get(t)
                    if h==None:
                        intersection *= risk_mapping.get((t[1],t[0]))
                    else:
                        intersection *= h
                sum+=((-1)**(i+1))*intersection
        return(sum)

    
    
    
    
    def convert_path_to_edges(path):
        edge_list=[]
        for i in range(len(path)-1):
            edge_list.append((path[i],path[i+1]))
        return(tuple(edge_list))

    
    
    
    
    def eq(x,y):
        x.sort()
        y.sort()
        if x==y:
            return(True)
        else:
            return(False)

    
    
    
    
    
    def find_all_possible_paths(source,target,mapping): # Uses depth first search to traverse graph
        
        paths=[]
        path=[source]
        visited={}
        for i in mapping:
            visited.update({i:[]})

        current=source
        while True:
            
            backtrack=True
            for vertex in mapping[current]:
                just_visited=[]
                if vertex==target:
                    path.append(vertex)
                    k=path.copy()
                    paths.append(k)
                    path.remove(vertex)
                elif vertex not in path and vertex not in visited.get(current):
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
                current=path[-1]
            else:
                current = vertex
            
            
            if current==source and eq( visited.get(source),mapping.get(source) ):
                break
            
        return(paths)


    
    
    
    
    
    return(calculate_risk(risk_mapping))







