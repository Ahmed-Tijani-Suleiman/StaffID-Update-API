import os
import urllib
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
#SQL Server
#ODBC Driver 17 for SQL Server
# Connect to the database

#Username = os.environ.get("Username")
#Password = os.environ.get("Password")

#connection_string = "DRIVER={{SQL Server}};SERVER=172.30.52.89;DATABASE=ENHANCE;UID=%s;PWD=%s" %(Username, Password)

#connection_string = "DRIVER={{SQL Server}};SERVER=172.30.52.89;DATABASE=ENHANCE;UID={0};PWD={1}".format(Username, Password)

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=PHEDETSLT33666\SQLEXPRESS;DATABASE=Portal;Trusted_Connection=yes"

params = urllib.parse.quote_plus(connection_string)
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
SQLALCHEMY_TRACK_MODIFICATIONS = False