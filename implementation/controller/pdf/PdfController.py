from implementation.controller import Controller
from flask import Flask, render_template, make_response
import pdfkit
import pyqrcode


class PdfController(Controller):

    def __init__(self):
        pass

    def get_qr_code(self, key):
        qr = pyqrcode.create(key)
        return qr.png('static/image/qrcode/' + key + '.png', scale=5)

    def create_pdf(self):
        template = render_template('pdf/station.html')
        pdf = pdfkit.from_string(template, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=sportsday.pdf'

        return response


