from flask import Blueprint, request, render_template, redirect, url_for
from .forms import *
from ai_api import generatePlaylist, parsePlaylist, generateImage

app = Blueprint("routes",__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    if request.method == 'POST' and form.validate_on_submit:
        artist = form.artist.data
        song = form.song.data
        number_of_songs = form.number_of_songs.data
        playlist = generatePlaylist(artist, song, number_of_songs)
        playlist_dict = parsePlaylist(playlist)
        playlist_pic = generateImage(playlist_dict['dalle_prompt'])
        return render_template('playlist.html', form=form, playlist_name=playlist_dict['playlist_name'],
                               description=playlist_dict['description'],
                               song_title_list=playlist_dict['song_title_list'],
                               artist_list=playlist_dict['artist_list'],
                               playlist_pic=playlist_pic)