# from flask import Flask, request, render_template
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)