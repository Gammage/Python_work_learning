##Extensions##
    #now working with examples that are complext enough that they can be extended
    #in a number of ways. use one example programs from this chapter
        #extend it by adding new keys and values, changing the context of the 
        #program, or improving the format of the output
        
##decided to create my own dictionary
##DICTIONARY KEYS ARE REFERENCES, MUCH LIKE VARIABLES IN A LIST. THEY CANT BE 
#CALLED ON LITERALLY, IE. THE NAMES IN A STRING ARE INDEXS       

league_champions = {
    'shaco':{
        'role':['jungler','support'],
        'dmg_type':['AP','AD'],
        'difficulty':'medium'
    },
    'sion':{
      'role':['top','jungler',],
      'dmg_type':['ad','tank'],
      'difficulty':'easy',  
    },
    'aphelios':{
      'role':['adc'],
      'dmg_type':['ad'],
      'difficulty':'hard',  
    },
}

new_champion = {
    'zaheen':{
        'role':['top','jungler'],
        'dmg_type':['ad'],
        'difficulty':'easy',
    },
}

league_champions.update(new_champion)

for champions, stats in sorted(league_champions.items()):
    print(f"\n{champions.title()} stats:")
    print(f"Role:")
    for stat in sorted(stats['role']):
        print(f"{stat.title()}")
    print(f"Dmg type:")
    for stat in sorted(stats['dmg_type']):
        print(f"{stat.title()}")
    print(f"Difficulty: {stats['difficulty'].title()}")
     
    