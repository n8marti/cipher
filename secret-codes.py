#!/usr/bin/env python3

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

picked_code = ''
while not picked_code:
	print("\nPlease choose your code option (1 or 2):")
	response = input()
	if response == '1':
		picked_code = opt1
	elif response == '2':
		picked_code = opt2
	else:
		print("You obviously didn't type 'opt1' or 'opt2'. Try again.")

# Map the characters together in a dictionary.
encode_pairs = dict(zip(alphabet, picked_code))
decode_pairs = dict(zip(picked_code, alphabet))

transformation = encode_pairs
if picked_code == opt2:
	transformation = ''	
	while not transformation:
		# Choose to encode or decode.
		print("\nDo you want to [e]ncode or [d]ecode?")
		response = input()
		if response == 'encode' or response == 'e':
			transformation = encode_pairs
		elif response == 'decode' or response == 'd':
			transformation = decode_pairs
		else:
			print("You obviously didn't type 'encode' or 'decode'. Try again.")


# Get user input.
print("\nEnter your phrase:")
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


# Convert the text (output as a list) using the dictionary.
converted_text = []
for c in text_to_convert:
    if c not in transformation.keys():
        converted_text.append(c)
    else:
        converted_text.append(transformation[c])

# Prepare the output with correct capitalization.
output_text = converted_text
for i in uppers:
    output_text[i] = output_text[i].upper()

# Convert from list to text.
output_phrase = ''.join(output_text)

# Display the output.
print("\nResult:")
print(output_phrase)

