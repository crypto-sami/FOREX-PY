import base64
from pathlib import Path
import mailtrap as mt

def send_email(addr, name, ctime, latest, final_change, last_date, last_time):
  welcome_image = Path(__file__).parent.joinpath("welcome.png").read_bytes()
  mail = mt.Mail(
    sender=mt.Address(email="me@sturk.au", name="Foreign Exchange Notifier"),
    to=[mt.Address(email=addr, name=name)],
    subject="Foreign Exchange Notifier",
    text="Daily Alert",
    #html=str(open("msg.html", "r").read()),
    html= """
    <!doctype html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      </head>

      <body style="font-family: sans-serif;">
        <div style="display: block; margin: auto; max-width: 600px;" class="main">

          <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">
            Foreign Exchange Notifier 
          </h1>

          <p>Get emails daily about the latest news on foreign exchnage rates for multiple currencies</p>
          <img alt="Inspect with Tabs" src="cid:welcome.png" style="width: 100%;">
          <p>Emails are sent once per day, normally early in the morning</p>
          <p>To learn more visit https://www.sturk.au</p>
          <p>Price as of """ + ctime +"""</p>
          <p>1 GBP buys: """ + str(latest) +""" AUD as of """ + str(ctime) +"""


        </div>
      
        <style>
            .main { background-color: white; }
            a:hover { border-left-width: 1em; min-height: 2em; }
        </style>

      </body>
    </html>""",
    category="Test",
    attachments=[
      mt.Attachment(
        content=base64.b64encode(welcome_image),
        filename="welcome.png",
        disposition=mt.Disposition.INLINE,
        mimetype="image/png",
        content_id="welcome.png",
      )
    ],
    headers={"X-MT-Header": "Custom header"},
    custom_variables={"year": 2023},
  )
  client = mt.MailtrapClient(token="8b67ab369bd1f5529245fcacdb42e6b7")
  client.send(mail)

