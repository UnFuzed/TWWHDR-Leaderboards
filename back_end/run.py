from flask import Flask
from api import create_app

app: Flask = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
