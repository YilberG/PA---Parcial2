import mysql.connector
from . import settings

db = mysql.connector.connect(
    host = settings.MYSQL_HOSTNAME,
    user = settings.MYSQL_USERNAME,
    password = settings.MYSQL_PASSWORD,
    database = settings.MYSQL_DATABASE,
    port = settings.MYSQL_PORT
)
db.autocommit = True