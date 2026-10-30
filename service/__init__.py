"""
Package: service
Package for the application models and service routes
This module initializes the Flask service and database
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

# Create the Flask app
app = Flask(__name__)

# Initialize Talisman for security headers
# Enforce security policies and HTTP headers
talisman = Talisman(
    app,
    content_security_policy=None,
    force_https=False
)

# Initialize CORS
CORS(app)


def app_running():
    """Return status of application"""
    return True
