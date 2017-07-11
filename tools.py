from flask import Blueprint, jsonify
from extensions import autodoc

tools_blueprint = Blueprint(
    'tools',
    __name__
)


@tools_blueprint.route('/health')
def health_check():
    """ Check that the app is up and running. """
    status = {'status': 'OK'}
    return jsonify(status)


@tools_blueprint.route('/docs')
def html_doc():
    return autodoc.html()
