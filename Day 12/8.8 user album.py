def make_album(artist_name, album_title, no_of_songs = None):
    
    if no_of_songs:
        album = {"artist name": artist_name, "album_Title": album_title, "No of songs": no_of_songs}
    else:
        album = {"artist name": artist_name, "album_Title": album_title}
    
    return album
 

while True:
    print("\nEnter artist name: \nType 'q' to exit")
    aName = input("")

    print("\nEnter album name: \nType 'q' to exit")
    aTitle = input("")

    print("\nEnter total songs: \nType '0' to exit")
    songs = int(input())

    repeat = input("Do you want to give another album info?   (yes/no)\n")
    if repeat == "no":
        break
    else:
        continue


print(make_album(aName, aTitle, songs))


#will edit this later as the dictionary can store only one valeue