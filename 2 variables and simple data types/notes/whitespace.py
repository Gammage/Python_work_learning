# whitespace is space, new tab, end of line symbols. that sort of thing

print("python")

# tab
print("\tpython")

# newline
print("\npython\nc\nJavaScript")

# removing whitespace
favourite_language = ' english '
favourite_language = favourite_language.rstrip()
favourite_language = favourite_language.lstrip()
print(favourite_language)

# note that in order to permenantly apply the removal of whitespace, you have to assign the stripped value with the value name.
# thats why to remove the LEFT white space on lstrip you go favourite language equals favourite language minus the left whitespace.
# see above

nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)


