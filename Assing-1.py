# Python3 program to
# convert a decimal
# number to hexadecimal
# number
 
# function to convert
# decimal to hexadecimal

def decimal_to_hexadecimal(n):
    if n == 0:
        return '0'
    
    hex_digits = "0123456789ABCDEF"
    hex_result = ""
    
    while n > 0:
        remainder = n % 16
        hex_result = hex_digits[remainder] + hex_result
        n = n // 16

    return hex_result

# Examples
print(decimal_to_hexadecimal(10)) # Output : A
print(decimal_to_hexadecimal(2545)) # Output : 9F1

# Get user input
user_input1 = int(input("Enter a decimal number: "))
user_input2 = int(input("Enter a decimal number: "))

# Convert to hexadecimal
hex_value1 = decimal_to_hexadecimal(user_input1)
hex_value2 = decimal_to_hexadecimal(user_input2)

# Display the result
print(f"The hexadecimal representation of {user_input1} is: {hex_value1}")
print(f"The hexadecimal representation of {user_input2} is: {hex_value2}")