from functions import *
from itertools import combinations

def find_all_possible_paths(source,target, mapping,accuracy):

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


def dominancy(people,mapping,risk_mapping):
    combos = list(combinations(people, 2))
    paths=[]

    for pair in combos:
        paths.extend(find_all_possible_paths(pair[0], pair[1], mapping, 3))

    centrality={}
    for i in risk_mapping:
        centrality.update({i:0})

    total=0
    for path in paths:
        risk = intersection_of(path, risk_mapping)
        for edge in path:
            extract_and_insert(edge,centrality,risk)
        total+=risk
    print(total)
    for i in centrality:
        val=(centrality.get(i))/total
        centrality.update({i:val})
    
    return(centrality)


        




