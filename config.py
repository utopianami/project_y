import os.path

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://dbuser:dkagh123@localhost:3306/sandbox?charset=utf8&use_unicode=0"

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'