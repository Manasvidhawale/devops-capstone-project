"""
Package: service
Package for the Customer Accounts microservice
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Configure Talisman security headers
talisman = Talisman(
    app,
    content_security_policy=None,
    force_https=False
)

# Configure CORS policies
CORS(app)

from service import routes, models