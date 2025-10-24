# string is a series of characters. this file is part of the string chapter pg20

name = "ada lovelace"
print(name.title())

# the title is the method. it acts on the name variable which is ada lovelace,
# its told to do so by the literal dot after the name.
# as the title method doesnt need any other info (capitalises each word in string to title case) it doesn't need any other info in the parenthesis.
# paranthesis always follows a method, methods do usually need more info tho.

name = "ada lovelace"
print(name.upper())
print(name.lower())

# apparently lowercase is good for data storage!

first_name = "ada"
Last_name = "lovelace"
full_name = f"{first_name} {Last_name}"
print(f"Hello, {full_name.title()}!")

# notice the F? this turns the string into a f-string (format string). it formats the info in the {} curly braces

first_name = "ada"
Last_name = "lovelace"
full_name = f"{first_name} {Last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# instead of printing the output, we store it in message and just print the message. much simpler and cleaner tbh