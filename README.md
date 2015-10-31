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

    pip install -r requirements.txt
