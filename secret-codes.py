#!/usr/bin/env python3


# VARIABLES
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
opt3 = '3'


# FUNCTIONS
def convert_text(text_to_convert, transformation):
    converted_text = []
    for c in text_to_convert:
        if c not in transformation.keys():
            converted_text.append(c)
        else:
            converted_text.append(transformation[c])
    return converted_text
    
def encode_opt1(orig_phrase):
    encode_pairs = dict(zip(alphabet, opt1))
    output = convert_text(orig_phrase, encode_pairs)
    return output
    
def decode_opt1(orig_phrase):
    encode_pairs = dict(zip(alphabet, opt1))
    output = convert_text(orig_phrase, encode_pairs)
    return output
    
def encode_opt2(orig_phrase):
    encode_pairs = dict(zip(alphabet, opt2))
    output = convert_text(orig_phrase, encode_pairs)
    return output
    
def decode_opt2(orig_phrase):
    decode_pairs = dict(zip(opt2, alphabet))
    output = convert_text(orig_phrase, decode_pairs)
    return output
    
def encode_opt3(orig_phrase):
    out1 = encode_opt1(orig_phrase)
    out2 = encode_opt2(out1)
    return out2
    
def decode_opt3(orig_phrase):
    out2 = decode_opt2(orig_phrase)
    out1 = decode_opt1(out2)
    return out1


# PROCESSING
# Determine code to use.
picked_code = ''
while not picked_code:
	#print("\nPlease choose your code option (1, 2, or 3):")
	response = input("Code (1|2|3): ")
	if response == '1':
		picked_code = opt1
	elif response == '2':
		picked_code = opt2
	elif response == '3':
	    picked_code = opt3
	else:
		print("\nPlease choose '1', '2', or '3'.")

# Determine action to perform.
if picked_code != opt1:
    action = ''
    while not action:
        #print("\nDo you want to [e]ncode or [d]ecode?")
        response = input("[e]ncode | [d]ecode: ")
        if response == 'encode' or response == 'e':
            action = 'encode'
        elif response == 'decode' or response == 'd':
            action = 'decode'
        else:
            print("\nYou obviously didn't type 'encode' or 'decode'. Try again.")

# Get user input.
#print("\nEnter your phrase:")
original_phrase = input("Phrase: ")

# Note which characters are capitalized.
num = 0
uppers = []
for l in original_phrase:
    if l.isupper():
        uppers.append(num)
    num += 1

# Make all letters lowercase before converting.
text_to_convert = original_phrase.lower()

# Convert the text (output as a list) using the dictionary.
if picked_code == opt1:
    converted_text = encode_opt1(text_to_convert)
elif picked_code == opt2:
    if action == 'encode':
        converted_text = encode_opt2(text_to_convert)
    if action == 'decode':
        converted_text = decode_opt2(text_to_convert)
elif picked_code == opt3:
    if action == 'encode':
        converted_text = encode_opt3(text_to_convert)
    if action == 'decode':
        converted_text = decode_opt3(text_to_convert)

# Prepare the output with correct capitalization.
output_text = converted_text
for i in uppers:
    output_text[i] = output_text[i].upper()

# Convert from list to text.
output_phrase = ''.join(output_text)

# Display the output.
print("Result:")
print(output_phrase)

