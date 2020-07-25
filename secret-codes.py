#!/usr/bin/env python3

# Get user input.
print("Enter your phrase:")
original_phrase = input()

# Note which characters are capitalized.
num = 0
uppers = []
for l in original_phrase:
    if l.isupper():
        uppers.append(num)
    num += 1

# Make all letters lowercase before converting.
text_to_convert = original_phrase.lower()

# Define the code system.
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Create reverse alphabet.
opt1 = sorted(alphabet, reverse=True)
opt2 = [
    'f', 'b', 'c', 'o', 'd', 'w', 'n', 'x', 'l', 'h', 'k', 'j', 'e',
    't', 'a', 'g', 'p', 'z', 'q', 'i', 'v', 'm', 'u', 's', 'y', 'r'
]

#print("\nPlease choose your code option (opt1 or opt2):")
picked = opt1 #if input() == 'opt1' else opt2

# Map the characters together in a dictionary.
code = dict(zip(alphabet, picked))

# Convert the text (output as a list) using the dictionary.
converted_text = []
for c in text_to_convert:
    if c not in code.keys():
        converted_text.append(c)
    else:
        converted_text.append(code[c])

# Prepare the output with correct capitalization.
output_text = converted_text
for i in uppers:
    output_text[i] = output_text[i].upper()

# Convert from list to text.
output_phrase = ''.join(output_text)

# Display the output.
print("\nEncoded/Decoded:")
print(output_phrase)
