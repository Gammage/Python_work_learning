# dinner table wont arrive in time for dinner, now only space for two guests. exercise
dinner_people = ['BUMMY', 'Rob', 'mum', 'ben', 'Katie', 'matt']
print(f'reducing people around the dinner table. {dinner_people}')


removed_matt = dinner_people.pop()
print(f"sorry cant invite {removed_matt}")


removed_katie = dinner_people.pop()
print(f'sorry cant invite {removed_katie}')

removed_ben = dinner_people.pop()
print(f'sorry {removed_ben} you aint comin')

removed_mum= dinner_people.pop()
print(f'SORRY {removed_mum}')

print(f'there should be only two people left: {dinner_people}')
#note that when you delete the first list item (BUMMY), theres only one person on list (ROB) so the value is 0 for each. 
#I could use a slice, which is like [0:1], but for this exercise i just deleted using individual list items
del dinner_people[0]
del dinner_people[0]
print(dinner_people)





