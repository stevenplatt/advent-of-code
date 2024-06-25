file = open('input.txt', 'r')

def add_number (file):
    total = 0
    for line in file:
        num = []
        for char in line: 
            if char.isdigit():
                num.append(str(char))
        final_digit = num[0] + (num[-1])
        total = total + int(final_digit)
    return total

print(add_number(file))
