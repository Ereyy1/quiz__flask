import os
from flask import Flask

def crate_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'asdasd',
        DATABASE = os.path.join(r'C:\Users\eray\Desktop\quiz\venv\quiz', r'quiz.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db 
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app


quiz = crate_app()