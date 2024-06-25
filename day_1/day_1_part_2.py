# this solution is incomplete

import re

file = open('input_test.txt', 'r')

numbers = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
    'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19
}

match_pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in numbers.keys()) + r')\b')

def forwardMatch (line):
    first_text_match = None
    earliest_index = float('inf')  # Start with infinity as a placeholder
    for key in numbers:
        index = line.find(key)  # Get the index of the key in the string
        if index != -1 and index < earliest_index:  # Check for a valid match and if it's earlier than the current earliest
            earliest_index = index
            first_text_match = key
    return first_text_match

def lastTextMatch (line):
    last_text_match = None
    latest_index = -1
    for key in numbers:
        index = line.rfind(key)  # Get the index of the last occurrence of the key in the string
        if index > latest_index:   # Check if the current key is found later than the previous matches
            latest_index = index
            last_text_match = key
    return last_text_match

def initialText (line):
    match = re.search(r"\d", line)
    return line[:match.start()] if match else text

def trailingText (line):
    match = re.search(r"\d", line)
    return line[:match.start()] if match else text

def add_number (file):
    total = 0
    for line in file:
        num = []
        # Replace overlapping word-numbers while prioritizing longer matches (e.g., 'twone' -> '21')
        # for word, digit in sorted(numbers.items(), key=lambda item: -len(item[0])):
        #     line = line.replace(word, str(digit))  # Replace directly inline

        # word_length = sum(1 for char in line if char != "\n")

        first_text_match = forwardMatch (line)
        print (first_text_match)

        last_text_match = lastTextMatch (line)
        print (last_text_match)

        forwardSearch = initialText(line)
        reverseSearch = trailingText(line)

        if first_text_match in initialText:
            first_text_match = numbers[first_text_match]
            num = num.append(str(first_text_match))
        
        for char in line: 
            if char.isdigit():
                num.append(str(char))

        if last_text_match in 
        
        if len(num) > 1:
            final_digit = num[0] + (num[-1])

        elif len(num) == 1:
            final_digit = num[0] + num[0]
        
        else:
            pass

        total = total + int(final_digit)
        print(final_digit)
    return total

print (add_number(file))

