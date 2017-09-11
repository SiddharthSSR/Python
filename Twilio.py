# To message someone on their phone through the app Twilio

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5514a64d7046377cc09adae3ede9c804"
# Your Auth Token from twilio.com/console
auth_token  = "2c9012c6f2e2a510bf0b8929603ba868"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919873347409", # Receiver's Number
    from_="(856) 617-5463", # Twilio Number
    body="Hello i am using python")

print(message.sid)