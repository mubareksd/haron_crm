from flask import render_template
from views import app_view


@app_view.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')
