# May 18.2022

def make_album(artist_name, album_name, no_songs=None):
    """Create dictionary of album information."""
    album = {'artist': artist_name,
             'album': album_name,
             }
    if no_songs:
        album['songs'] = no_songs
    return album

while True:
    print("\nLets add an album!")
    print("Press 'q' to quit at any time.")

    art_name = input("Artist name?: ")
    if art_name == 'q':
        break
    alb_name = input("Album name?: ")
    if alb_name == 'q':
        break
    num_songs = input("Number of songs?: ")
    if num_songs == 'q':
        break

    album = make_album(art_name, alb_name, num_songs)
    print(album)
