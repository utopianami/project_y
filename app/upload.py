from werkzeug.utils import secure_filename
import app


__author__ = 'LeeYoungNam'
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import werkzeug


ALLOWED_EXTENSIONS = set(['JPG', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



def upload(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('./app/static/ddottylog/', filename))
        return '/static/ddottylog/'+filename


