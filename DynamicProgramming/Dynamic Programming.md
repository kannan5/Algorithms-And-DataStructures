**Dynamic Programming**

Dynamic Programming is a process of solving an Optimization Problem by breaking down into Smaller Sub Problems

    There are two types of  Dynamic Programming Approaches
	    1. Top Down Approach(Memoization) - Recursion
	        > Uses Recursive Approach and Memory Table To Store Sub Problem Results.
	        + Solve Sub Problem Only When its Demanded.
	        + Easy To Implement / Debug.
	        - Recursion use more memory in the Call stack. using Deep Recursion Might Stack Overflow
	        - Performance Overhead due to the recursion
	        
        2. Bottom Up Approach(Tabulation) - Iterative
            >Solve All the SubProblems and then we move to larger Problem. 
              Using Sub Problem result we used to generate result of larger problem.
            > Use for-loop to iterate sub problem and solve them.
            
            > So called, tabulation method or table filling method.
            
            + it is time and space efficient. since recursion uses lot of memory Overhead, recursion uses
                space in call stack.
            - it is difficult to implement
            - it solve all the subproblem whether its used or not /where Top down approach solve based on demand.
            
            
        
    Tips:Usually we start with Naive Recursive Approach and Understand the Base Cases and InOuts and Try to Optimize 
    with DP Techniques.
    
    In Other Words: It's a technique for solve certain type of complex problems **efficiently** by breaking down into sub problems.
    and solving each sub-problem exactly once. Dynamic programming stores results into table and reuse 
    them whenever needed to avoid such problem again and again.
                 
     Types Of Problem Can be Solved Using Dynamic Programming:
            The Problem Should have following properties:
            
                        1. Optimal Sub Structure.
                            - By Optimal Solution of given Problem can be obtained by using Optimal Solution
                                of its Sub Problems. 
                                
                            In Other Words:
                            - If we can able to define solution to the problem by using recurrence relationship
                                based on the Sub Problems.
                                
                        2. OverLapping Sub Problems.
                            
                
                    
      
