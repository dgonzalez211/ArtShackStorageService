from .app import App, db, migrate

def create_app() -> App:
    return App()
