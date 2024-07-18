# WRITE PROGRAM THAT HANDLES EXCEPTIONS BY USING TRY, 
# CATCH, AND FINALLY BLOCKS

def handle_exception():
    try:
        # Prompt user to input a number
        user_input = input("Please enter a number: ")
        number = float(user_input)

        # Attempt to divide a fixed number by the user-provided number
        result = 10 / number

        # Print the result 
        print(f"The result of dividing 10 by {number} is {result}")

    except ZeroDivisionError:
        # Handle the division by zero exception
        print("Error: Division by zero is not allowed.")

    except ValueError:
        # Handle the exception if the input is not a number
        print("Error: Invalid input. Please enter a valid number.")

    finally:
        # Cleanup operations
        print("Execution of the try-except block is complete.")

if __name__ == "__handle_exception__":
    handle_exception