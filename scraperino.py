import requests
from bs4 import BeautifulSoup

while True:
    URL = input("Enter Spotify Playlist Link: ")
    URL = 'https://open.spotify.com/playlist/37i9dQZF1EM30dmPXagctT?si=7xt5FOLcRLmKph2j-u3eMw' if URL == '' else URL

    if 'open.spotify.com/playlist/' in URL:
        try:
            page = requests.get(URL)
            break
        except:
            print("Bad Link, try another one\n")
    else:
        print("Please enter an open.spotify Link\n")

print("\n")

soup = BeautifulSoup(page.content, 'html.parser')

songList = []
songItems = soup.find('ol').findAll('li')
for song in songItems:
    index = song.find(class_='tracklist-col__track-number').text.strip()[:-1]
    name = song.find(class_='track-name').text.strip()
    artist = song.find(class_='artists-albums').findAll('span',
                                                        dir='auto')[0].text.strip()
    album = song.find(class_='artists-albums').findAll('span',
                                                       dir='auto')[1].text.strip()
    duration = song.find(class_='total-duration').text.strip()

    songList.append({
        'index': index,
        'name': name,
        'artist': artist,
        'album': album,
        'duration': duration
    })

for song in songList:
    print(f"{song['artist']} - {song['name']}")
    print(f"Album: \"{song['album']}\"\n")

playlistName = soup.find("h1").text.strip()
creatorName = soup.find("h2").text.strip()[3:]
numberSongs = soup.find(
    'p', class_='text-silence entity-additional-info').text.strip()

print(f'\n\n"{playlistName}" by {creatorName}')
print(numberSongs)

input()
