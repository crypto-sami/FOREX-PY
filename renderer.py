from jinja2 import Environment, FileSystemLoader
import csv
from ast import Return
from operator import truediv
import smtplib
import mailsend
from datetime import datetime
from currency_converter import CurrencyConverter


def render_html(ctime, latest):
    filename = 'output.html'
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("template.html")
    content = template.render(
        ctime=ctime,
        latest=latest,
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")

