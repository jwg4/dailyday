from flask import Flask

from extensions import autodoc

from tools import tools_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(tools_blueprint)
    autodoc.init_app(app)
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
