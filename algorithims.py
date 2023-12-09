def list_difference(a, b):
    return [element for element in a if element not in b]
#returns list for difference 

def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False
#endswith function- if string endswith something
    
def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if all(letter in s for letter in alphabet):
        return True
    else:
        return False
#all function - contains all elements in string thats found in another

def duplicate_encode(word):
    word_lower = word.lower()  # Convert the input string to lowercase
    new_string = ''
    
    for char in word_lower:
        if word_lower.count(char) == 1:
            new_string += '('  # Append '(' if character appears only once
        else:
            new_string += ')'  
    
    return new_string
#loop a string by character and use count function to count the character

def longest(a1, a2):
    combined_string = a1 + a2 
    unique_chars = sorted(set(combined_string)) 
    result = ''.join(unique_chars)  # convert to string
    return result

# combine strings - use set function to get unique characters
#sort function to sort

def find_short(s):
    words = s.split()  
    l = min(len(word) for word in words) 
    return l 

# uses split function to split string into [list] of words
# uses min function to find minimum length

def duplicate_count(s):
  
    s_lower = s.lower()

    # Initialize a dictionary to count occurrences of characters
    char_count = {}

    # Count occurrences of each character
    for char in s_lower:
        if char.isanum():  # Check if the character is alphanumeric
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Count the characters that occur more than once
    repeated_chars_count = sum(1 for count in char_count.values() if count > 1)

    return repeated_chars_count
        