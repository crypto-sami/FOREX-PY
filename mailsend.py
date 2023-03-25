import base64
from pathlib import Path
import mailtrap as mt
import renderer

def send_email(addr, name, ctime, latest, final_change, last_date, last_time):
  welcome_image = Path(__file__).parent.joinpath("welcome.png").read_bytes()
  mail = mt.Mail(
    sender=mt.Address(email="me@sturk.au", name="Foreign Exchange Notifier"),
    to=[mt.Address(email=addr, name=name)],
    subject="Foreign Exchange Notifier",
    text="Daily Alert",
    html=str(open("output.html", "r").read()),
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

