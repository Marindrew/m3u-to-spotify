m3u-to-spotify
=============

Part 1: Download `.m3u` playlist from vk.com
--------------------

You can use [https://chrome.google.com/webstore/detail/musicsig-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5-vk/hanjiajgnonaobdlklncdjdmpbomlhoa](Music Sig) to download `.m3u` playlist from vk.com. Save it in the project folder.

Part 2: Install dependencies of the project
--------------------

Then, install dependencies:
  pip install -r requirements.txt

Part 3: Convert m3u tracks to json
--------------------------

Just run, where PLAYLIST_FILENAME is the name of your vk playlist
  
    python convert-m3u-2-json.py --file PLAYLIST_FILENAME.m3u
  
After this, you will have songs.json in the same folder.

Part 3: upload tracks to spotify
--------------------------------

1. Go to [https://developer.spotify.com/my-applications/](Spotify developer console) and press `Create an app`.
2. Give it a name and description and take `Client ID` and `Client Secret` and generate environment variables:
3. `SPOTIPY_REDIRECT_URI` can be set to any website you trust in the developer console. I just use my website https://hiboo.co but you can use yours or any other website. Keep in mind that those website will in theory get the access token of your spotify account, so make sure to delete the app after you are done :). `PLAYLIST_ID` can be found in the link to your spotify playlist. For example `https://open.spotify.com/user/11165866010/playlist/6AJ6BZYORhywkrJ8nL9DtH` has `6AJ6BZYORhywkrJ8nL9DtH` at the end.


    SPOTIPY_CLIENT_ID='HERE_IS_YOUR_CLIENT_ID_FROM_NEW_SPOTIFY_APP' SPOTIPY_CLIENT_SECRET='HERE_IS_YOUR_CLIENT_SECRET_FROM_NEW_SPOTIFY_APP' SPOTIPY_REDIRECT_URI='https://hiboo.co' python import.py songs.json YOUR_SPOTIFY_EMAIL PLAYLIST_ID

    or example

    SPOTIPY_CLIENT_ID='HERE_IS_YOUR_CLIENT_ID_FROM_NEW_SPOTIFY_APP' SPOTIPY_CLIENT_SECRET='HERE_IS_YOUR_CLIENT_SECRET_FROM_NEW_SPOTIFY_APP' SPOTIPY_REDIRECT_URI='https://hiboo.co' python import.py songs.json youremail@gmail.com 6AJ6BZYORhywkrJ8nL9DtH

4. This will open the browser window. Just copy the url and paste it in the terminal. This will start the process of copying


Enjoy!