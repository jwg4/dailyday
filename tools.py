from flask import Blueprint
from extensions import autodoc

tools_blueprint = Blueprint(
    'tools',
    __name__
)


@tools_blueprint.route('/health')
def health_check():
    """ Check that the app is up and running. """
    return "OK", 200


@tools_blueprint.route('/docs')
def html_doc():
    return autodoc.html()
