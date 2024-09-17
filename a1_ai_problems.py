# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# 1. Write a function that sorts even and odd numbers in a list and returns the odd numbers

def dog(lst):
    odd = []
    for x in range (len(lst)):
        if x % 2 !=0:
            odd.append(x)
            return odd
        
assert dog([5,4,3,2,1]) == [1,3,5], "failed[5,4,3,2,1]"
        
# 2. Write a function that counts the number of vowels (a, e, i, o, u) in a given string.

def vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            c+=1 
    return count


# 3. Write a function that determines if a number is divisible by 7 or not.

def div7(n):
    if n % 7 == 0:
        return True
    return False
