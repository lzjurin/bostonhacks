# Datetime module
from datetime import datetime

# Import Flask modules
from flask import (
    Flask,
    request,
    redirect,
    session,
    abort,
    flash,
    render_template,
    url_for,
)

# Import Twilio API
import twilio.twiml

# Import custom file loader
# import imp
# routes = imp.load_source('guardianroutes', 'config/guardianroutes.py')

# Config app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '(yeg1d!r4y0q6u=52*1)==z!4isfoxrf#f6pu+-_w&93lv=)89'


if __name__ == "__main__":
    app.run()
