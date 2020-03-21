from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')
#api = Blueprint('api', __name__, subdomain='api')
from .import book_manage

