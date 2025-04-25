from flask import Flask
from api.click import click_bp
from api.order import order_bp
from api.export import export_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(click_bp, url_prefix="/api/click")
app.register_blueprint(order_bp, url_prefix="/api/order")
app.register_blueprint(export_bp, url_prefix="/api/export")

if __name__ == "__main__":
    app.run(debug=True)
