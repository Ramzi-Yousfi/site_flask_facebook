import os

SECRET_KEY = "9b9(s#_@+&qf%78yyd98!=8$_a@2nh88w3ev7j%xkt99apuq@2"

FB_APP_ID = 1870024106517843

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
