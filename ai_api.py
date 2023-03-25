import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def generatePlaylist(artist, song, number_of_songs):
    prompt = artist + ' | ' + song + ' | ' + str(number_of_songs)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': """You are a playlist creator for a website called Playlist Creator AI. The prompt you receive will contain an artist's name, a song title, and a number for how many songs you will add to the playlist. Each song you recommend must be similar to the given song. Do not choose songs that are the same name or artist. The artist's name, song title, and the number will be separated by this symbol: "|". You will come up with a playlist title, a description, and a bulletpoint list of songs up to the requested number of songs. When listing the artists and songs, format it like this: "{song title} by {artist name}". Then, you will create a prompt that can be put into DALL-E that would represent the playlist. Do not write any explanations or other words, just reply with the playlist name, description, artists, songs, and DALL-E prompt. Your format will be like this:
            Playlist Name: <insert playlist name here>

            Description: <insert description here>

            Songs:
            <insert list of songs here>

            DALL-E Prompt: <insert prompt here>"""},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=2048
        
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def parsePlaylist(playlist):
    # # Split the input string into different sections based on the line breaks
    # sections = playlist.split('\n\n')

    # # Parse the sections into separate variables
    # playlist_name = sections[0].split(': ')[1].strip()
    # description = sections[1].split(': ')[1].strip()
    # song_list = sections[2].strip().split('\n')[1:]
    # dalle_prompt = sections[3].split(': ')[1].strip()

    # Split the string into lines
    lines = playlist.split('\n')

    # Extract the playlist name
    playlist_name = lines[0].split(': ')[1]

    # Extract the playlist description
    description = lines[2].replace('Description: ', '')

    # Extract the song titles and artist names
    song_title_list = []
    artist_list = []
    for line in lines[4:-2]:
        print(line)
        if 'Songs:' in line:
            continue
        if "by" in line:
            song_title, artist = line.split(" by ")
        else:
            song_title, artist = line.split('"')[1], line.split('"')[3]
        song_title_list.append(song_title.replace('-', '').replace('"', ''))
        artist_list.append(artist)

    # Extract the DALL-E prompt
    dalle_prompt = lines[-1].split(': ')[1]

    return {'playlist_name': playlist_name,
            'description': description,
            'song_title_list': song_title_list,
            'artist_list': artist_list,
            'dalle_prompt': dalle_prompt}

def generateImage(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512",
    )
    return response["data"][0]["url"]
