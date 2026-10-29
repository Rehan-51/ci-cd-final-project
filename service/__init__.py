"""
Package: service
Package for the application models and service routes
This module initializes the Flask service and database
"""
import sys
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman
from service import config
from service.common import log_handlers

# Create the Flask app
app = Flask(__name__)
app.config.from_object(config)

# Initialize Talisman for security headers
talisman = Talisman(app)

# Initialize CORS
CORS(app)

# Import the routes after the Flask app is created
# pylint: disable=wrong-import-position,cyclic-import,wrong-import-order
from service import routes, models  # noqa: F401 E402
from service.common import error_handlers, status  # noqa: F401 E402

# Set up logging for production
log_handlers.init_app(app)

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
