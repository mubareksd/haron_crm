from flask import Blueprint

admin_view = Blueprint('admin_view', __name__, url_prefix='/admin')

from views.admin.index import *
from views.admin.swift_request import *
