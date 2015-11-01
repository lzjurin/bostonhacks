from flask import Flask, request, redirect, session
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def run():
    resp = twilio.twiml.Response()

    message = "Hiya!"
    if (request.values):
        from_num = request.values.get('From', None)
        if from_num:
            message = "Hi " + from_num

    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
