import argparse
import json
import sys


def parse_arguments():
    p = argparse.ArgumentParser(
        description='A script to import a m3u playlist into Spotify'
    )
    p.add_argument(
        '-f',
        '--file',
        help='Path to m3u playlist file',
        type=argparse.FileType('r'),
        required=True
    )
    return p.parse_args()


def load_playlist_file(playlist_file):
    tracks = []
    try:
        content = [
        line.strip() for line in playlist_file if line.strip() and line.startswith("#")
        ]
    except Exception as e:
        print(
            'Playlist file "%s" failed load: %s' % (playlist_file, str(e))
        )
        sys.exit(1)
    else:
        for track in content:
            spl = track.split(",", 1)
            if len(spl) > 1:
                artistTitle = spl[1].split("-", 1)
                if len(artistTitle) > 1:
                    tracks.append(
                        {'title': artistTitle[1], 'artist': artistTitle[0]}
                    )
        return tracks


args = parse_arguments()
playlist = load_playlist_file(args.file)
out = json.dumps(playlist)
print (out)
text_file = open("songs.json", "w")
text_file.write(out)
text_file.close()
