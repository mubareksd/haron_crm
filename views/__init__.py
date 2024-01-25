from flask import Blueprint
app_view = Blueprint('app_view', __name__, url_prefix='/')

from views.index import *