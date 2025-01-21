# Find a Palindrome Number in Python

We will see how to find the n-th palindrome number using a program written in the Python programming language.

To achieve this, we will cover:
- [What is a Palindrome Number?](#what_is_markdown)
- [Program Code](#program_code)
- [Global Explanation of the Program](#program_overview)
- [Block-by-Block Explanation](#explanation_by_block)
- [Line-by-Line Explanation with Comments](#line_by_line_explanation_with_comments)

## What is a Palindrome Number?
<div id='what_is_markdown'/>  

A palindrome number is a number that remains the same when its digits are reversed. In other words, it reads the same from left to right and from right to left.

For example:

- 121 is a palindrome number because reversing its digits still gives 121.
- 1331 is also a palindrome because 1331 read backward is still 1331.
- Another example is 1221, which also remains 1221 when reversed.

On the other hand, a number like 123 is not a palindrome because reversing its digits gives 321, which is different from 123.

## Program Code
<div id='program_code'/>  

```python
import time

# Function to check if a number is a palindrome
def is_palindrome(number: int):
    str_number = str(number)
    return str_number == str_number[::-1]

def find_palindrome(target: int):
    count = 0
    number = 0

    # Find the palindrome
    while count < target:
        if is_palindrome(number):
            count += 1
        number += 1
    
    return number - 1


# --- Program ---

if __name__ == "__main__":  # This line is for logistics. Don't worry too much about it.
    
    while True:
        try:
            palindrome_target = int(input("Please enter the palindrome number to find: "))
            if palindrome_target <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Oops! That wasn't a valid number. Try again...\n")

    # Display a loading message
    print("\nLoading ...\n")
    
    # Start timing
    start_time = time.time()
    
    # Perform the palindrome search
    palindrome = find_palindrome(palindrome_target)
    
    # End timing
    duration = time.time() - start_time
    
    # Display results
    print(f"Execution time: {duration:.3f} seconds")
    print(f"The {palindrome_target}th palindrome number is: {palindrome}")
```

## Global Explanation of the Program
<div id='program_overview'/>

This program works simply: it checks each integer one by one to see if it's a palindrome. Whenever it finds one, it increments a counter. When the counter reaches the number of palindromes requested by the user, the program stops and displays the result, along with the execution time.

## Block-by-Block Explanation
<div id='explanation_by_block'/>  

### Importing Libraries

```python
import time
```
This line imports the `time` library, which is used to measure the program's execution time.

### Function to Check for a Palindrome

```python
# Function to check if a number is a palindrome
def is_palindrome(number: int):
    str_number = str(number)
    return str_number == str_number[::-1]
```
This function converts a number into a string (text) to compare its normal and reversed versions. If they are identical, the number is a palindrome.

### Function to Find a Palindrome

```python
def find_palindrome(target: int):
    count = 0
    number = 0

    # Find the palindrome
    while count < target:
        if is_palindrome(number):
            count += 1
        number += 1
    
    return number - 1
```

This function searches for the **n-th palindrome** by incrementing a `count` variable each time a palindrome is found. The number is returned once the counter reaches the target value.

### User Interface and Time Measurement

#### 1. User Input and Validation

```python
if __name__ == "__main__":
    while True:
        try:
            palindrome_target = int(input("Please enter the palindrome number to find: "))
            if palindrome_target <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Oops! That wasn't a valid number. Try again...\n")
```

This block asks the user to input a valid integer, ensures it is strictly positive, and retries in case of an error.

#### 2. Preparation and Loading Message

```python
    # Display a loading message
    print("\nLoading ...\n")
```

This line informs the user that the program is starting the search.

#### 3. Timing and Calculation

```python
    # Start timing
    start_time = time.time()
    
    # Perform the palindrome search
    palindrome = find_palindrome(palindrome_target)
    
    # End timing
    duration = time.time() - start_time
```

These lines measure the time taken to find the palindrome by recording the start and end times of the operation.

#### 4. Results

```python
    # Display results
    print(f"Execution time: {duration:.3f} seconds")
    print(f"The {palindrome_target}th palindrome number is: {palindrome}")
```

This block displays the execution time and the found palindrome.

## Line-by-Line Explanation with Comments
<div id='line_by_line_explanation_with_comments'/>  

Here is the program with comments for each line:

```python
import time  # Import the library to measure execution time

# Function to check if a number is a palindrome
def is_palindrome(number: int):
    str_number = str(number)  # Convert the number to a string
    return str_number == str_number[::-1]  # Compare the normal and reversed strings

# Function to find the n-th palindrome
def find_palindrome(target: int):
    count = 0  # Counter to track the number of palindromes found
    number = 0  # The current number being checked

    # Loop until the counter reaches the target
    while count < target:
        if is_palindrome(number):  # Check if the current number is a palindrome
            count += 1  # Increment the counter if it is
        number += 1  # Move to the next number
    
    return number - 1  # Return the last found palindrome

# --- Main Program ---

if __name__ == "__main__":  # Entry point of the program
    
    while True:  # Loop to ask for valid user input
        try:
            palindrome_target = int(input("Please enter the palindrome number to find: "))  # Ask for an integer
            if palindrome_target <= 0:  # Ensure the number is positive
                raise ValueError()  # Raise an error if it is not
            break  # Exit the loop if the input is valid
        except ValueError:  # Handle errors related to invalid input
            print("Oops! That wasn't a valid number. Try again...\n")

    print("\nLoading ...\n")  # Display a loading message
    
    start_time = time.time()  # Record the start time
    
    palindrome = find_palindrome(palindrome_target)  # Find the n-th palindrome
    
    duration = time.time() - start_time  # Calculate execution time
    
    print(f"Execution time: {duration:.3f} seconds")  # Display execution time
    print(f"The {palindrome_target}th palindrome number is: {palindrome}")  # Display the result
```
