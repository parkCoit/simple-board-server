from admin.env import HOSTNAME, PORT, USERNAME, PASSWORD, CHARSET, DATABASE, DB_URL
from sqlalchemy import create_engine


ENGINE = create_engine(DB_URL, encoding=CHARSET, echo=True)
conn = ENGINE.connect()
