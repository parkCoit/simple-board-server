# host.docker.internal

HOSTNAME = 'localhost'
PORT = 3306
USERNAME = 'coitpark'
PASSWORD = '2955park'
DATABASE = 'coitparkdb'
CHARSET = 'utf8'
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
