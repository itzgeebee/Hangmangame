# A spotify time machine that creates a playlist from a specified billboard top 100 from the past using spotipy
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ClIENT_ID = "Your spotify client Id"
SPOTIFY_CLIENT_SECRET = "Your spotify client secret"
SPOTIFY_REDIRECT_URI = "http://example.com"

#login to stotify
auth_manager = SpotifyOAuth(client_id=SPOTIFY_ClIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                            redirect_uri=SPOTIFY_REDIRECT_URI, scope="playlist-modify-private")
sp = spotipy.Spotify(auth_manager=auth_manager)

#get user id
user = sp.current_user()["id"]
print(user)

billboard_url = "https://www.billboard.com/charts/hot-100/"

#get user input
search_date = input("What year do you want to travel to? Enter date in this format: YYYY-MM-DD\nAnswer: ")

# use beautifulsoup to scrape the billboard top 100 songs of the year from user input 
user_search_param = f"{billboard_url}{search_date}"
response = requests.get(user_search_param).text
soup = BeautifulSoup(response, "html.parser")
title = soup.find_all(name="h3", class_="a-no-trucate")
artiste = soup.find_all(name="span", class_="a-no-trucate")
position = soup.find_all(name="span", class_="a-font-primary-bold-l")

song_list = [title.get_text() for title in title]

# print(song_list[0])

# search and collate the URI for the songs collated from billboard
uri = []
for i in song_list:
    result = sp.search(q=f"track:{i} year:{2001}", type="track")
    try:
        name = result["tracks"]["items"][0]["uri"]
        uri.append(str(name))
    except IndexError:
        print(f"{i} is not on spotify, skipped\n")

#bill_board_play_list = sp.user_playlist_create(user=user, name=f"{search_date}", description=f"A playlist of Billboard top 100 for {search_date}", public=False)
play_list_ID ='52xXD5B143w4acxVg2x5Cb'

#sp.playlist_add_items(playlist_id=play_list_ID, items= uri)

print(sp.playlist(playlist_id=play_list_ID))





