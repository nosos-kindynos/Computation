# Disease-Risk-Estimation
Risk estimation by modelling disease transmission dynamics through user updated social interactions

This program is designed for estimating risks based on social connections assumming relatively simple and idealistically equiweighted one to one transmission dynamics with the hope that the necessarry protocols (hygiende,social distancing, wearing surgical face masks,etc.) are being followed and may not be able capable to track large social gatherings or physical contacts where transmission dynamics get chaotic , making parameters assumed insignificant here dominant enough to produce a significantly different result ,  thus require more advanced and sophesticated methods.

It cannot take action, all it can do is give people information with the hope that they will take the right necessarry actions,as people should know what they are dealing with.


With all good hope, we wish that it can make some difference and avoid something unwanted from happening.


make a formatting file which formats data into the requisite input
use .get for retrieving data in dictionary as it will automatically give none for isolated node groups
use database for retrieving data and make UI with image of a map with ID card photo of student.

This program does not have an autonomous input system and is heavily biased on user data, witht the hope that they will enter data accurate to the best of thir information.
This takes equiweighted variables for all people based on rough estimates or measures of central tendency of huge datasets from various sources of information.
incubation period=3 days transfer chance will be based on relationship.
Run master code everytime there is even the smallest mapping update...if too much then run on every few updates.
Have a quarantine status,given to people above critical value.
critical value>safe value. all these values will be exponentially decreasing.
check all first degree connection of each node and suggest them people they should distance from if they are above safe calue and also suggest them who they pose a risk to if they are above safe value.
they can press a distance option if they have started distancing from the required person.
weight of the graph will be the one on one tranfer chance ....whose value depends on relationship.
option for committing that you have come in close contact with someone and how close they are.
on that basis, only student will be quarantined as they are second degree and others will be just high risk.
give daily update on who is high risk.


# Objective

To find the risk of a node from multiple sources given a probability mapping
 



# Algorithmic Flow:


Find all possible paths between all given sources and target(node) in a given mapping by finding all possible paths between one source and target considering a mapping without all the other sources and repeating for all the sources, logging the paths in each case.

Calculate probability from probability mapping by intersection of all edges of a path and then a union of all paths from all sources.



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











