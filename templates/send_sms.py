# Download twilio python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC441bb6b31b3d4ae5c4c3fab98bfda5c2"
auth_token = "35c0d3ad9608b998217e7eb9a1b88796"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="19037010300", from_="+18183056583", body="Where da hell are you humph")

