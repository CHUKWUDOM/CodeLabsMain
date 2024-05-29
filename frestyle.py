def check_letter_type(letter):
    # Define vowels
    vowels = "aeiouAEIOU"

    # Check if the input is a single alphabetic character
    if len(letter) == 1 and letter.isalpha():
        if letter in vowels:
            return "The letter is a vowel."
        else:
            return "The letter is a consonant."
    else:
        return "Invalid input. Please enter a single alphabetic character."


# Get user input
user_input = input("Please enter a letter: ")

# Check the letter type and print the result
result = check_letter_type(user_input)
print(result)

