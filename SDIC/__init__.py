from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = "SDIC/static/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nono@192.168.219.100/sdic'
app.config['SECRET_KEY'] = '@#$!@#%!@#%!@#%!@#!@#$!@#%!@#$!'

ALLOWED_EXTENSIONS = set(['png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'bmp', 'BMP', 'gif', 'GIF'])

from SDIC.routes import index

app.register_blueprint(index.bp, url_prefix='/')
