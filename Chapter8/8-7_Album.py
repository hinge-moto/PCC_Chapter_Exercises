# May 18.2022

def make_album(artist_name, album_name, no_songs=None):
    """Create dictionary of album information."""
    album = {
        'artist': artist_name,
        'album': album_name,
        }
    if no_songs:
        album['songs'] = no_songs
    return album

rust_in_peace = make_album('Dave Mustaine', 'Rust In Peace', 10)
print(rust_in_peace)
