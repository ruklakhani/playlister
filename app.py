from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Flask is Cool!!')


if __name__ == '__main__':
    app.run(debug=True)
# OUR MOCK ARRAY OF PROJECTS
playlists = [
    {'title': 'Cat Videos', 'description': 'Cats acting weird'},
    {'title': '80\'s Music', 'description': 'Don\'t stop believing!'},
    {'title': 'Absolute Bops', 'description': 'my favorite songs'}
]


@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)
