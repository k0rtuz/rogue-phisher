from app import init_app, db
from app.models import User

app = init_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


if __name__ == '__main__':
    app.run()
