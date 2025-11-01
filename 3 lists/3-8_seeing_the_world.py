#exercise in the book. storying five places in the world i want to see
countries = ['america','japan','korea','france','spain']
# countries.sort()
#sort is permenantly changing the list
print(countries)
print(sorted(countries))
print(sorted(countries, reverse=True)) # this still uses sorted, reverses the list but not change the permenant list. not actually shown in book...
print(countries)

countries.reverse()
print(countries)
countries.reverse()
print(countries)

countries.sort(reverse=False)
print(countries)

countries.sort(reverse=True)
print(countries)

# print(f'{}')