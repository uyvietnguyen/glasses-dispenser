def init_app(app):
    from .page import page_api
    app.register_blueprint(page_api)
    pass
