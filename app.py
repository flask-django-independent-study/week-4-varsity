"""Import and run app."""
from the_bank import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
