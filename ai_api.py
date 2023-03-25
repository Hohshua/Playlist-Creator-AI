import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def generatePlaylist(artist, song, number_of_songs):
    prompt = artist + ' | ' + song + ' | ' + str(number_of_songs)
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': """You are a playlist creator for a website called Playlist Creator AI. The prompt you receive will contain an artist's name, a song title, and a number for how many songs you will add to the playlist. Each song you recommend must be similar to the given song. Do not choose songs that are the same name or artist. The artist's name, song title, and the number will be separated by this symbol: "|". You will come up with a playlist title, a description, and a numbered list of songs up to the requested number of songs. When listing the artists and songs, format it like this: "{song title} by {artist name}". Then, you will create a prompt that can be put into DALL-E that would represent the playlist. Do not write any explanations or other words, just reply with the playlist name, description, artists, songs, and DALL-E prompt. Your format will be like this:
                                        Playlist Name: <insert playlist name here>

                                        Description: <insert description here>

                                        Songs:
                                        <insert numbered list of songs here>

                                        DALL-E Prompt: <insert prompt here>"""},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=2048
        
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def parsePlaylist(playlist):
    # Split the input string into different sections based on the line breaks
    sections = playlist.split('\n\n')

    # Parse the sections into separate variables
    playlist_name = sections[0].split(': ')[1].strip()
    description = sections[1].split(': ')[1].strip()
    song_list = sections[2].strip().split('\n')[1:]
    dalle_prompt = sections[3].split(': ')[1].strip()

    print(description)
    return {'playlist_name': playlist_name,
            'description': description,
            'song_list': song_list,
            'dalle_prompt': dalle_prompt}

def generateImage(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512",
    )
    return response["data"][0]["url"]
