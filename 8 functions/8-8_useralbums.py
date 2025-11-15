##user albums##
#start with program from exercise 8-7
#write a while loop that allows users to enter an albums artist and title
#once you have that information, call make_album() with the users input and
#print the dictionaryu that's created. be sure to cinlude a quit value in the 
#while loop

def make_album(artist_name,album_title,album_songs=None):
    """takes in artist name, album title and amount of songs on album"""
    album = {
        'artist name':artist_name,
        'album title':album_title,
    }
    
    if album_songs is not None:
        album['songs'] = album_songs
    return album

while True:
    print("type q to quit at anytime")
    
    
    artist_name = input("please enter artist name:")
    if artist_name == 'q':
        break

    album_title = input("please enter album title: ")
    if album_title == 'q':
        break
    
    album_songs = input("please enter amount of songs (if any)")
    if album_songs == 'q':
        break
    else:
        album_songs = int(album_songs)
        
    album1 = make_album(artist_name,album_title,album_songs)
    
print(album1)

#when taking a string and wanting it to integer in while loop its important to
#remember it needs to be stored, cant just do int(album_songs), it has to 
#stored! album_songs = int(album_songs)


