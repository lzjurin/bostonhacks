Larry Zhang, Humphrey Obuobi, Ben Zheng

This project attempts to use data from the Microsoft Band to perform activity tracking and monitor
disabled or elderly individuals in case of critical health conditions arising.


Project Steps

1. Install python first, if you can't do that we slap you.
2. Check your python version
3. Install virtual env (and pip, which comes installed)
    3a. If Python 2.4 run easy_install virtual_env
    3b. If 2.5-2.7 run easy_install-2.7 virtualenv
    3c. If 3 run the below. If you get permission denied errors use sudo python instead of just python:
        curl http://python-distribute.org/distribute_setup.py | python
        curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
4. Switch to the directory you're working in and create a virtual environment:
    cd -------
    virtualenv --no-site-packages .
5. Activate the virtual environment
    source bin/activate


6. Set up flask and twilio. To set up flask and twilio API, run the following (assuming you have pip 
and python installed and requirements.txt has been filled out):

    bin/pip install -r requirements.txt

    do NOT use pip install -r requirements.txt

To run Flask, first acitvate the virtualenv then run the server:

    source bin/activate
    (BostonHacks)$ python controllers/run.py

In order to have the website accessible to the internet, even if we run the server we need something to host it.
For that, we use Heroku!

Steps:
Get python, virtualenv, and pip (pip for resolving dependencies)
Heroku user account info:
    user: larryzhang101@gmail.com
    pw:   tSf11Wy1rY

    See keys.txt for this information as well

Install the Heroku Toolbelt on your workstation from https://devcenter.heroku.com/articles/getting-started-with-python-o
    This gives you access to the Heroku command-line client, giving you the heroku local command

Then, use 'heroku login' to log into the Heroku account.
We also need to resolve the dependency 'gunicorn' via:

    pip install gunicorn

--------
We now need to declare our process types with a Procfile. This is already done in the procfile in this repo but you can
take a look if you want to understand how it works. Now, we simply execute heroku local.
