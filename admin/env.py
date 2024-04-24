# host.docker.internal

HOSTNAME = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'mydb'
CHARSET = 'utf8'
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"