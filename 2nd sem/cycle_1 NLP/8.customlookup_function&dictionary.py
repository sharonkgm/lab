#Create a custom Lookup Dictionary and Create a Custom Function For text Standardization

# Custom dictionary
custom_dict = {
    'h': 'Hi',
    'l': '.',
    'hw': 'how',
    'ty': 'today',
    '.' : '.',
}

# Custom function 
def custom_fuction(input_text, custom_dict):
    words = input_text.split()
    standardized_words = [custom_dict.get(word, word) for word in words]
    return ' '.join(standardized_words)

# Example usage
input_text = "h l hw is ty ."
standardized_text = custom_fuction(input_text, custom_dict)

print("Original Text:", input_text)
print("Standardized Text:", standardized_text)
