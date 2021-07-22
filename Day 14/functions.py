def make_album (artist_name, album_title, no_of_songs = None):
    if no_of_songs:
        album = {"artist name": artist_name, "album title": album_title, "No of  songs: ": no_of_songs}
        
    else:
        album = {"artist name": artist_name, "album title": album_title}
    
    return album

while True:

    artist = input("Enter an artist name: ")
    album = input("Enter album title: ")
    no_of_songs = int(input("Enter total songs: "))

    quit = input("Enter 'quit' to exit: ")
    if quit == "quit":
        break
    else:
        continue
       
    

print(make_album(artist, album, no_of_songs))


