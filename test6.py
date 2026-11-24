

#Question 1: Find the largest number

def find_largest(values):
  if not values:
    raise ValueError("Cannot find the largest number in an empty list.")

  largest = values[0]  # Start with the first number as the largest
  for num in values[1:]:
    if num > largest:
      largest = num  # Update if we find a bigger number

  return largest


# Example usage:
print(find_largest([4, 9, 2, 7]))  






#Question 2: Count even and odd numbers

def count_even_odd(values):
    even_count = 0
    odd_count = 0

    for num in values:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


# Example
print(count_even_odd([1, 2, 3, 4, 6])) 

# Tests with negative numbers and zero
print(count_even_odd([-2, -1, 0, 1, 2])) # output 3,2 (Doubt)




#Question 3: Reverse a string

def reverse_text(text):
    result = ""
    for ch in text:
        result = ch + result
    return result

original = "Anand Kumar Chaursiya"
reversed_str = reverse_text(original)

print(reversed_str)  
print(original)    



#Question 4: Check for a palindrome


def is_palindrome(text):
    return text == text[::-1]


# Examples
print(is_palindrome("level"))   # True
print(is_palindrome("Python"))  # False (capital 'P' != lowercase 'p')

# Edge cases
print(is_palindrome(""))        # True
print(is_palindrome("a"))       # True






#Question 5: Linear search
def linear_search(values, target):
    for i, item in enumerate(values):
        if item == target:
            return i
    return -1


nums = [10, 20, 30, 40]

# Example
print(linear_search(nums, 30))  # 2

# Required test cases
print(linear_search(nums, 10))  # 0  (first position)
print(linear_search(nums, 40))  # 3  (last position)
print(linear_search(nums, 99))  # -1 (not present)