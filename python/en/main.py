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

if __name__ == "__main__":  # This line is for logistics. Don't pay attention to it.
    
    while True:
        try:
            palindrome_target = int(input("Please enter a palindrome number to find: "))
            if palindrome_target <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...\n")
    
    # Start time measurement
    start_time = time.time()
    
    # Perform the search for the number
    palindrome = find_palindrome(palindrome_target)
    
    # End time measurement
    duration = time.time() - start_time
    
    # Display results
    print(f"Execution time: {duration:.3f} seconds")
    print(f"The {palindrome_target}th palindrome number is: {palindrome}")
