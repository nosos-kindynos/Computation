


# Objective:

To find the risk of a node from multiple sources given a probability mapping
 



# Algorithm:


Find all possible paths between all given source vertices and target vertex in a given mapping by finding all possible paths between one source and target considering a mapping without all the other sources and repeating for all the sources. All possible paths can be found by traversing the mapping by progressing from vertex to vertex and only removing the vertex from the path and backtracking to the previous one, if the vertex has already been visited in the current path, while putting a small constraint that if it happens to come across the target while traversing the mapping, it logs in the current path while treating the target as a visited vertex.

Calculate probability from probability mapping by a set intersection of all edges in a path and then a set union of all induvidual paths from all sources , where the final expression is evaluated treaating the intersection as multiplication.



# Pseudocode:

    function estimate_risk (sources,target,mapping,risk_mapping) :
        
        
        
        function find_all_possible_paths (source,target,mapping) :
            
            log source to path
            
            while path is not empty :

                backtrack=True
                for vertex = all unexplored first degree connections of current
                    
                    if vertex is target
                        log path to all_possible_paths
                        log vertex as an exploration of current
                        
                    else
                        backtrack=False
                        log vertex to path
                        log vertex as an exploration of current
                        current=vertex
                        
                        break from for loop
                        
                        
                if backtrack is True
                    erase current from path
                    erase all explorations of current
                    backtrack current to its predecessor from path if path is not empty
                    

            return all_possible_paths



         
         
         function calculate_risk (target,risk_mapping) :
            
            for source in sources
                relative_mapping = mapping without all the other sources
                log find_all_possible_paths(source,target,relative_mapping) in paths

            for i from 1 to (total number of paths) :

                combinations = all i path combinations of paths
                intersection = summation of the products of transfer chance of all distinct edges

                if i is odd
                    add intersection to risk
                else
                    subtract intersection from risk


             return risk
             
         
         if target is in sources:
             return (1)
         else:
             return calculate_risk (risk_mapping)
             
             
          


Time Complexity: summation i from 1 to n ip nci (assumming one cycle to be a primary binary operation)

# Note: 

For running in current computers relevant approximations may be needed to achieve an output in a considerable time , which may vary depending on the processing speed of the computer.

The probability may be calculated by taking into account not all the paths but the relatively dominant paths ,  which can be ranked on an estimate based on the degree of connection, thus a constraint which holds the backtrack variable True if a path lenth overshoots the input parameter while exploring may be added to the 
find_all_possible_paths function in the above pseudocode to achieve output in a considerable time with limited processing capabilities.






