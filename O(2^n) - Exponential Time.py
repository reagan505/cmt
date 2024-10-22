#Exponential time complexity occurs when the growth rate doubles with each addition to the input size

#Real-World Example: The number of ways to arrange a group of people in different seatings increases exponentially as more people are added.

#Solving the Fibonacci sequence recursively.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))