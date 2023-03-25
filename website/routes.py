from flask import Blueprint, request, render_template
from .forms import *

app = Blueprint("routes",__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    # return render_template('index.html', form=form)
    if request.method == 'GET':
        return render_template('index.html', form=form)
    if request.method == 'POST':
        return f"You entered: {form.artist}, {form.song}"