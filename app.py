"""Flask app."""

from flask import Flask
from models import Comment

app = Flask(__name__)


@app.route("/")
def index():
    """Home route handler."""
    return '''
    <html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Welcome!</h1>
    </body>
    </html>'''

@app.route("/coments")
def comments():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Test</title>
    </head>

    <body>
        {}
    </body>

    </html>
    """
    table = COMMENTS.table()
    return page.format(table)