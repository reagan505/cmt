#Factorial time complexity appears in problems involving permutations, where you need to evaluate all possible orders.

#Real-World Example: Solving the traveling salesman problem by considering every possible route.

#Generating all permutations of a list.

import itertools

arr = [1, 2, 3]
permutations = list(itertools.permutations(arr))
print(permutations)  
