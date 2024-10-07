import re

def analyze_text(text):
    # Split the text into words (Hint: Use a string method that splits based on spaces)
    words = text.________()
    
    # Count the number of words (Hint: Use a built-in function to count the length of a list)
    num_words = ___________(words)
    
    # Count the number of digits using regex (Hint: Use re.findall() with the pattern for digits '\d')
    num_digits = len(re._________(________, text))
    
    # Count the number of punctuation marks (.,!?) (Hint: Use re.findall() with a regex pattern for punctuation)
    num_punct = len((________, text))

    # Print the results (Hint: Use f-strings or another string formatting method to display the output)
    print(f'Text Analysis:')
    print(f'Words: {________}')
    print(f'Digits: {________}')
    print(f'Punctuation Marks: {________}')

# Input from the user (Hint: Use the built-in function to get input from the user)
user_text = ____________("Enter a sentence: ")

# Analyze the input text (Hint: Call the analyze_text function with the user_text)
____________(user_text)