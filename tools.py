from flask import Blueprint

tools_blueprint = Blueprint(
    'tools',
    __name__
)


@tools_blueprint.route('/health')
def health_check():
    """ Check that the app is up and running. """
    return "OK", 200
