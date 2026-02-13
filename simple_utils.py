# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in a string.
    
    Parameters:
        text (str): The input string to reverse.
    
    Returns:
        str: The input string with characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence by splitting on whitespace.
    
    Parameters:
        sentence (str): Input text to count words from.
    
    Returns:
        int: Number of word tokens obtained by splitting `sentence` on whitespace.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius (float | int): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32