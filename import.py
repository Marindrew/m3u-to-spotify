
# Add tracks to 'Your Collection' of saved tracks

# import pprint
import sys
import json
import unicodedata
import re

import spotipy
import spotipy.util as util

scope = 'playlist-modify-public'


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def find_spotify(name):
    search = sp.search(name)
    items = search['tracks']['items']
    if len(items) > 0:
        uri = items[0]['uri']
        return uri
    return None


def import_tracks(file, sp):
    songs = []
    with open(file, 'r') as f:
        songs = json.load(f)

    spotify_tracks = []
    for i, song in enumerate(songs):
        track_name = ''.join([song['artist'], ' ', song['title']])
        alternative_name = re.sub(
            "([\(\[]).*?([\)\]])", "\g<1>\g<2>",
            track_name
        )
        alternative_name = re.sub(r'[^\w]', ' ', alternative_name)

        found = find_spotify(track_name)
        if found is not None:
            print('Found {}'.format(track_name.encode('utf-8')))

        if found is None:
            # print('Not found, searching {}'.format(alternative_name.encode('utf-8')))
            found = find_spotify(alternative_name)
            if found is not None:
                print('Found {}'.format(alternative_name.encode('utf-8')))
        if found is not None:
            spotify_tracks.append(
                unicodedata.normalize('NFKD', found).encode('ascii', 'ignore')
            )

    return spotify_tracks


if len(sys.argv) > 2:
    filename = sys.argv[1]
    username = sys.argv[2]
    playlist_id = sys.argv[3]
else:
    print("Usage: %s filename username playlist" % (sys.argv[0]))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    user = sp.current_user()
    tracks_ids = import_tracks(filename, sp)
    # user_playlist_add_tracks
    track_ids_chunks = chunks(tracks_ids, 20)
    for i, track_ids_element in enumerate(track_ids_chunks):
        results = sp.user_playlist_add_tracks(
            user['id'],
            playlist_id,
            track_ids_element
        )
        print(results)
else:
    print("Can't get token for", username)
