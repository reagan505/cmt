#Quadratic time complexity occurs when there are nested loops, leading to an increase in time proportional to the square of the input size.

#Real-World Example: Comparing each pair of students in a class to check if they know each other.

 #Bubble sort algorithm.

def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j] > students[j+1]:
                students[j], students[j+1] = students[j+1], students[j]
    return students

students = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(students)) 
