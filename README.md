# Preview

This project is completely open source and we look forward to considering your suggestions about any error we might have overlooked or any logical fallacy we might have not been able to figure out , or even a scope for improvement as a user's actions and judgements concerning their own safety might use these statistics as a dominant parameter and giving them inaccurate results might lead to a compromise of their safety , contradicting the whole intention of this project.

This project is just a prototype and has not been designed to fully  be put to mass use , but rather to just convey an idea , which we hope can provide an incentive to people in the development of further ideas thus progressing society as a whole.


# Disease Risk Estimation

Disease risk estimation by modelling disease transmission dynamics through user updated social interactions.

This project is designed for estimating risks based on social connections assumming relatively simple and ideal one to one transmission dynamics with the hope that the necessarry protocols such as hygiene,social distancing, wearing surgical face masks, etc. are being followed and may not be capable of analysing large social gatherings or physical contacts where transmission dynamics get more advanced and relitively chaotic , making parameters assumed insignificant here dominant enough to produce a significantly different result ,  thus require more advanced and sophesticated methods.

It cannot take action, all it can do is give people information with the hope that they will take the right necessarry actions,as people should know what they are dealing with.


With all good hope, we wish that it can make some difference and avoid something unwanted from happening.



# Objective

To find the risk of a node from multiple sources given a probability mapping
 



# Algorithmic Flow:


Find all possible paths between all given sources and target(node) in a given mapping by finding all possible paths between one source and target considering a mapping without all the other sources and repeating for all the sources, logging the paths in each case.

Calculate probability from probability mapping by an intersection of all edges of a path and then a union of all induvidual paths from all sources.



# Pseudocode:

    function estimate_risk(sources ,target,mapping,risk_mapping):
        
        
        
        function find_all_possible_paths(source,target,mapping):

            while all first degree connections of source have not been explored

                backtrack=True
                for vertex = all unexplored first degree connections of current
                    
                    if vertex is target
                        log path to all_possible_paths
                    else
                        backtrack=False
                        log vertex to path
                        log vertex as an exploration of current
                        current=vertex
                        break from for loop

                if backtrack is True
                    erase current from path
                    erase all explorations of current
                    backtrack current to its predecessor from path

            return all_possible_paths



         
         
         function calculate_risk(target,risk_mapping):
            
            for source in sources
                relative_mapping = mapping without all the other sources
                log find_all_possible_paths(source,target,relative_mapping) in paths

            for i from 1 to ( total number of paths):

                combo = all i path combinations of paths
                intersection = product of risks of all distinct values of combo from risk_mapping

                if i is odd
                    add intersection to risk
                else
                    subtract subtract intersection from risk


             return risk











