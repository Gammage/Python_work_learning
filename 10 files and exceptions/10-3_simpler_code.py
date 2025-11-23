##SIMPLER CODE EXERCISE 10-3##
##file_reader in this section uses a temp variable, lines, to show how splitlines
#work. skip the temproary variable and loop directly over the list that spltlines()
#reutrns

from pathlib import Path

path = Path('10 files and exceptions/notes/pi_millions_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()

pi_string  = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string[:52])
print(len(pi_string))