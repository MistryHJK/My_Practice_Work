# Array And List
# 1. Find minimum and maximum values of a list
# Here we are defining a function min_max which takes a list as an argument and returns the minimum and maximum value of the list.
def min_max(arr):
    return min(arr),max(arr)

arr = [4,9,6,7,2,0,36,89]
print(min_max(arr))

print("--------------------------------------")

# 2. Reverse the list
def reverse_array(arr):
    return arr[::-1]

arr=[4,5,9,3,5,6,1,2,3,33,22,55,99,77,88]
print(reverse_array(arr))

print("--------------------------------------")

# 3. Find the sum of all elements of a list
def sum_array(arr):
    return sum(arr)
    
arr=[4,9,6,7,2]
print(sum_array(arr))

print("--------------------------------------")

# 4. Find the average of all elements of a list
from statistics import mean

def average_array(arr):
    return mean(arr)

arr=[4,9,6,7,2]
print(average_array(arr))

print("--------------------------------------")

# 5. Find the median of all elements of a list
from statistics import median
def median_array(arr):
    return median(arr)#sorted(arr)[len(arr)//2]

arr=[4,9,6,7,2]
print(median_array(arr))

print("--------------------------------------")

# 6. Find the mode of all elements of a list
from statistics import mode
def mode_array(arr):
    return mode(arr)

arr=[4,9,6,7,2]
print(mode_array(arr))

print("--------------------------------------")

# 7. Find the number of even and odd numbers in a list
def odd_even(arr):
    odd=0
    even=0
    for i in arr:
        if i%2==0:
            print(f"{i} is even")
            even+=1
        else:
            print(f"{i} is odd")
            odd+=1
    return odd,even
    
arr=[4,9,8,6,3,2,1]
print(odd_even(arr))

print("--------------------------------------")

# 8. Find the number of positive and negative numbers in a list
def positive_negative(arr):
    positive=0
    negative=0
    for i in arr:
        if i<0:
            print(f"{i} is negative")
            negative+=1
        else:
            print(f"{i} is positive")
            positive+=1
    return positive,negative
    
arr=[4,9,6,-8,-5,2,6,-3]
print(positive_negative(arr))