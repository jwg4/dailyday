from flask import Blueprint

tools_blueprint = Blueprint(
    'tools',
    __name__
)

@tools_blueprint.route('/health')
def health_check():
    return "OK", 200