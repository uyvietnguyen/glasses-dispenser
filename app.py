from flask import Flask
# from . import models, routes, services
from . import routes
app = Flask(__name__)

def create_app():
    # models.init_app(app)
    routes.init_app(app)
    # services.init_app(app)
    return app

if __name__ == '__main__':
    app.run()
