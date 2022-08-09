"""
Collatz conjecture program
"""

def steps(number):
    steps = 0
    numbr = number
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while numbr > 1:
        if numbr % 2 == 0:
            numbr = numbr / 2
        else:
            numbr = numbr*3 + 1
        steps += 1
    if numbr <= 1:
        return steps