from twilio.rest import Client

account_sid = 'AC193d748d25503840854f2c96157c9367'
auth_token = '2e77fd39f959a8d3b11c0473da826581'
client = Client(account_sid, auth_token)

def send_love():

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Good Night Love',
        to='whatsapp:+8801687849347'
    )

    print(message.sid)