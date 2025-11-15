##8-7 ALBUM EXERCISE##
#write a function called make_album()

#builds a dictionary describing music album

#function should take in an artist name and album title
    #it should return a dictionary containing these two bits of information
    #use the function to make three dictionaries representing different albums
    
#print each return value to show that the dictionaries are storing the album
#information correctly

#use none to add an optional paramter to make_album() allows you to store the
#number of songs on an album
    #if the calling line includes a value for the number of songs, add that value
    #to the albums dictionary. make at least one new function call that includes
    #the number of songs on an album
    
def make_album(artist_name,album_title,album_songs=None):
    """takes in artist name, album title and amount of songs on album"""
    album = {
        'artist name':artist_name,
        'album title':album_title,
    }
    
    if album_songs is not None:
        album['songs'] = album_songs
    return album

album1 = make_album('violet meridian','glass cities',5)
album2 = make_album('neon lanterns','echoes of tomorrow')
album3 = make_album('hollow pines','aria solstice',10239812039821)
print(album1,album2,album3,sep='\n')

