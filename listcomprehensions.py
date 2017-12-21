prizes = [1,2,3,4,5];

dbl_prizes = [];

for prize in prizes:
    dbl_prizes.append(prize*2)

# Here we get [2,4,6,8,10]
print(dbl_prizes)


# Comprehension method

dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

# Squaring of numbers

square_numbers = [];
# Using the list comprehension method
square_numbers = [prize*prize for prize in prizes]
print(square_numbers)

# Only even squared numbers
even_squared_numbers = [square_number for square_number in square_numbers if square_number % 2 == 0]
print(even_squared_numbers)

# Only odd squared numbers
odd_squared_numbers = [square_number for square_number in square_numbers if square_number % 2 != 0]
print(odd_squared_numbers)

