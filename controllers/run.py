from flask import Flask, request, redirect, session
import views
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def run():
    resp = twilio.twiml.Response()

    if
    with resp.message("Hello, Mobile Monkey") as m:
        m.media('http://demo.twilio.com/owl.png')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
