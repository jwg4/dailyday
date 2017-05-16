from flask import Flask

from tools import tools_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(tools_blueprint)
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
