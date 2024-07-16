# host.docker.internal

HOSTNAME = '34.64.140.98'
PORT = 3306
USERNAME = 'coitpark'
PASSWORD = '2955park'
DATABASE = 'simple_board'
CHARSET = 'utf8'
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
