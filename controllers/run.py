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

# Import Stormpath methods
from flask_stormpath import (
    StormpathError,
    StormpathManager,
    User,
    login_required,
    login_user,
    logout_user,
    user,
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
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'Guardian'

# Initialize Stormpath manager
stormpath_manager = StormpathManager(app)


################################################################

def checkPlatform():
    if (request.values.get('', None)):
        resp = twilio.twiml.Response()
        resp.message("Hi " + request.values.get('From', None) + "!")
        return str(resp)
    else:
        return None


@app.route("/", methods=['GET', 'POST'])
def show_posts():
    # msg = checkPlatform()
    # if msg != None:
    #     return msg
    posts = []
    for account in stormpath_manager.application.accounts:
        if account.custom_data.get('posts'):
            posts.extend(account.custom_data['posts'])

    posts = sorted(posts, key=lambda k: k['date'], reverse=True)
    return render_template('show_posts.html', posts=posts)


@app.route('/add', methods=['POST'])
@login_required
def add_post():
    # msg = checkPlatform()
    # if msg:
    #     return msg
    if not user.custom_data.get('posts'):
        user.custom_data['posts'] = []

    user.custom_data['posts'].append({
        'date': datetime.utcnow().isoformat(),
        'title': request.form['title'],
        'text': request.form['text'],
    })
    user.save()

    flash('New post successfully added.')
    return redirect(url_for('show_posts'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # msg = checkPlatform()
    # if msg:
    #     return msg
    error = None

    if request.method == 'POST':
        try:
            _user = User.from_login(
                request.form['email'],
                request.form['password'],
            )
            login_user(_user, remember=True)
            flash('You were logged in.')

            return redirect(url_for('show_posts'))
        except StormpathError, err:
            error = err.message

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    # msg = checkPlatform()
    # if msg:
    #     return msg
    logout_user()
    flash('You were logged out.')

    return redirect(url_for('show_posts'))

################################################################

if __name__ == "__main__":
    app.run()
