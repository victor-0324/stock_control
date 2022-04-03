from flask import Flask, g, render_template, request, redirect, Response, send_file, session, url_for, abort
from flask_sqlalchemy  import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from base64 import b64encode
import io
import os
from werkzeug.utils import secure_filename

# Criando a enginer
Base.metadata.create_all(engine)


# pegando a img
@app.route('/get-file/<filename>')
def getfile(filename):
  file = os.path.join(UPLOAD_FOLDER, filename  + '.png')
  files = os.path.join(UPLOAD_FOLDE, filename  + '.png')
  filees = os.path.join(UPLOAD_FOLDERS, filename  + '.png')
  filee = os.path.join(UPLOAD_FOLDERSS, filename  + '.png')
  return  send_file(pic, mimetype="image/png")