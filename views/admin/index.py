from flask import render_template

from models import storage, CNC
from views.admin import admin_view


@admin_view.route('/', methods=['GET'], strict_slashes=False)
def index():
    swift_requests = storage.all('SwiftRequest')
    actions = [
        {
            'label': 'Update',
            'url': '/admin/swift_request/',
            'color': 'primary',
            'icon': 'edit'
        },
    ]
    return render_template(
        'index.html',
        swift_requests=swift_requests,
        page={
            'title': 'Dashboard',
        },
        actions=actions
    )
