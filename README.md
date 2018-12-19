IceCream solves the following problem using a brute force algorithm with minimal/no pruning. The only permutation that
is somewhat reduced is that Peter selected strawberry first, other than that the program attempts all possible 
combinations. That said, this solution takes a very long time to run.

**Problem Statement:**

An ice cream shop conducted a survey on children’s taste in ice cream.  They asked Carl and 
Iris and four other children to rank vanilla, chocolate and strawberry in order of preference, 
and to state whether they preferred ice cream in a cone or in a dish.  
From the eight statements below, you need to determine each child’s first and last name, 
flavor ranking, and preference as to cone or dish.
    
1.   Two of the last names are Hillman and McNeal.
2.   None of the children who ranked chocolate first (at least three did) have siblings who
      ranked chocolate first.
3.   Peter is the only child who ranked strawberry first.
4.   Jacob (who didn’t rank vanilla last and whose last name is not McNeal) and a child 
      whose last name is Harding do not both prefer a cone to a dish, but they are the only
      children with identical flavor rankings. 
5.   Among the only children, all prefer cones.
      Among the siblings, one child in each family prefers a cone.
6.   Only the Johnson children ranked vanilla last.
7.   Hannah prefers a dish to a cone.
8.   Naomi’s brother ranked chocolate last.  

        Present your answer by filling out the following table:

| First Name | Last Name |   First |  Second	|  Third	 | Cone / Dish |
| :--------  | :-------: | :-----: | :------: | :------: | :---------: |
|Peter       |           |         |          |          |             |
|Jacob       |           |         |          |          |             |
|Carl        |           |         |          |          |             |
|Hannah      |           |         |          |          |             |
|Naomi       |           |         |          |          |             |
|Iris        |           |         |          |          |             |
					
My approach to solving this little riddle was first to write a logic board that would represent
the eight statements given above. Before I did that I decided to make a little class with some
very simple methods. The first of these methods is `build_table()` which constructs a table 
identical to the one shown above. I decided to have the table built with the first column 
already containing the first names since all of the first names were given throughout the eight
problem statements anyways. Next, these eight statements are represented in the `check_table()` 
method which returns true if all of the eight statements are satisfied, and false otherwise. After 
those two methods I proceeded to make the `permute_table()` method which does all of the dirty work.
Last but not least I made use of the PrettyTable module in Python to print out the solution table
in a pretty format inside of the `print_table()` method.

After waiting for a few days for the program to go through all of the permutations, the following
solution table was finally obtained.

**The program yields the following solution:**

| First Name | Last Name |   First |  Second	|  Third	 | Cone / Dish |
| :--------  | :-------  | :-----: | :------: | :------: | :---------: |
|Peter       |Johnson    |Strawberry|Chocolate|Vanilla   |    Cone     |
|Jacob       |Hillman    |Chocolate|Vanilla|Strawberry   |    Cone     |
|Carl        |Harding    |Vanilla|Strawberry|Chocolate   |    Cone     |
|Hannah      |Johnson    |Chocolate|Strawberry|Vanilla   |    Dish     |
|Naomi       |Harding    |Chocolate|Vanilla|Strawberry   |    Dish     |
|Iris        |McNeal     |Vanilla|Chocolate|Strawberry   |    Cone     |
