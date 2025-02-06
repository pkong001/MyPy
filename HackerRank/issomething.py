if __name__ == '__main__':
    for _ in range(5):  # Loop to take 5 inputs
        s = input("Enter a string: ")  
        print(any(i.isalnum() for i in s))  # Checks if any character is alphanumeric
        print(any(i.isalpha() for i in s))  # Checks if any character is a letter
        print(any(i.isdigit() for i in s))  # Checks if any character is a digit
        print(any(i.islower() for i in s))  # Checks if any character is lowercase
        print(any(i.isupper() for i in s))  # Checks if any character is uppercase
        print("-" * 30)  # Separator for readability

# Sample Input
# qA2

# Sample Output
# True
# True
# True
# True
# True