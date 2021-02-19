Recursion is approach of Solving / traversing  the Problem.
        Problem can be Traverse and Solve using Iterative and Recursive Approach. 
        Also we can able to transform any iterative into Recursive approach and Vice versa.

    There are two approaches
        1, Iterative (increment approach)
        2, Recursive Approach
        
    we are going to see the Recursive approach in this section:
        
       Recursive=> Breaking Down the Problem into smaller instances
                    (pieces of Sub Problems)

           Note=> **while Using Recursive approach you should have clear vision about the 
                    base Conditions(Like, How you are going to iterate/ increment, 
                    At which state it is going to Stop, Other Special Cases to Handle)
                    Or else it will end in Infinite Loop. Which is a nightmare**
                    
       
       Types of Recursion:
               I,  Head Recursion
              II,  Tail Recursion
          
          
    I, Head Recursion:
            Head Recursion which happens at the initial instead of start of the Node
                 It Saves The Current State before proceed jumping to another call
                    Because of this it requires more memory when compare to the Tail recursion
                        
                        Ex Print Upto X values (Ex: X =10)
              
                   
  
  
    II, Tail Recursion:
           Tail Recursion which Recursion Call occurs at end of the Function/Method.
                This Method Execute all the Input Before Moving into next Recursive Call
                    This Is tail approach is same as For Loop and while Loop Iterative approach
                            
                        Ex:      Calculate Factorial
                        
                        
                        
    Every Recursive call represent decision or choice at each step.
        Try Out all path to meet certain criteria.
            These are Called Exhaustive Search or Combinatorial Search.
            
           
        Problems are divided into two broad categories
            1. To Generate **Permutations**
                - In Permutation ** Sequences are Important.**
            2. To Generate **Combinations**
                - In Combinations ** Sequences are Not Important. Can Randomly Chose some Elements.**
                So called these are Combinatorial Search
    