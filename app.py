from flask import Flask
from api.click import click_bp

app = Flask(__name__)
app.register_blueprint(click_bp, url_prefix="/api/click")

@app.route("/")
def index():
    return "Tracking API for muataiday.store is running."

if __name__ == "__main__":
    app.run()
