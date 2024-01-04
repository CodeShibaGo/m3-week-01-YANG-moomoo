import math

def century(year):

    if not isinstance(year, int) or year <= 0:
        return "Error: Year must be a positive integer"

    return math.ceil(year/100)