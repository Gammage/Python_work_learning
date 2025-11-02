# so this exercise is to use every function mentioned in this chapter, but im using methods too...

league_chars = ['shaco','trundle','khazix','lee sin','sion']
print(f'list of league characters {league_chars}')
print(f'this is the list temporarily sorted {sorted(league_chars)}')
print(f'the list is {len(league_chars)} characters long')
print(f'this is the list currently, not changed {league_chars}')
# league_chars.pop()
print(f'the character {league_chars.pop()} is not really a jungler')
league_chars.insert(2, 'jarvan') #integer then string
print(f'added jarvan into the list {league_chars}')
league_chars.sort(reverse=False)
print(f'sorted the list a-z {league_chars}')
league_chars.remove('lee sin')
print(f'deleted lee sin from the list {league_chars}')
del league_chars[0]
print(f'just using the del method so cya jarvan {league_chars}')

