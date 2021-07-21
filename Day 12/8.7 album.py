def make_album(artist_name, album_title, no_of_songs = None):
    
    if no_of_songs:
        album = {"artist name": artist_name, "album_Title": album_title, "No of songs": no_of_songs}
    else:
        album = {"artist name": artist_name, "album_Title": album_title}
    
    return album

print(make_album("Justin Bieber", "Anyone"))
print(make_album("Shawn Mendes", "Monster", 5))