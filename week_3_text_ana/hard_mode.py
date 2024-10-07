import re 

# Function to count words, digits, and punctuation
def analyze_text(text):
    # Split the text into words (Hint: Use a string method that splits based on spaces)
    words = text.________()

    # Count the number of words (Hint: Use a built-in function to count the length of a list)
    num_words = ___________(words)

    # Count the number of digits using regex (Hint: Use re.findall() with the pattern for digits '\d')
    num_digits = len(re._________(r'________', text))

    # Count the number of punctuation marks (.,!?) (Hint: Use re.findall() with a regex pattern for punctuation)
    num_punct = len(re.findall(r'[________]', text))

    # Print the basic analysis results
    print(f'Text Analysis:')
    print(f'Words: {________}')
    print(f'Digits: {________}')
    print(f'Punctuation Marks: {________}')

    # Call additional functions for extended analysis
    count_vowels(________)
    count_consonants(________)
    count_upper_lower(________)
    count_special_characters(________)

# Function to count vowels
def count_vowels(text):
    # Hint: Use re.findall() with a regex pattern to find vowels (both lowercase and uppercase)
    num_vowels = len(re.findall(r'[________]', text))
    print(f'Vowels: {________}')

# Function to count consonants
def count_consonants(text):
    # Hint: Use re.findall() with a regex pattern for consonants (both lowercase and uppercase)
    num_consonants = len(re.findall(r'[________]', text))
    print(f'Consonants: {________}')

# Function to count uppercase and lowercase letters
def count_upper_lower(text):
    # Hint: Use string methods to count uppercase and lowercase characters
    num_uppercase = sum(1 for char in text if char.________())
    num_lowercase = sum(1 for char in text if char.________())
    print(f'Uppercase letters: {________}')
    print(f'Lowercase letters: {________}')

# Function to count special characters (Hint: Characters that are not letters, digits, or spaces)
def count_special_characters(text):
    # Hint: Use re.findall() to identify non-alphanumeric characters excluding spaces
    num_special_chars = len(re.findall(r'[^________]', text))
    print(f'Special Characters: {________}')

# Input from the user (Hint: Use the built-in function to get input from the user)
user_text = ____________("Enter a sentence: ")

# Analyze the input text (Hint: Call the analyze_text function with the user_text)
____________(user_text)
