''' Data Input format:
    sources= # List of nodes #                                                                                                       eg [1,3,6....]
    target=    # Node Number #                                                                                                       eg    5
    mapping=   # Dictionary with key as node number and value as list of all first degree connected nodes#                           eg {1:[2,3],2:[1,4],3:[1,4],4:[2,3,5],5:[4]}
    risk_mapping = #  Dictionary with key as edge denoted by tuple of joint nodes and value as risk probability in decimal system #  eg  {(1,2):0.5 , (2,4):0.5 , (3,4): 0.5, (4,5): 0.5, (1,3):0.5 , }   
'''

from functions import *
from itertools import combinations


def find_all_possible_paths(source, target, mapping, accuracy):

    paths = []
    path = [source]
    visited = {}
    for i in mapping:
        visited.update({i: []})

    current = source
    while True:

        just_visited = []
        backtrack = True

        for vertex in mapping[current]:

            if vertex == target and vertex not in visited.get(current):
                path.append(vertex)
                k = path.copy()
                paths.append(k)
                path.remove(vertex)
                just_visited.append(vertex)
            elif vertex not in path and vertex not in visited.get(current) and len(path) < accuracy:
                path.append(vertex)
                just_visited.append(vertex)
                backtrack = False
                break
            else:
                pass

        just_visited = just_visited+visited.get(current)
        visited.update({current: just_visited})
        if backtrack == True:
            path.remove(current)
            visited.update({current: []})

            if path != []:
                current = path[-1]
            else:
                break
        else:
            current = vertex

    paths = convert_path_to_edges(paths)

    return(paths)



def estimate_risk_of_target(sources, target, mapping, risk_mapping,accuracy,top):


    paths=[]
    for source in sources:
        relative_mapping=relative_map(source,sources,mapping)
        paths.extend(find_all_possible_paths(source,target, relative_mapping, accuracy))

    paths = rank(paths, risk_mapping, top)
    sum=0
    for i in range(1,len(paths)+1):
        sign = (-1)**(i+1)
        combos=list(combinations(paths,i))
        
        for j in combos:
            d=()
            for k in j:
                d+=k
            d=distinct(d)
            intersection = intersection_of(d, risk_mapping)
            sum+=(sign)*intersection

    
    if target in sources:
        return(1)
    else:
        return(sum)





def estimate_risk_of_relation_infection_in_social_network(people, mapping, risk_mapping):
    
    combos = list(combinations(people, 2))
    paths = []

    for pair in combos:
        paths.extend(find_all_possible_paths(pair[0], pair[1], mapping, 3))

    centrality = {}
    for i in risk_mapping:
        centrality.update({i: 0})

    total = 0
    for path in paths:
        risk = intersection_of(path, risk_mapping)
        for edge in path:
            extract_and_insert(edge, centrality, risk)
        total += risk

    for i in centrality:
        val = (centrality.get(i))/total
        centrality.update({i: val})

    return(centrality)
