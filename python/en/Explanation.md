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
