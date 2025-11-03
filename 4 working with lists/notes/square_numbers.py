# using the range for square numbers example
# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# We start with an empty list called squares.
# The for loop goes through the numbers 1 through 10.
# For each number, we calculate value ** 2 (value squared) and store it in 'square'.
# We then append that squared value to the squares list.
# After the loop finishes, we print the final list of squared numbers.

#the cleaner way for this
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

#focus on writing code that makes sense first, then make it cleaner once it gets easier. the shorter version is better for big things but,
#its the case of simplicity is beautiful.

#LIST COMPREHENSION
#advanced way of writing lists, people will use this often when writing code. get used to it, i guess?

squares= [value**2 for value in range(1,11)]
print(squares)

