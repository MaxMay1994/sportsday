
from flask import request, render_template, session, redirect, escape, url_for


class Controller(object):

    def main(self):
        return render_template('/main/index.html')
