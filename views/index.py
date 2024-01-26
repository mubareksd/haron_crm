from flask import render_template

from models import storage
from views import app_view


@app_view.route('/', methods=['GET'], strict_slashes=False)
def index():
    swift_requests = storage.all('SwiftRequest')
    return render_template(
        'index.html',
        swift_requests=swift_requests,
        page={
            'title': 'Home',
        }
    )
